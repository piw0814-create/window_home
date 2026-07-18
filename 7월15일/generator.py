# 파일을 한 줄씩 흘려보내는 제너레이터
def read_lines(path):
    with open(path, encoding="utf-8") as f:
        for line in f:  # 파일 객체는 한 줄씩 순회할 수 있다
            yield line  # return이 아니라 yield: 한줄을 내주고 멈췄다 재개


# sum 이 제너레이터에서 한 줄 씩 받아 길이를 더한다(리스트로 전부 읽지 않음)
total = sum(len(l) for l in read_lines("big.log"))

print("정체 글자 수 : ", total)  # 수 gb 로그도 적은 메모리로 처리 가능


"""궁금했던 부분
텍스트 파일 객체 f는 for line in f로 반복하면 기본적으로 한 줄씩 읽어 온다.

한 줄씩 처리: for line in f
파일 전체를 문자열로 읽기: f.read()
모든 줄을 리스트로 읽기: f.readlines()
여러 줄을 하나로 합치기: "".join(...)

즉, 기본 반복은 줄 단위이고, 전체가 필요하면 별도 명령을 사용한다.

파일 객체 f 에 반복문으로 불러올시 한줄씩 불러온다는 내용이 내장되어 있다. 그래서 제너레이터를 만들 때도 for line in f로 한 줄씩 읽어 yield로 내보내면 된다."""
