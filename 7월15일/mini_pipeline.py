import httpx
import pandas as pd
from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    id : int
    title : str
    price : float

rows = [] 
for i in range(1,4): # 검증을 통과한 데이터만 담을 목록
    r = httpx.get(f"https://fakestoreapi.com/products/{i}", timeout=10)  # API 호출
    try:
        p = Product(**r.json()) #JSON을 스키마에 통과시켜 검증
        rows.append({"번호": p.id, "제품명": p.title, "가격": p.price})   # 통과분만 적재
    except ValidationError:
        print(i, "번 상품 검증 실패 - 건너뜀") #형태가 어긋난 데이터는 프로그램 멈추지 말고 기록만 남김

df = pd.DataFrame(rows)                   # 검증 통과분으로 표 생성
df.to_csv("products.csv", index=False)    # 사람이 열어 보기 좋은 CSV 로 저장
df.to_parquet("products.parquet")         # 분석용으로 빠른 parquet 으로도 저장
print("수집→검증→저장 완료:", len(df), "건")   # 파이프라인 결과 한 줄 요약

'''
row에 [{"번호": p.id, "제품명": p.title, "가격": p.price} ,{ ~~~ }] 이런식으로 연결되고, 
이걸 pd.DataFarme을 이용하면 알아서 표형태로 저장 하는거야? 저 키 값이 자동으로 열로 가는거임?

ㅇㅇ
딕셔너리 하나 → 표의 한 행
딕셔너리의 키 → 열 이름
딕셔너리의 값 → 해당 행의 셀 값

없는자리는 NaN
'''