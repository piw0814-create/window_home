import polars as pl #pandas보다 빠른 최신 데이터프레임 라이브러리

# scan_csv: 파일을 지금 읽지 않고 읽을 계획만 세운다

lazy = pl.scan_csv('sales_100k.csv')

# filter,group_by,agg 를 이어 붙여도 아직 실행되지 않는다 - 계획만 쌓인다

plan = (
    lazy
    .filter(pl.col('amount')>0) # 정상금액만
    .group_by('region') # 지역별로 묶어
    .agg(pl.col('amount').mean().alias('avg')) #평균 매출 계산
)

# collect()를 부르는 순간, polars가 쌓인 계획을 최적화 해서 한 번에 실행
result = plan.collect()
print(result) 