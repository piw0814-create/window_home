import pandas as pd

# 매출 표: 고객·지역·분류별 거래 기록
sales = pd.DataFrame({
    'customer_id': [1, 2, 1, 3],                    # 고객 번호
    'region': ['서울', '부산', '서울', '부산'],       # 지역
    'category': ['가전', '식품', '식품', '가전'],     # 상품 분류
    'amount': [1200, 300, 500, 2000],               # 매출액
})

# 고객 표
cust = pd.DataFrame({'customer_id': [1,2,3], 'grade' : ['VIP', '일반', '일반']})

# 1. pivot_tabel 

pivot = sales.pivot_table(values = 'amount', 
                          index= 'region',
                          columns='category',
                          aggfunc= 'sum',
                          fill_value=0
                          )

print(pivot)

# 2 merge 고객 등급을 매출 표에 붙인다

joined = pd.merge(sales, cust, on='customer_id', how= 'left')
print(joined[['customer_id', 'amount', 'grade']])


# 3 결합햇으니 등급별 매출 합계도 한줄

print(joined.groupby('grade')['amount'].sum())