from pydantic import BaseModel, Field, ValidationError


# 가격은 0보다 커야 한다는 규칙(gt= 0)을 스키마에 새긴다
class OrderIn(BaseModel):
    name: str
    price: int = Field(gt=0)


# 올바른 입력은 통과하고 model_dump()로 dict 변환할 수 있다
ok = OrderIn(name="사과", price=1000)
print(ok.model_dump())  # 결과 : {'name': '사과', 'price': 1000}

# 규칙을 어기면(음수 가격) ValidationError 발생
try:
    OrderIn(name="사과", price=-1)
except ValidationError as e:
    print(
        "검증 실패:", e.errors()[0]["msg"]
    )  # e.errors() : 어떤 필드가 어떤 규칙을 어겼는지 알려줌
