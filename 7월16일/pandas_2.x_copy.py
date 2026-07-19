import pandas as pd

df = pd.DataFrame({'region': ['서울', '부산', '서울'],
                   'amount': [1000, 2000, 3000]})   # 원본 매출 표

# 위험 조건으로 걸러낸 조각 
seoul = df[df['region'] =='서울'] # >>>경고, 오류 발생

# 안전
seoul = df[df['region'] =='서울'].copy()

# 원본 자체를 고치기
df.loc[df['region']=='서울', 'amount'] *= 1.1