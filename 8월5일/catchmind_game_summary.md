# 캐치마인드 게임 연동 실습 정리

## 1. 핵심 요약

기존 Spring Boot 게시판 프로젝트에 캐치마인드 게임 기능을 연결. 게임방과 플레이어 구조를 만들고, WebSocket을 이용해 그림과 채팅 메시지를 실시간으로 주고받도록 구성했다. 또한 Controller, Service, DTO, Domain, Config 역할을 구분해 구조를 정리했고, 기존 인증·게시판 기능과 함께 하나의 서비스 안에서 동작하도록 통합.

핵심 구조는 다음과 같다.

```text
로그인(JWT)
   ↓
게시판
   ↓
게임 페이지
   ↓
REST API → 방 생성/참가/제시어 조회
   ↓
WebSocket(STOMP) → 채팅/게임상태/그림 실시간 동기화
   ↓
GameService
   ↓
GameRoom
```

가장 중요한 포인트는 **클라이언트가 username을 직접 보내는 방식에서 벗어나, 서버가 JWT 로그인 정보(Authentication / Principal)를 기준으로 사용자를 판단하도록 변경한 것**이다.

또한 `ngrok`을 사용해 로컬 Spring Boot 서버를 외부에 공개하여 다른 사용자가 실제로 접속해 게임할 수 있도록 연결했다.

---

## 2. 전체 실행 흐름

```text
[사용자 로그인]
      ↓
JWT 쿠키 발급
      ↓
[게시판]
      ↓
[캐치마인드 게임 페이지]
      ↓
방 생성 / 방 참가 (REST)
      ↓
WebSocket 연결
      ↓
방장 게임 시작
      ↓
서버가 제시어 선택
      ↓
현재 출제자(drawer)에게만 제시어 공개
      ↓
출제자 그림 전송
      ↓
WebSocket으로 모든 참가자에게 그림 동기화
      ↓
참가자 채팅으로 정답 입력
      ↓
정답 판정
      ↓
점수 증가 + 다음 라운드 + 출제자 변경
```

---

## 3. 주요 구성 요소와 역할

### `GameController`

게임 관련 **HTTP 요청(REST API)** 을 받는 입구.

주요 역할:

- 방 생성
- 방 참가
- 방 나가기
- 현재 로그인 사용자 확인
- 출제자에게 제시어 전달

REST 요청에서는 Spring Security의 `Authentication`을 사용해 로그인 사용자를 가져온다.

```java
Authentication authentication
authentication.getName()
```

즉 브라우저에서 username을 직접 보내지 않아도 서버가 현재 로그인 사용자를 알 수 있다.

### `GameSocketController`

실시간 통신을 담당하는 WebSocket Controller.

주요 역할:

- 실시간 채팅
- 게임 시작
- 그림 좌표 전달
- 그림판 전체 지우기
- 게임 상태 broadcast

WebSocket에서는 `Principal`을 사용했다.

```java
Principal principal
principal.getName()
```

```text
클라이언트 WebSocket 메시지
        ↓
@MessageMapping
        ↓
GameSocketController
        ↓
Principal로 사용자 확인
        ↓
GameService 호출
        ↓
/topic/... 으로 참가자들에게 broadcast
```

### `GameService`

게임의 핵심 비즈니스 로직을 담당한다.

주요 역할:

- 방 생성/조회
- 참가자 추가/삭제
- 게임 시작
- 랜덤 제시어 선택
- 정답 판정
- 다음 라운드 진행

현재 게임방은 DB가 아니라 메모리에 저장한다.

```java
ConcurrentHashMap<String, GameRoom>
```

따라서 서버를 재시작하면 만들어진 게임방은 사라진다.

### `GameRoom`

한 개의 게임방 상태를 관리하는 도메인 객체.

주요 상태:

```text
roomCode
players
hostUsername
started
round
currentDrawer
answer
```

즉 `GameRoom` 하나가 현재 한 방의 게임 상태 전체를 들고 있다.

게임방 내부 상태 변경에는 `synchronized`를 사용해 동시에 여러 요청이 들어올 때 상태가 꼬이는 것을 줄였다.

### `GamePlayer`

게임 참가자 정보를 표현한다.

```text
username
score
```

정답을 맞히면 점수를 증가시킨다.

### `GameRoomResponse`

서버의 `GameRoom` 정보를 브라우저에 전달하기 위한 응답 DTO.

중요한 점은 **answer를 포함하지 않았다는 것**이다.

```text
GameRoom
 ├─ currentDrawer
 ├─ round
 ├─ players
 └─ answer  ← 그대로 보내면 모든 사람이 정답 확인 가능

GameRoomResponse
 ├─ currentDrawer
 ├─ round
 └─ players
```

제시어는 별도 API에서 현재 drawer인지 확인한 뒤 전달한다.

---

## 4. 핵심 Spring Annotation 정리

### `@RestController`

HTTP 요청을 받고 JSON 응답을 반환하는 Controller.

```text
브라우저
 → HTTP 요청
 → @RestController
 → Service
```

게임에서는 방 생성/참가/제시어 조회 등에 사용했다.

### `@Controller`

일반 Spring Controller.

이번 게임에서는 WebSocket 메시지를 받는 `GameSocketController`에 사용했다.

### `@Service`

비즈니스 로직을 담당하는 객체를 Spring Bean으로 등록한다.

```java
@Service
public class GameService {
}
```

Controller는 직접 게임 규칙을 처리하기보다 `GameService`를 호출한다.

### `@MessageMapping`

WebSocket/STOMP에서 클라이언트 메시지를 받을 주소를 지정한다.

```java
@MessageMapping("/games/{roomCode}/chat")
```

클라이언트가:

```text
/app/games/ABC123/chat
```

으로 메시지를 보내면 해당 메서드가 실행된다.

### `@DestinationVariable`

WebSocket 주소 안에 들어있는 값을 메서드 변수로 받는다.

```text
/games/ABC123/chat
        ↓
roomCode = "ABC123"
```

### `@PathVariable`

REST URL 경로 안의 값을 받는다.

### `@Configuration`

Spring 설정 클래스임을 나타낸다.

### `@EnableWebSocketMessageBroker`

Spring에서 STOMP 기반 WebSocket 메시지 기능을 활성화한다.

---

## 5. WebSocket / STOMP 연결 구조

WebSocket 설정에서:

```text
/app   → 클라이언트가 서버로 보낼 때
/topic → 서버가 여러 사용자에게 broadcast할 때
```

사용했다.

예:

```text
클라이언트
/app/games/ABC/chat
        ↓
GameSocketController
        ↓
/topic/games/ABC
        ↓
방 참가자 전원
```

사용한 주요 채널:

```text
/app/games/{roomCode}/chat
/app/games/{roomCode}/start
/app/games/{roomCode}/draw
/app/games/{roomCode}/clear

/topic/games/{roomCode}
/topic/games/{roomCode}/state
/topic/games/{roomCode}/draw
/topic/games/{roomCode}/clear
```

---

## 6. JWT 로그인 정보와 게임 연결

초기 구현에서는 브라우저가 직접 username을 전송했다.

```json
{
  "username": "사용자",
  "message": "정답"
}
```

이 방식은 사용자가 값을 바꾸면 다른 사용자처럼 요청할 수 있다는 문제가 있다.

그래서 최종적으로:

```text
HTTP 요청
 → Authentication.getName()

WebSocket 요청
 → Principal.getName()
```

으로 바꿨다.

```text
JWT 쿠키
  ↓
Spring Security
  ↓
Authentication / Principal
  ↓
실제 로그인 사용자
  ↓
게임 권한 검사
```

적용한 기능:

```text
방 생성      → Authentication
방 참가      → Authentication
제시어 조회   → Authentication

채팅          → Principal
게임 시작      → Principal
그림 전송      → Principal
전체 지우기    → Principal
```

---

## 7. 제시어 보안

게임 상태를 조회할 때 모든 사용자에게 정답이 전달되지 않도록 `GameRoomResponse`에서 answer를 제외했다.

제시어 조회는 별도 API로 처리한다.

```text
GET /api/games/rooms/{roomCode}/answer
        ↓
Authentication
        ↓
현재 로그인 사용자 확인
        ↓
현재 drawer와 같은가?
   ├─ YES → 제시어 반환
   └─ NO  → 제시어 비공개
```

따라서 출제자는 제시어를 보고, 다른 참가자는 `???`를 보게 된다.

---

## 8. 게임 진행 로직

게임 시작 시:

```text
방장 검사
 ↓
최소 인원 검사
 ↓
started = true
 ↓
round = 1
 ↓
첫 번째 참가자를 drawer로 지정
 ↓
랜덤 제시어 지정
```

정답 채팅이 들어오면:

```text
채팅 입력
 ↓
GameService.submitGuess()
 ↓
현재 answer와 비교
 ↓
정답
 ↓
+100점
 ↓
round 증가
 ↓
다음 참가자를 drawer로 선택
 ↓
새 제시어 선택
 ↓
게임 상태 broadcast
```

---

## 9. Canvas 그림 실시간 동기화

브라우저 Canvas에서 마우스로 그림을 그리면 선의 좌표를 WebSocket으로 전송한다.

```text
마우스 이동
 ↓
(x1, y1) → (x2, y2)
 ↓
sendDraw()
 ↓
WebSocket
 ↓
GameSocketController
 ↓
현재 사용자가 drawer인지 확인
 ↓
/topic/.../draw broadcast
 ↓
모든 브라우저 Canvas에 동일하게 그림
```

서버에서도 drawer 여부를 검사하므로 일반 참가자는 임의로 그림 데이터를 보내도 적용되지 않는다.

---

## 10. 지우개 기능

그림 메시지에 `mode`를 추가했다.

```text
pen
eraser
```

Canvas에서는:

```javascript
ctx.globalCompositeOperation = "destination-out";
```

을 사용해 기존 그림의 픽셀을 지운다.

```text
펜
 → source-over
 → 선 그리기

지우개
 → destination-out
 → 기존 픽셀 삭제
```

전체 지우기도 WebSocket으로 broadcast되어 모든 참가자의 Canvas가 동시에 지워진다.

---

## 11. 외부 사용자 접속 — ngrok

로컬 서버는 기본적으로:

```text
localhost:9090
```

이므로 다른 컴퓨터에서 직접 접속할 수 없다.

`ngrok`을 사용해 임시 공개 주소를 만들었다.

```bash
ngrok http 9090
```

구조:

```text
친구 브라우저
    ↓
https://xxxxx.ngrok-free.dev
    ↓
ngrok
    ↓
내 PC의 localhost:9090
    ↓
Spring Boot
```

---

## 12. 외부 WebSocket 연결 문제와 해결

처음 WebSocket 주소가:

```javascript
ws://localhost:9090/ws
```

로 고정되어 있었다.

이 경우 친구 컴퓨터에서는 `localhost`가 친구 자신의 컴퓨터를 의미하므로 연결할 수 없다.

그래서 현재 접속 주소를 기준으로 자동 생성하도록 변경했다.

```javascript
const wsProtocol = window.location.protocol === "https:" ? "wss" : "ws";

const wsUrl = `${wsProtocol}://${window.location.host}/ws`;
```

결과:

```text
로컬 접속
http://localhost:9090
→ ws://localhost:9090/ws

ngrok 접속
https://xxxxx.ngrok-free.dev
→ wss://xxxxx.ngrok-free.dev/ws
```

이후 외부 사용자도 실시간 채팅과 그림 기능을 사용할 수 있게 됐다.

---

## 13. 테스트하면서 확인한 중요 포인트

같은 브라우저 일반 탭에서 서로 다른 계정으로 로그인하면 JWT 쿠키가 공유된다.

```text
탭1 → 사용자 A 로그인

탭2 → 사용자 B 로그인
       ↓
같은 브라우저 쿠키가 B의 JWT로 변경
       ↓
탭1의 다음 요청도 사용자 B로 인증될 수 있음
```

멀티 사용자 테스트는 다음처럼 하는 것이 안전하다.

```text
일반 Chrome → 사용자1
시크릿 Chrome → 사용자2
```

또는 서로 다른 브라우저를 사용한다.

---

## 14. 현재 게임 기능 정리

```text
로그인 사용자 연동          ✅
방 생성                     ✅
방 참가                     ✅
방 나가기                   ✅
최대 6명                    ✅
방장                         ✅
방장만 게임 시작             ✅
실시간 채팅                  ✅
랜덤 제시어                  ✅
drawer에게만 제시어 공개      ✅
정답 자동 판정               ✅
정답 +100점                  ✅
라운드 증가                  ✅
drawer 순환                  ✅
실시간 Canvas 그림           ✅
drawer만 그림 가능            ✅
지우개                       ✅
전체 지우기                  ✅
라운드 변경 시 Canvas 초기화  ✅
JWT 기반 사용자 확인          ✅
ngrok 외부 접속               ✅
외부 WebSocket 연결           ✅
```

---

## 15. 오늘 구현의 핵심

오늘 구현에서 가장 중요한 것은 단순히 게임 기능을 만든 것이 아니라,

```text
기존 로그인/JWT
      ↓
Spring Security
      ↓
REST + WebSocket
      ↓
실시간 게임
```

을 하나의 Spring Boot 애플리케이션 안에서 연결해 본 것이다.

특히 REST의 `Authentication`과 WebSocket의 `Principal`을 이용해 **로그인 사용자 정보를 게임 권한과 연결**했고, WebSocket/STOMP를 이용해 **채팅·게임 상태·Canvas 그림을 여러 브라우저에 실시간 동기화**했다.

최종적으로 `ngrok`을 통해 로컬 개발 서버를 외부에 공개하면서 실제 다른 사용자가 접속 가능한 형태까지 테스트했다.
