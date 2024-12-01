def main() :
    """
    음료 판매 관리 프로그램
    """
    # 데이터
    name_lst = ["아메리카노", "모카", "라떼"]
    price_lst = [3000, 4000, 5000]
    stack_list = [10, 10, 10]

    sales_price = 0 

    while(True) :
        print("\n==========Index==========")
        print("음료판매(1) : ")
        print("현황(2) : ")
        print("종료(3) : ")
        menu = int(input("입력 : "))

        if (menu == 1) :
            print("===========Menu==========")
            # for name in name_lst :
            #     print(f"{name}({name_lst.index(name)})")
            for i in range(len(name_lst)) :
                print(f"{name_lst[i]}({i})")

            # 사용자가 입력한 음료코드가 유효한 음료코드인지 검증,
            # 유효하지 않다면 Index로 돌려보내는 검증로직 작성,
            # "유효하지 않은 음료코드입니다."

            drink = int(input("\n * 음료코드 : "))

            if drink not in range(len(name_lst)) :
                print("유효하지 않은 음료코드입니다.")
                continue

            order_cnt = int(input(" * 주문량 : "))
            if (stack_list[drink] < order_cnt) :
                print("재고가 없습니다.")
                continue
            
            print()
            stack_list[drink] -= order_cnt
            sales_price += price_lst[drink]*order_cnt

            print(f"제품명 : {name_lst[drink]}")
            print(f"판매가 : {price_lst[drink]}")
            print(f"판매수량 : {order_cnt}")
            print(f"결제금액 : {price_lst[drink]*order_cnt}")
            print(f"재고 : {stack_list[drink]}")


        elif (menu == 2) :
            print("==========Status==========")
            for i in range(len(name_lst)) :
                print(f"{name_lst[i]} | 재고 : {stack_list[i]}")

            print(f"\n매출 : {sales_price}")

        elif (menu == 3) :
            print("종료합니다.")
            break
        
        else :
            print("잘못된 입력입니다.")
            continue
main()