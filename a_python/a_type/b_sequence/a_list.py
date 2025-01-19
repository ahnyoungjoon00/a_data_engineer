"""
자료구조 : 대량의 데이터를 관리하는 구조

sequence : 공통시퀀스 연산, 함수를 구현
    mutable : list
    immutable : tuple, str
list :
순서가 보장되고 중복을 허용하는 자료구조
변경 가능한(mutable) 객체 + 가변 시퀀스

데이터를 다루는 4가지 방법(CRUD)

C : create
R : read
U : update
D : delete
"""

def list_create() :
    """
    여러개의 데이터를 하나의 이름(변수)로 다루기 위한 객체
    순서가 보장되고 중복을 허용하는 자료구조
    """
    # 모든 타읍을 요소로 가질 수 있다.
    a = [1, "a", True, [1, 2, 3]]
    print(a)

def list_add_1() :
    a = [1, "a", True, [1, 2, 3]]
    a.append(10000)
    print(a)

def list_add_2() :
    a = [1, "a", True, [1, 2, 3]]
    a.insert(3, "python")
    print(a)

def list_read() :
    # list안의 데이터는 index를 통해 접근할 수 있다.
    # index는 [0:n-1]까지의 범위
    # 순차적으로 증가
    a = [1, "a", True, [1, 2, 3]]
    b = [1, 2, 3, 4, 5]
    for i in range(0, len(a)) :
        print(a[i])
    for j in b:
        print(j**2, end = " | ")

def list_update() :
    a = [1, 2, 3, 4]
    a[2] = 100
    print(a)

def list_delete() :
    a = [1, 2, 3, 4]
    del a[-1]
    print(a)

list_create()
list_add_1()
list_add_2()
list_read()
list_update()
list_delete()


for i, j, k, l in [[1, 2, 3, 4], ["a", "b", "c", "d"], [True, False, True, False], [1800, 2500, 7300, 3200]] :
    print(i, end = " | ")
    print(j, end = " | ")
    print(k, end = " | ")
    print(l, end = " | ")