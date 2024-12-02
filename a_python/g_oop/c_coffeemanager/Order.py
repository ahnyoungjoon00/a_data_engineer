from datetime import datetime
from Coffee import Coffee
from OrderStatus import OrderStatus

class Order:
    def __init__(self, coffee:Coffee, cnt):
        self.__coffee = coffee # 주문한 커피
        self.__cnt = cnt
        self.__regist_time = datetime.now() # 주문등록시간
        self.__order_price = coffee.price * cnt
        self.__order_info = f'{coffee.name}[{cnt}잔]'
        self._order_status = OrderStatus.check_order_status(self)

        # if(cnt > coffee.stock):
        #     self.__cnt = 0 # 주문이 불가능한 상황이면 주문수량을 0으로 변경
    @property
    def order_status(self):
        return self._order_status

    def execute(self):
        self.coffee.offer(self.cnt)

    @property
    def coffee(self):
        return self.__coffee

    @property
    def cnt(self):
        return self.__cnt

    @property
    def regist_time(self):
        return self.__regist_time

    @property
    def order_price(self):
        return self.__order_price

    @property
    def order_info(self):
        return self.__order_info

        
        

