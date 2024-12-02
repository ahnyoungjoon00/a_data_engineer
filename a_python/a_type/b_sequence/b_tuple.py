"""
tuple
immutable - 불변 시퀀스
tuple이 생성된 이후 수정이 불가능
수정 : tuple에 데이터를 넣거나, 삭제하거나, 특정 요소의 값을 수정
"""

def tuple_read() :
    # a, i, j, k, l = (1, 3, 5, "a", "b")
    a = (1, 3, 5, "a", "b")
    b, c, d = 9, 8, 7

    print(a)
    # print(a, i, j, k, l)
    print(b, c, d)
    print(type(a))
    print(type(b))

    for x in a :
        print(x)
tuple_read()