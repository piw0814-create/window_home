import plotly.express as px #인터랙티브 차트를 한 줄로 그려주는 라이브러리

df = px.data.tips() 

#산점도
#마우스를 올리면 값이 뜨고, 드래그로 확대,축소가 되는 차트

fig = px.scatter(
    df, x='total_bill', y='tip',
    color='smoker',           # 범주별로 색을 나눈다
    size='size',              # 점 크기 = 일행 인원 수
    title='결제액 대비 팁 (인터랙티브)'
)

fig.write_html('tip_scatter.html') #HTML로 저장하면 브라우저에서 만져 볼 수 있다
# 주피터에서는 fig.show()로 바로 확인
print('차트 저장 완')