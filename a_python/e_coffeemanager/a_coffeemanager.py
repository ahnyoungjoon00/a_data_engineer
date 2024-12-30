def main() :
    """
    음료 판매 관리 프로그램
    """
    # 데이터
    americano_name = "아메리카노"
    americano_price = 3000
    americano_stack = 10

    moca_name = "모카"
    moca_price = 4000
    moca_stack = 10

    latte_name = "라떼"
    latte_price = 5000
    latte_stack = 10

    sales_price = 0 

    while(True) :
        print("\n==========Index==========")
        print("음료판매(1) : ")
        print("현황(2) : ")
        print("종료(3) : ")
        menu = int(input("입력 : "))

        if (menu == 1) :
            print("===========Menu==========")
            print(f"{americano_name}({0})")
            print(f"{moca_name}({1})")
            print(f"{latte_name}({2})")

            drink = int(input("\n * 음료코드 : "))
            order_cnt = int(input(" * 주문량 : "))
            print()

            if (drink == 0) :
                if (americano_stack < order_cnt) :
                    print("재고가 없습니다.")  
                    continue

                americano_stack -= order_cnt
                sales_price += americano_price*order_cnt
                print(f"제품명 : {americano_name}")
                print(f"판매가 : {americano_price}")
                print(f"판매수량 : {order_cnt}")
                print(f"결제금액 : {americano_price*order_cnt}")
                print(f"재고 : {americano_stack}")
            elif (drink == 1) :
                if (moca_stack < order_cnt) :
                    print("재고가 없습니다.")
                    continue
                moca_stack -= order_cnt
                sales_price += moca_price*order_cnt
                print(f"제품명 : {moca_name}")
                print(f"판매가 : {moca_price}")
                print(f"판매수량 : {order_cnt}")
                print(f"결제금액 : {moca_price*order_cnt}")
                print(f"재고 : {moca_stack}")
            
            elif (drink == 2) :
                if (latte_stack < order_cnt) :
                    print("재고가 없습니다.")
                    continue
                latte_stack -= order_cnt
                sales_price += latte_price*order_cnt
                print(f"제품명 : {latte_name}")
                print(f"판매가 : {latte_price}")
                print(f"판매수량 : {order_cnt}")
                print(f"결제금액 : {latte_price*order_cnt}")
                print(f"재고 : {latte_stack}")

        elif (menu == 2) :
            print("==========Status==========")
            print(f"{americano_name} | 재고 : {americano_stack}")
            print(f"{moca_name} | 재고 : {moca_stack}")
            print(f"{latte_name} | 재고 : {latte_stack}")
            print(f"\n매출 : {sales_price}")
        elif (menu == 3) :
            print("종료합니다.")
            break
        else :
            print("잘못된 입력입니다.")
            continue
main()


