from Account import *
from Coffee import *
from Order import *
from Payment import *
from Sales import *

class Menu:
    def __init__(self, sales, drinks):
        self.account = Account()
        self.sales = sales
        self.drinks = drinks

    def main_menu(self):
        while True:
            print("\n=========Menu=========")
            print("판매등록(1)")
            print("현황(2)")
            print("종료(3)")
            input_menu = int(input("입력 : "))

            if input_menu == 1:
                self.coffee_menu()
            elif input_menu == 2:
                self.statistics()
            elif input_menu == 3:
                print(" * 종료합니다.")
                return
            else:
                print(" * 잘못된 번호를 입력하셨습니다.")

    def statistics(self):
        print("\n=========statistics========= ")
        for drink in self.drinks:
            print(
                f"{drink.name} | 재고 : {drink.stock} | 판매량 : {drink.total_sales_cnt}"
            )

        print(
            f"잔고 : {self.account.balance}| \
            매출 : {self.account.sales_volume} | \
            지출 : {self.account.expenses}"
        )

    def coffee_menu(self):
        print("\n=========List========= ")
        for drink in self.drinks:
            print(f"{drink.name} ({self.drinks.index(drink)})")

        input_code = int(input("\n * 판매한 커피코드 : "))
        order_cnt = int(input(" * 판매량 : "))

        if input_code < 0 or input_code >= len(self.drinks):
            print("정확한 상품번호를 선택해 주세요.")
            return

        order = self.register_order(input_code, order_cnt)
        if(not order): return
        payment = self.sales.take_order(order)
        print(f"""결제금액: {payment.pay_price}""")


    def register_order(self, input_code, order_cnt):
        order = Order(self.drinks[input_code], order_cnt)
        if(order.order_status != OrderStatus.OK):
            print(order.order_status.desc)
            return

        return order

    def order_result(self, payment):
        order = payment.get_order()
        print(f"\n 제품명 : {order.coffee.name}")
        print(f" 판매가 : {order.coffee().price}")
        print(f" 판매수량 : {order.cnt}")
        print(f" 결제금액 : {payment.pay_price}")
        print(f" 남은 재고 : {order.coffee.stock}")
