def fnc1():
    """
    a = (1, 'a', True, (1,2,3))
    b = (1.1, None)
    두 튜플을 합쳐 c 변수에 할당하세요.
    """
    a = (1, 'a', True, (1,2,3))
    b = (1.1, None)
    c = a + b
    print(c)

def fnc2():
    """
    a = (1, 'a', True, (1,2,3), 1.1, None)
    a의 1,3,5 인덱스의 요소를 요소로 가지는 튜플을 구하세요.
    """
    a = (1, 'a', True, (1,2,3), 1.1, None)
    print(a[1::2])

def fnc3():
    """
    a = (1, 'a', True, (1,2,3), 1.1, None) 의
    길이를 구하시오.
    """
    a = (1, 'a', True, (1,2,3), 1.1, None)
    print(len(a))

def fnc4():
    """
    a = (30, 8, 900, 77, -9, 100)
    a의 가장 작은 요소와 가장 큰 요소의 합을 구하시오.
    """
    a = (30, 8, 900, 77, -9, 100)
    print(max(a) + min(a))

def fnc5():
    """
    a = (30, 8, 900, 7, -9, 100, 7)
    a에서 7이 등장하는 총수를 구하시오
    """
    a = (30, 8, 900, 7, -9, 100, 7)
    print(a.count(7))

# fnc1()
# fnc2()
# fnc3()
# fnc4()
# fnc5()

a = (1, 'a', True, (1,2,3))
b = (1.1, None)
c = a + b
d = c + (1)
e = c + (1, )
print(c)
print(d)
print(e)
