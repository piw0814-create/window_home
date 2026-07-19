import timeit
data_list = list(range(100_000))
data_set = set(data_list)

#리스트의 in 검사 : 앞에서부터 하나씩
t_list = timeit.timeit(lambda : 99_999 in data_list, number = 1000)
# 집합의 in 검사, 해시로 위치를 바로 찾는다 
t_set = timeit.timeit(lambda: 99_999 in data_set, number = 1000)

print('리스트 검색:', round(t_list, 4), '초')   # 집합보다 수백 배 느리다
print('집합 검색  :', round(t_set, 6), '초')    # 거의 0에 가깝다

#그러나 집합은 순서와 중복을 보존하지 않는다, 존재 여부를 자주 검사할때 집합이 유리.