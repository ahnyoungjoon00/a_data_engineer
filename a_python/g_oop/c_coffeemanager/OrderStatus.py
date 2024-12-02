from enum import Enum

"""
Enum : 연관된 상수들의 집합
"""
class OrderStatus(Enum):
    # OrderStatus의 인스턴스
    # Enum은 클래스 내에서 정의한 인스턴스 외에는 인스턴스를 생성할 수 없다.
    OK = (0, '주문생성성공')
    FAIL_SOLDOUT = (1, '품절로 인한 주문실패')
    FAIL_STOCK = (2, '재고부족으로 인한 주문실패')
    COMPLETE = (3, '주문 완료')

    def __init__(self, code, desc):
        self.code = code
        self.desc = desc
    
    # 타입정보로 사용할 수 있는 메서드
    # classmethod : 클래스의 맥락(클래스변수를 수정, 클래스인스턴스를 생성)과 관련되었을 경우 사용
    # staticmethod : 클래스 맥락과 독립적으로, 클래스를 돕기 위한 유틸에 가까울때 사용
    @staticmethod
    def check_order_status(order):
        coffee = order.coffee
        cnt = order.cnt

        if(coffee.stock < cnt):
            return OrderStatus.FAIL_SOLDOUT
        else:
            return OrderStatus.OK
        