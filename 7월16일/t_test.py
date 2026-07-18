from scipy import stats # 통계 검정 함수가 모인 라이브러리
import seaborn as sns

df = sns.load_dataset('tips')

# 흡연 그룹과 비흡연 그룹의 '팁 금액'을 각각 뽑음
smoker = df[df['smoker'] == 'Yes']['tip']
nonsmoker = df[df['smoker'] == 'No']['tip']

print('흡연 평균:', round(smoker.mean(),2))
print('비흡연 평균', round(nonsmoker.mean(),2))

#독립 표본 t 검정 : 두 그룹 평균 차이가 '통계적으로 의미 있는가'를 따진다

t, p = stats.ttest_ind(smoker,nonsmoker)
print('p-value:', round(p,3))

# 판정 규칙: p < 0.05 면 '우연이라 보기 어렵다(의미 있는 차이)', 아니면 '차이가 있다고 보기 어렵다'
if p < 0.05:
    print('=> 두 그룹의 팁은 통계적으로 유의하게 다르다')
else:
    print('=> 평균은 달라 보여도 우연일 수 있어 단정할 수 없다')