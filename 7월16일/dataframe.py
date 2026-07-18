import pandas as pd

df = pd.DataFrame({'이름' : [ 'A', 'B', 'C'], '점수': [90, 70, 85]})
print(df['점수'].mean())  # '점수' 열의 평균 → 결과: 81.666...

#조건으로 행 필터링
high = df[df['점수'] >= 80]
print (len(high))

#groupby로 그룹별 평균내기
df = pd.DataFrame({'반': ['1', '1', '2'], '점수': [90, 80, 70]})
# '반'으로 묶어 각 반의 평균 점수를 구한다
print (df.groupby('반')['점수'].mean()) # 결과: 1반 85.0, 2반 70.0