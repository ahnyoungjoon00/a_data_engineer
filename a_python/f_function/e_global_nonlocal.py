"""
파이썬의 함수는 1급객체이다.
1급객체는 값으로 다룰 수 있음을 의미한다.
값으로 다룰 수 있다는 것은 변수에 할당할 수 있다는 것을 의미한다.
함수를 매개변수로 전달하거나, 반환값으로 쓸 수 있다는 뜻
"""
x = 100
y = 200
def proxy_fn() :
    x = 10
    y = 20
    cnt = 0
    print(f'{cnt} 호출, {x}, {y}로 변경되었습니다.')
    def counting() :
        global x
        nonlocal y
        nonlocal cnt
        x = 1000
        y = 2000
        cnt += 1
        print(f'{cnt} 호출, {x}, {y}로 변경되었습니다.')
    counting()
    print(f'{cnt} 호출, {x}, {y}로 변경되었습니다.')
proxy_fn()