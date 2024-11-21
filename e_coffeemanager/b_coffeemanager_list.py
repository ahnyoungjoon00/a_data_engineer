def main():
    """
    음료판매관리프로그램
    """
    # 음료관련 데이터
    names = ['아메리카노', '모카', '라떼']
    prices = [3000, 4000, 5000]
    stocks = [10, 10, 10]

    sales_price = 0 # 매출

    while(True):
        print('\n==========Index==========')
        print('음료판매(1)')
        print('현황(2)')
        print('종료(3)')
        menu = int(input('입력: '))

        if(menu == 1):
            print('\n==========Menu==========')
            for name in names:
                print(f'{name}({names.index(name)})')

            drink = int(input('\n * 음료코드: '))
            order_cnt = int(input(' * 주문수량: '))

            # 사용자가 입력한 음료코드가 유효한 음료코드인지 검증하고, 
            # 유효하지 않다면 Index로 돌려보내는 검증로직을 작성하세요.
            # '유효하지 않은 음료코드입니다.'

            if(drink < 0 or drink >= len(names)):
                print('유효하지 않은 음료코드입니다.')
                continue

            if(stocks[drink] < order_cnt):
                print('재고가 없습니다.')
                continue

            stocks[drink] -= order_cnt
            sales_price += prices[drink] * order_cnt

            print(f'\n제품명: {names[drink]}')
            print(f'판매가: {prices[drink]}')
            print(f'판매수량: {order_cnt}' )
            print(f'결제금액: {prices[drink] * order_cnt}')
            print(f'남은 재고: {stocks[drink]}')
        
        elif(menu == 2):
            print('\n==========Status==========')
            for i in range(0, len(names)):
                print(f'{names[i]} | 재고: {stocks[i]}')

        elif(menu == 3):
            print('종료합니다.')
            break

main()