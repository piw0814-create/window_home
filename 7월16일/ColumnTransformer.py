import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer # 열 종류별로 다른 처리 적용
from sklearn.impute import SimpleImputer #결측치 채우기
from sklearn.preprocessing import StandardScaler, OneHotEncoder #표준화, 원핫
from sklearn.linear_model import LinearRegression # 회귀모델

# 수치형 열 전용 : 빈칸은 중앙값으로 채우고 -> 크기를 표준화
num_pipe = Pipeline(
    [
        ("결측", SimpleImputer(strategy=('median'))),
        ('스케일', StandardScaler())
    ]
)
# 범주형 열 전용 : 빈칸은 'missing'글자로 채우고 -> 원핫인코딩(0/1 표로 변환)
cat_pipe = Pipeline([
    ('결측', SimpleImputer(strategy='constant', fill_value='missing')),
    ('원핫', OneHotEncoder(handle_unknown='ignore'))
])

# 두 파이프라인을 '열 이름 기준'으로 하나로 결합
pre = ColumnTransformer([
    ('수치' , num_pipe, ['연령대_10', '연령대_20', '연령대_30']), #숫자 열 3개는 이쪽
    ('범주', cat_pipe, ['상권_구분']), #글자열 1 개는 저쪾
])

# 전처리 + 모델
model = Pipeline([
    ('전처리', pre),
    ('회귀', LinearRegression()),
])

X = pd.DataFrame({"연령대_10": [20, None, 15], "연령대_20": [180, 140, 150],
                  "연령대_30": [260, 80, None], "상권_구분": ["골목", None, "발달"]})

y = [820, 310, 640]  # 정답 당월 매출

model.fit(X,y)
print('예측 : ', model.predict(X).round(1))