from concurrent.futures import ProcessPoolExecutor #여러 프로세스로 나눠 실행
import multiprocessing as mp # 내 컴퓨터의 CPU 코어 수 확인용

#CPU 를 많이 쓰는 무거운 계산(행 단위 전처리라고 가정)
def process_chunk(chunk):
    return [x * x % 97 for x in chunk] # 청크 안의 값을 하나씩 변환

def split_chunks(data, n): # 데이터를 코어 수 만큼 등분하는 함수
    size = len(data) //n # 청크 하나의 크기
    return [data[i*size:(i+1)*size] for i in range(n)] #n개 조각으로 분할

if __name__== '__main__': # 멀티 프로세싱은 이 가드가 반드시 필요하다
    data = list(range(1_000_000)) # 처리할 큰 데이터(100만 건)
    n_cores = mp.cpu_count() # cpu 코어 수
    chunks = split_chunks(data, n_cores)

    with ProcessPoolExecutor(max_workers=n_cores) as exe: # 코어 수 만큼 청크 분할
        result = list(exe.map(process_chunk, chunks))

    total = sum(len(r) for r in result) # 조각난 결과를 다시 합친다
    print(n_cores, '코어로', total, '건 병렬 처리 완료')
