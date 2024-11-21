"""
자료구조 : 대량의 데이터를 관리하는 구조

sequence : 공통시퀀스 연산, 함수를 구현
    mutable : list
    immutable : tuple, str

list :
순서가 보장되고 중복을 허용하는 자료구조
변경 가능한(mutable) 객체 = 가변 시퀀스

데이터를 다루는 4가지 방법
CRUD

C : create
R : read
U : update
D : delete

"""

def list_create():
    """ 여러개의 데이터를 하나의 이름(변수) 로 다루기 위한 객체
        순서가 보장되고 중복을 허용하는 자료구조
    """
    # 모든 타입을 요소로 가질 수 있다.
    a = [1, 'a', True, [1,2,3]]
    a.append(10000)

    # a의 3번인덱스 뒤에 'python' 을 추가해야합니다.
    # [1, 'a', True, 'python', [1, 2, 3],  10000]
    a.insert(3,'python')
    print(a)

    for a ,b ,c ,d  in [[1,2,3,4],['a','a','a','a']]:
        print(a,b,c,d)


list_create()

def list_read():
    # a가 가지고 있는 위치 + index * 데이터의 크기
    # 요소가 메모리 상에서 4칸의 크기를 가짐
    a = [1, 2, 3, 4]

    # list안의 데이터는 index를 통해 접근할 수 있다.
    # index는 0부터 list안에 들어있는 요소의 개수(length, size) -1 까지
    # 순차적으로 증가하는 수열

    index0 = a[0]
    print(index0)

    # list안에 들어있는 요소를 반복문을 사용해 확인
    for e in a:
        print(e**2, end=' | ')


def list_update():
    a = [1, 2, 3, 4]
    a[2] = 100
    print(a)

def list_delete():
    a = [1, 2, 3, 4]
    del a[3]
    print(a)



# list_create()
# list_read()
# list_update()
list_delete()