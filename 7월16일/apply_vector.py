import pandas as pd

df = pd.DataFrame({
    'name': ['kim', 'lee', 'park'] * 1000,                        # 고객명 3000건
    'date': ['2026-01-05', '2026-02-14', '2026-03-01'] * 1000,    # 주문일 3000건
})

# 느린 방법 apply
df['upper1']= df['name'].apply(lambda x: x.upper())

# 빠른 방법 str 접근자, c레벨에서 열 전체를 한 번에 처리(벡터화)
df['upper2'] = df['name'].str.upper()

# 날짜도 마찬가지
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
df['weekday'] = df['date'].dt.day_nanme() 

print(df[['name', 'upper2', 'month', 'weekday']].head(3))

# 습관: apply 를 쓰기 전에 'str/dt/산술 벡터 연산으로 되는가'를 먼저 묻는다