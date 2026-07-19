from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler #스케일 맞추기(전처리)
from sklearn.linear_model import LogisticRegression # 분류 모델
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split #전체 데이터를 학습용과 테스트용으로 나누기
import joblib # 학습된 파이프라인을 파일로 저장/불러오기

X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X,y, test_size=0.2, random_state=0)

# 전처리(스케일러)와 모델을 한 줄로 묶는다 - 학습,예측에 '같은 처리'가 보장
# Pipeline에는 다음처럼 (단계 이름, 실행 객체) 튜플들을 리스트로 전달.

pipe = Pipeline([
    ('scaler', StandardScaler()), # 1단계 : 값의 크기를 표준화
    ('model', LogisticRegression(max_iter=200)), # 2단계 : 모델 학습
])

pipe.fit(X_tr, y_tr)
print("정확도 : ", round(pipe.score(X_te,y_te),3))

# 파이프 라인을 통째로 저장하면, 나중에 불러와 바로 예측 할 수 있다(재현성 확보)
joblib.dump(pipe, 'model.joblib')
loaded = joblib.load('model.joblib')

print('불러온 모델 예측 : ', loaded.predict(X_te[:3]))
print("정확도:", round(loaded.score(X_te[:3], y_te[:3]), 3))