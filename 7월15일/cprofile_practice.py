import cProfile  #함수별 호출 횟수 누적 시간을 재는 표준 도구

def load_data():
    return list(range(200_000))

def slow_clean(data): # 일부러 느리게 만든 정제 함수 
    out = []
    for x in data:
        out.append(str(x).zfill(8))

    return out

def summarize(data): # 요약 통계
    return sum(len(s) for s in data)

def analysis(): # 전체를 하나로 묶음
    data = load_data() # 읽고
    cleaned = slow_clean(data) # 정제하고
    return summarize(cleaned) # 요약

# cumtime(누적시간) 순으로 정렬해 어느 함수가 오래 걸렸는지 표적
cProfile.run('analysis()', sort= 'cumtime')