# 실습 1 : 매출 레코드를 자료구조로 집계하기
from collections import Counter, defaultdict #빈도, 집계 그룹핑 전용 자료구조

# Python_Practicel_Data.json 을 흉내 낸 Sales 레코드(행: 날짜 지역 금액 품목)

sales = [
    {'date': '2026-01', 'region': '서울', 'amount': 1500, 'category': '가전'},
    {'date': '2026-01', 'region': '부산', 'amount': 800,  'category': '의류'},
    {'date': '2026-02', 'region': '서울', 'amount': 1200, 'category': '가전'},
    {'date': '2026-02', 'region': '서울', 'amount': 300,  'category': '식품'},
    {'date': '2026-02', 'region': '부산', 'amount': 2000, 'category': '가전'},
]

# 1. amount >= 1000 인 거래만 남긴다.
big = [r for r in sales if r['amount'] >= 1000 ]

# 2. Counter로 지역별 거래 건수를 샌다
region_count = Counter(r['region'] for r in big)
print ('지역별 거래 건수 : ', region_count.most_common()) # 많은 순으로 정렬

# 3. defaultdict 로 카테고리별 금액 리스트를 모은다
by_cat = defaultdict(list) #defaultdict(list)는 없는 키를 처음 사용할 때 자동으로 빈 리스트를 만들어줘.
# 키 하나당 빈 리스트를 만듬 -> append로 그 리스트안에 값을 넣음 -> for로 다음 꺼 반복
for r in big:
    by_cat[r['category']].append(r['amount'])

# 4. 딕셔너리 컴플리헨션으로 지역별 총매출 dict 를 만든다
region_total = {reg: sum(r['amount'] for r in big if r['region']==reg) for reg in region_count}
print('지역별 총매출:', region_total)
"""
궁금했던부분
for reg in region_count가 가능한 이유는 딕셔너리나 Counter를 반복하면 기본적으로 키가 하나씩 나오기 때문이야.
"""

# 금액 상위 3건을 내림차순으로 정렬( 정렬 기준 key = 금액, reverse)
top3 = sorted(big, key= lambda r: r['amount'], reverse=True)[:3]
assert region_total['서울'] == 2700


"""
실습1 체크포인트 : 리스트 제너레이터 메모리 비교
"""
import sys # 객체가 차지하는 바이트를 재는 표준 모듈

# 1. 리스트 : 1000만 개 제곱값을 한꺼버넹 메모리에 올림
squres_list = [x * x for x in range(10_000_000)]

# 2. 제너레이터
squres_gen = (x * x for x in range(10_000_000))

print('리스트 : ', sys.getsizeof(squres_list), 'bytes')
print('제너레이터 : ', sys.getsizeof(squres_gen), 'bytes')

assert sys.getsizeof(squres_gen) < sys.getsizeof(squres_list)

# 3. 제너레이터는 한번만 흐름, 합을 구하면 소진
total = sum(squres_gen)
print ('합계 : ', total , '\w 다시 세면 : ', sum(squres_gen))