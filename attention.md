## 1주

7/15

    제너레이터로 대용량 파일을 메모리 아끼며 처리하기

    dataclass로 데이터 레코드 깔끔하게 정의하기

    Pydantic으로 입력값 검증하기

    functools·파일 IO·pathlib·예외를 한 흐름으로

    pytest 로 정제 함수 테스트하고 Ruff 로 정리

    asyncio·httpx 로 여러 API를 동시에 수집

    Parquet으로 저장하고 필요한 열만 골라 읽기

    수집→검증→저장을 한 스크립트로 — 미니 데이터 파이프라인

    예상되는 문제점들 예외 처리 신경쓰기

    practice1: 매출 레코드 집계 — Counter·defaultdict·컴프리헨션

    TypedDict + mypy — dict 에 타입 계약을 새겨 실행 전에 오류 잡기

    ProcessPoolExecutor — CPU 무거운 전처리를 코어 수만큼 병렬로

    cProfile — 느린 함수를 느낌이 아니라 측정으로 찾기

    practice2 : safe_load_csv와 Pydantic SalesRecord 스키마, valid/errors 분리 저장과 재로딩 검증

    종합실습 1 지정 API — countries.dev 국가 정보 조회 (보완 안내)

        공공 데이터포털 등 무료 JSON API에서 asyncio·httpx로 데이터를 비동기 수집하고, Pydantic으로 스키마를 검증한 뒤 Parquet로 저장하는 스크립트를 작성해 제출한다.

        위 스크립트의 수집·변환 함수에 pytest 테스트를 최소 2개 붙이고, ruff로 정리한 뒤 requirements.txt와 함께 Git으로 커밋해 재현 가능한 형태로 만든다.

7/16

    DataFrame 만들고 열 선택하기, 조건으로 행 필터링하기, groupby로 그룹별 평균 내기

    Polars Lazy API

    Plotly Express 로 인터랙티브 차트 한 줄

    t-검정으로 두 그룹 차이가 우연인지 확인

    sklearn Pipeline 으로 전처리+모델을 한 덩어리로 저장

    업종별 매출 합계 상위 뽑고 막대그래프를 파일로 저장하기

    ColumnTransformer — 숫자 열과 글자 열을 각각 다르게 전처리해 결합

    실습3: IQR 이상치 제거 후 named aggregation 집계 (Practice 3)

    실습3: DuckDB로 DataFrame에 바로 SQL 집계 (Practice 3)

    실습4: 카이제곱 검정 — 두 범주형 변수의 독립성 (Practice 4)

    pivot_table 과 merge — 엑셀 피벗과 SQL JOIN 을 Pandas 로

    Pandas 2.x Copy-on-Write — 걸러낸 조각을 고칠 때의 함정

    apply 대신 벡터화 — str·dt 접근자로 열 전체를 한 번에

    schedule 로 매일 아침 리포트 자동 실행 — 반복 분석 자동화

## 2주

7/20

    DBeaver 이용법.

    표를 키로 연결해 정합성 보장.

    SQL 질의 -> 파서 -> 옵티마이저 -> 실행기 -> 저장 엔진

    NULL값 잘 대응하기

    ERD

    PK, 후보키, 대리키, 왜래식별자, 자연키

    키와 무결성 제약조건

    정규화 = 하나의 사실을 한 곳에만 저장하도록 함수 종속 기준으로 표를 나누는 작업 : 1NF, 2NF, 3NF

    반정규화 - 너무 정규화 하면 속도 느려질수 있음, 병목이 확인된 곳만 선택적으로 반정규화

    좋은 데이터 모델 체크리스트

        모든 엔티티에 PK가 있다, 속성이 원자값, 하나의 사실은 한곳(원본1개->나머지 참조), 관계,선택성 명확, 명명규칙 명확, FK로 참조 무결성 보장

        계산 가능한건 컴럼으로 만들지 않기

7/21

    join 방식들


    옵티마이저 : nested loop join , hash join, sort merge join


    상관 서브 쿼리의 비용과 완화

    바깥 N행 -> 서브쿼리 최대 N회 실행, 바깥이 클수록 비용이 선형증가

    완화
    1 표준 형태로 작성해 Unnesting 유도
    2 서브쿼리 조인 컬럼에 인덱스 제공
    3 집계 후 조인(인라인 뷰·CTE)으로 재작성
    4 결측 처리는 NOT EXISTS

    피하기
    select 절의 무거운 상관 스칼라 반복
    Not in + null 가능 목록
    불필요하게 깊은 중첩
    측정 없는 추측성 재작성

    CTE

    집계 함수 : count(*), count(col), count(distinct), sum-avg, max-min : null 취급 잘 알기

    윈도우 함수

    다중 그룹핑 -> 주의: 이 경우는 실행순서에서 별칭 사용이 가능?, select의 비집계 컬럼은 모두 group by에 있어야함

    집계 함수 문제 -> 윈도우 함수

    트래잭션 : 원자성 일관성 고립성 지속성

        동시성 제어 : MVCC, 락, 데드락, 격리

7/22

    B+tree 구조

    삽입과 노드 분할

    인덱스 트레이드 오프 : 읽기는 빨라지지만 데이터 변경 시 인덱스도 갱신 -> 쓰기느려짐 + 공간추가

    클러스터형 인덱스, 비클러스터형

    복합 인덱스 : 순서가 중요 (=조건을 앞, 범위 조건 뒤)(=을 뒤에달면 풀스캔 위험!)

    covering index

    선택도와 인덱스 효율

    explain-> analyze -> 트리 읽기(노드 안->밖), 병목 찾기(가장 큰 노드)

    buffers 진짜 i/o비용

    스캔 방식 선택 기준 : 인덱스 온리, 인덱스스캔, bitmap scan, seq scan ->>옵티마이저가 정함

    조인 방식 : nested loop, hash join, merge join
    참고 : 디스크 스필

    병목 진단 : 풀스캔?, 예상vs실제 row검사, 정렬-해시가 디스크로 넘침?(work메모리 부족->조정-인덱스정렬), 많이 읽고 나중에 버림?(필터를 일찍->조건-조인 순서), 조인 방식이 적절한가(행추정 오류 -> 통계,인덱스)

    쿼리 리라이팅 : SARgable 조건, 필요한 컬럼,행만(명시잘하기)(일찎필터), 적절한 스캔 유도, 불필요 연산 제거(습관적 distinct, order by, 영향없는 서브쿼리,   union(중복이 없는데 사용)), 집합적 사고

        참고 : 조건을 갈래로 나눠 UNION 으로 합치면 갈래마다 자신의 인덱스(a용·b용)를 탈 수 있다.

        느린 상관서브쿼리(조인,집계 후 처리), not in (null 위험), 깊은 중첩 서브쿼리(CTE단계화), 스칼라 서브쿼리 반복(조인으로 한번에)

        핵심 코드에 반복문(for/while)으로 쿼리를 반복 호출하는 게 보이면 “집합으로 바꿀 수 있나 확인

        페이지네이션 : 오프셋 vs 키셋

        집계 튜닝 - 미리 계산하기 (materialized view로 캐시)

        정렬 튜닝 - 인덱스로 정렬 생략(drder by 컬럼에 인덱스->정렬 생략), 상위 n, 복합 정렬은 인덱스 순서-방향일치, work_men 초과 시 디스크 정렬

        N+1 제거 : 왕복 줄이기 -> 한번의 조인으로 일괄 조회, in으로 묶어 조회(바인딩도), orm은 eager loading/명시적 조인

        파티셔닝 : 큰 테이블을 쪼개기 (인덱스로 부족한 초대용량,시계열의 마지막 카드)

7/23

    요청/응답, 렌더링, 역할 분담, 개발환경

    HTML

    파싱, 렌더 트리, 레이 아웃, 페인트

    HTML(구조) -> CSS(표현) -> JavaScript(동작)

    DTD(문서형 정의) -> 문서의 시작과 끝 -> 문서 정보(메타데이터) -> (브라우저에 표시할 내용)

    태그, 요소(태그 + 내용), 속성(여는 태그 안에 이름=값 형태로 추가 정보 지정)(id, class, style lang, hidden)

    시맨틱 태그 : 문서의 구조와 의미를 명확히 나타내는 HTML5 태그: 가독성(코드 구조가 명확), 접근성(화면 낭독기가 콘탠츠가 콘텐츠 구조를 더 잘 이해한다), SEO(검색 엔진이 주요 정보를 효율적으로 파악)

    css

7/24
