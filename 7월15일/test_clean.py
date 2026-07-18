# test_clean.py - pytest가 자동으로 찾아 실행하는 테스트 파일
# (파일명 test_로 시작, 함수명도 test_로 시작해야 pytest가 자동으로 찾아 실행한다.)
from clean import clean_price


def test_음수와_None_제거():
    """음수와 None을 제거하고 정상 금액만 남기는지 테스트"""
    # given : 정상값 2개 + 잘못된 값 3개
    result = clean_price([12000, -1, None, 0, 8000])
    # then : 정상값 2개만 남았는지 확인
    assert result == [12000, 8000]


def test_빈_목록은_빈_목록을_반환():
    """빈 목록을 넣으면 빈 목록을 반환하는지 테스트"""
    assert clean_price([]) == []


"""
궁금한점
assert로 검증을 하게되면, 예상하지 설정하지 못한 조합이 들어왔을 떄 오류나오지 않나?
경우의 수가 많아지면 assert로 검증하는게 한계가 있지 않나?

필요한 경우, 중요한 경우를 골라 검증
Hypothesis 같은 도구도 있음

테스트는 완벽함을 증명하는 도구라기보다
미리 생각한 오류와 회귀 버그를 빠르게 발견하는 안전망
"""
