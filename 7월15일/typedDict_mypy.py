from typing import TypedDict #dict 모양에 타입 힌트를 입히는 도구

# dict를 그대로 쓰되, 어떤 키에 어떤 타입이 오는지 계약을 선언

class SalesRow(TypedDict) : 
    date : str
    region : str
    amount : float

# CSV 한 행을 읽었다고 가정 - 겉모습은 평범한 dict 다

row : SalesRow = {'date' : '2026-01', 'region' : '서울', 'amount' : 1500.0}
print(row['region'])

# 타입 힌트가 있으면 정적 검사기가 실수를 실행 전에 잡아준다
def compute_avg(values : list[float]) -> float:
    return sum(values) / len(values) # 평균 계산


compute_avg(['a', 'b'])  #<- 문자열 리스트를 넘기는 실수(주석 해제해 실험)
# 터미널에서:  mypy typedDict_mypy.py
#   error: Argument 1 has incompatible type 'list[str]'; expected 'list[float]'
# 수백만 행을 처리한 뒤 터지는 것보다, 실행 전에 빨간 줄로 아는 편이 훨씬 싸다