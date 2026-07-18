from functools import reduce  # 목록을 하나의 값으로 '접는' 도구
from pathlib import Path  # OS에 상관없이 안전하게 경로를 다룬다
import json  # json 파일 읽고 쓰기

# 1. 여러 주문 금액을 map/filter/reduce로 한 줄씩 처리
prices = [12000, -1, 35000, 0, 8000]
valid = list(filter(lambda p: p > 0, prices))  # 0보다 큰 금액만 남긴다
with_tax = list(map(lambda p: int(p * 1.1), valid))  # 10% 세금 붙이기
total = reduce(lambda a, b: a + b, with_tax)
print("부가세 포함 총액 : ", total)

# 2. pathlib로 경로를 만들고 json 으로 저장
out = Path("data") / "summary.json"  # data/summary.json 경로 객체
out.parent.mkdir(exist_ok=True)  # data 폴더가 없으면 만들고, 있으면 그냥 넘어간다
out.write_text(
    json.dumps({"total": total}), ensure_ascii=False, encoding="utf-8"
)  # json 문자열로 변환 후 저장

# 3. 없을 수도 있는 파일을 예외 처리로 안전하게 읽는다
try:
    raw = Path("data/summary.json").read_text(encoding="utf-8")
    print("저장된 값:", json.loads(raw))  # json 문자열을 dict로 변환
except FileNotFoundError:
    print("파일이 없습니다")  # 터지지 않고 다음 진행

""" 
궁금했던거

    dump, dumps, load, loads 차이
    dump : dict -> json 파일로 저장
    dumps : dict -> json 문자열로 변환
    load : json 파일 -> dict로 변환
    loads : json 문자열 -> dict로 변환

write_text와 .dumps 조합과 open('파일명','w')와 .dump 조합의 차이

    write_text : 문자열을 파일로 저장
    dumps : dict를 문자열로 변환
    즉, write_text와 dumps를 조합하면 dict -> 문자열 -> 파일로 저장
    open('파일명','w') : 파일을 쓰기 모드로 열기
    dump : dict를 파일로 저장
    즉, open과 dump를 조합하면 dict -> 파일로 바로 저장

JSON 파일에 바로 저장·읽기
→ dump / load가 간단함

JSON 문자열 자체가 필요함
→ dumps / loads 사용

Path 객체로 파일을 간단히 다루고 싶음
→ dumps + write_text
→ read_text + loads
"""
