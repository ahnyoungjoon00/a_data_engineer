""" 연산자
산술연산자
    +, -, *, /(실수나누기), //(정수나누기 몫), %(정수나누기 나머지), **

    !! 컴퓨터는 같은 타입끼리만 연산이 가능하다.
    !! 정수와 실수간 연산이 발생하면, 정수를 실수로 바꿔서 연산

    // a를 b로 나누었을 때 , a는 b * q(몫) + r(나머지)
    a = bq + r

비교연산자
    ==, != , >=, <=, >, <

논리연산자
    and, or
    and : 양쪽 항의 값이 True이면 연산결과가 True, 아니면 False
    2 > 1 and 5 < 3  => True and False => False
    
    or : 양쪽 항의 값 중 하나라도 True 이면 True, 양쪽 항의 값이 모두 False 이면 False
    2 > 1 or 5 < 3 => True or False => True

    드모르간 법칙

    not A or not B = not(A and B)
    True, False
    False, True
    False, False

    not A and not B = not(A or B)
    False, False

대입연산자
    =
    변수에 값을 할당하기 위해 사용

연산자 우선순위
    1. 산술연산자의 우선순위
        1. 지수 : **
        2. 곱하기, 나누기 : *, /, //, %
        3. 더하기, 빼기 : +, -

    2. 비교연산자의 우선순위
        1. 모든 비교연산자

    3. 논리연산자의 우선순위
        1. not
        2. and
        3. or


문자열연산자
    +, * , in
"""

print("""
산술연산자 써보기
""")

print( 100 // 3, 100 % 3)

print(100 + 200)
print(100 - 200)
print(100 * 200)
print(100 / 200)
print(100 // 200)
print(100 % 200)

# 지수거듭제곱법칙 : X의 M제곱의 3제곱은 X의 3M
print(100 ** 2)
print(100 ** 0.5)


