from Purchase import Purchase

class Coffee:
    def __init__(self, name, stock, total_sales_cnt, safety_stock, cost, price):
        self.__name = name
        self.__stock = stock
        self.__total_sales_cnt = total_sales_cnt # 누적판매량
        self.__safety_stock = safety_stock # 안전재고
        self.__cost = cost # 원가
        self.__price = price # 판매가
    
    def offer(self, cnt):
        self.__deduct_stock(cnt) # 재고 차감
        self.__add_total_sales_cnt(cnt) # 누적 판매량 추가

        if(self.stock < self.safety_stock): #재고가 안전재고 미만이라면
            self.__add_safety_stock() # 안전재고 확보

    def add_stock(self, cnt):
        self.__stock += cnt
    
    def __deduct_stock(self, cnt):
        self.__stock -= cnt
    
    def __add_total_sales_cnt(self, cnt):
        self.__total_sales_cnt += cnt

    def __add_safety_stock(self):
        print('[system:log] 재고가 부족해 안전재고를 확보합니다.')
        purchase = Purchase(self, self.safety_stock * 2)
        if(purchase.execute()):
            print('[system:log] 안전재고 확보에 성공했습니다.')
            return
        print('[system:log] 안전재고 확보에 실패했습니다.')


    @property
    def name(self):
        return self.__name

    @property
    def stock(self):
        return self.__stock

    @property
    def total_sales_cnt(self):
        return self.__total_sales_cnt

    @property
    def safety_stock(self):
        return self.__safety_stock

    @property
    def cost(self):
        return self.__cost

    @property
    def price(self):
        return self.__price

