from Order import Order
from Account import Account

class Payment:
    def __init__(self, order:Order):
        self.__order = order
        self.__pay_price = order.order_price
    
    def execute(self):
        account = Account.get_instance()
        account.regist_sales(self.pay_price)

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value

    @property
    def pay_price(self):
        return self.__pay_price

    @pay_price.setter
    def pay_price(self, value):
        self.__pay_price = value


