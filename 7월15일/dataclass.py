from dataclasses import dataclass # 반복되는 __init__을 자동으로 만들어줌

@dataclass
class Order:
    name : str
    qty: int
    price:int

order = Order('사과', 3, 1000) # 생성자를 직접 안써도 필드 순서로 만듬
print(order.name)
print(order)

"""
기존 방식

class Order:
    def __init__(self, name: str, qty: int, price: int):
        self.name = name
        self.qty = qty
        self.price = price

order = Order("사과", 3, 1000)

print(order.name)
print(order)

"""
