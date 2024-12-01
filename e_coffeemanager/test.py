def main() :
    """
    음료 판매 관리 프로그램
    """
    # 데이터
    # name_lst = ["아메리카노", "모카", "라떼"]
    # price_lst = [3000, 4000, 5000]
    # stack_list = [10, 10, 10]

    sales_price = 0 

    americano = {"name" : "아메리카노", "price" : 3000, "stack" : 10}
    moca = {"name" : "모카", "price" : 4000, "stack" : 10}
    latte = {"name" : "라떼", "price" : 5000, "stack" : 10}
    drinks = [americano, moca, latte]

    while(True) :
        print("\n==========Index==========")
        print("음료판매(1) : ")
        print("현황(2) : ")
        print("종료(3) : ")
        menu = int(input("입력 : "))

        if (menu == 1) :
            print("===========Menu==========")
            for i in range(len(drinks)) :
                print(f"{drinks[i]["name"]}({i})")


            drink = int(input("\n * 음료코드 : "))
            if drink not in range(len(drinks)) :
                print("유효하지 않은 음료코드입니다.")
                continue
            order_cnt = int(input(" * 주문량 : "))
            if (drinks[drink]["stack"] < order_cnt) :
                print("재고가 없습니다.")
                continue
            print()
            drinks[drink]["stack"] -= order_cnt
            sales_price += drinks[drink]["price"]*order_cnt

            print(f"제품명 : {drinks[drink]["name"]}")
            print(f"판매가 : {drinks[drink]["price"]}")
            print(f"판매수량 : {order_cnt}")
            print(f"결제금액 : {drinks[drink]["price"]*order_cnt}")
            print(f"재고 : {drinks[drink]["stack"]}")


        elif (menu == 2) :
            print("==========Status==========")
            for i in range(len(drinks)) :
                print(f"{drinks[i]["name"]} | 재고 : {drinks[i]["stack"]}")

            print(f"\n매출 : {sales_price}")

        elif (menu == 3) :
            print("종료합니다.")
            break
        
        else :
            print("잘못된 입력입니다.")
            continue
main()