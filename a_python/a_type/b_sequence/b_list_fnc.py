def fnc1():
    """
    a = [1, 'a', True, [1,2,3]]
    b = [1.1, None]
    두 리스트를 합쳐 c 변수에 할당하세요.
    """
    a = [1, 'a', True, [1,2,3]]
    b = [1.1, None]
    c = a + b
    print(c)

def fnc2():
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    a의 1,3,5 인덱스의 요소를 요소로 가지는 list를 구하세요.
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    print(a[1::2])

def fnc3():
    """
    a = [1, 'a', True, [1,2,3], 1.1, None] 의
    길이를 구하시오.
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    print(len(a))

def fnc4():
    """
    a = [30, 8, 900, 77, -9, 100]
    a의 가장 작은 요소와 가장 큰 요소의 합을 구하시오.
    """
    a = [30, 8, 900, 77, -9, 100]
    print(max(a) + min(a))

def fnc5():
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    의 순서를 뒤집으세요.
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    print(a)
    a.reverse()
    print(a)

def fnc5_1():
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    의 순서를 뒤집으세요.
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    print(a)
    print(a[::-1])

def fnc6():
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    의 0, 2, 4 인덱스의 요소를 -999로 대체하세요.
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    print(a)
    a[0::2] = -999, -999, -999
    print(a)

def fnc7():
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    의 복사본을 만들어 b에 할당하시오
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    b = a.copy()
    print(b)

fnc1()
fnc2()
fnc3()
fnc4()
fnc5()
fnc5_1()
fnc6()
fnc7()

def copy() :
    starbuks = ["아메리카노", "카페라떼", "프라푸치노"]
    print("starbuks", starbuks)

    bbaeck = starbuks
    bbaeck.append("식혜")
    print("bbaeck", bbaeck)

    print("?", starbuks)
    print("starbuks 주소", id(starbuks))
    print("bbaeck 주소", id(bbaeck))
copy()