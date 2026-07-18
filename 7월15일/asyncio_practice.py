import asyncio # 비동기 실행을 관리하는 표준 라이브러리
import httpx # async 를 지원하는 최신 HTTP 클라이언트

# 한 개의 주소를 비동기로 받아오는 코루틴(async 함수)

async def fetch(client, url) :
    r = await client.get(url) #await : 응답을 기다리는 동안 다른 일을 양보
    return r.status_code  # 상태코드만 돌려준다(200 이면 성공)

async def main():
    urls = [f'https://httpbin.org/delay/1' for _ in range(5)]
    async with httpx.AsyncClient(timeout=30) as client:
        # gather : 5개 요청을 순서대로가 아니라 동시에 띄운다
        results = await asyncio.gather(*[fetch(client, u) for u in urls])

    print("응답 코드들 : ", results)

#순서대로면 5초, 동시 처리면 약 1초
asyncio.run(main())