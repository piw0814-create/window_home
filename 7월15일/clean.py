# clean.py - 테스트 대상이 되는 정제 함수
def clean_price(price):
    """0이하 값을 걸러내고 정상 금액만 돌려준다."""
    return [p for p in price if p is not None and p > 0]  # None과 0이하 값은 제거
