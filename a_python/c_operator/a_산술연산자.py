"""연산자 우선순위
    산술연산자의 우선순위
        1. 지수 **
        2. 곱하기, 나누기 *, /, //, %
        3. 덧셈, 뺄셈 +, -

    비교연산자의 우선순위
        - 먼저 온 순서대로
    
    논리연산자의 우선순위
        1. not
        2. and
        3. or

        드모르간 법칙
        not A or not B = not(A and B)
        True, False
        False, True
        False, False

        not A and not B = not(A or B)
        False, False
"""


"""산술연산자
    +, -, *, /(실수), //(정수, 몫), %(정수, 나머지), **(지수 연산자, 제곱)
    
    - 컴퓨터는 같은 타입끼리만 연산 가능
    - 정수와 실수간 연산 발생 시, 정수를 실수로 변환하여 연산
"""
print(100 + 200)
print(100 - 200)
print(100 * 200)
print(100 / 200)
print(100 // 200)
print(100 % 200)
print(100 ** 2)
print(100 ** 0.5)

"""
대입연산자
    변수에 값을 할당하기 위해 사용
"""

"""
문자열연산자
    +, *, in, ...
"""