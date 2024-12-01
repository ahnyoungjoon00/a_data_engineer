"""
논리연산자
    and, or
    and : 모두 True 일때만 True, 하나라도 아닐 시, False
    or : 양쪽 값 중 하나라도 True면 True, 모두 False 일때만 False

    드모르간 법칙

    not(A and B) = not A or not B
    not(A or B) = not A and not B
"""
print(not(3 >= 3) and not(3 < 4))
print(not(3>= 3 or 3 < 4))