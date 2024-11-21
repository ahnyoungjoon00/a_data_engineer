"""
코드 블록 :
    특정 작업을 수행하는 코드의 그룹
    타 프로그래밍언어 코드블록: {} 
    파이썬의 코드블록은 들여쓰기로 표현

함수 : 이름이 있는 코드 블록, 이름으로 코드블록을 호출할 수 있다.
      경우에 따라서 호출부로 인수를 전달하기 위한 매개변수가 있다.
      경우에 따라서 결과값을 반환할 수 있다.

def 함수명(매개변수...):
    코드블록...
    return문

    표현식 : 값을 부여하거나 계산하는 형태의 연산
    return문 : return 표현식 | None
    return문을 수행하면 표현식을 반환값으로 해 현재의 함수호출을 떠난다.

docString : document String
    함수, 클래스, 모듈 등을 설명하기 위한 텍스트
    함수의 첫 줄에 multiline string으로 작성

    파이썬 줄 (line)
    물리적인 line : 실제 코드 상의 한 줄
    논리적인 line : 하나의 표현식

    파이썬은 암묵적으로 물리적인 line과 논리적인 line이 같다고 가정
"""

a = "가나다라마바사 \
아자차카타파하 \
가나다라마바사 \
아자차카타파하 \
가나다라마바사 "

def q2():
    """ q2. 사용자로부터 입력받은 숫자가 짝수인지 판단하는 코드를 작성하세요.
        단, 입력값은 정수만 입력된다고 가정합니다.
    """
    inp = input('숫자만 입력: ')
    n = int(inp)
    print(type(inp))
    print(n % 2 == 0)

def q3():
    """ q3. 아래 논리연산의 결과값을 예상해 보세요.
    """
    a, b, c, d, = True, False, False, False
    print(a or b and c or d)

def q4():
    """ q4. 사용자가 입력한 문자가 (y or Y) 인지 확인하는 코드를 작성하시오.
        단 알파벳만 입력된다고 가정합니다.
        출력예시 : y ? : True/False
    """
    inp = input('알파벳만 입력: ')
    print('y ? : ', inp == 'y' or inp == 'Y')

# q1이라는 이름의 코드블록을 실행해달라고 컴퓨터에게 요청

def calcurate_hypotenuse(base, height):
    square = base ** 2 + height **  2
    return square ** 0.5

def q5():
    """ q1. 밑변의 길이가 8, 높이가 11인 직각삼각형의 빗변의 길이를 구하시오.
    """
    calcurate_hypotenuse(3, 4)


def q6():
    """ q1. 밑변의 길이가 99, 높이가 100인 직각삼각형의 빗변의 길이를 구하시오.
    """
    calcurate_hypotenuse(99, 100)


def q7():
    """
    밑변의 길이가 10이고 높이가 10인 직각삼각형의 빗변의 길이를
    시속 30키로미터로 달릴 때 걸리는 시간을 구하시오
    빗변의 길이단위는 km로 가정합니다.
    """
    length = calcurate_hypotenuse(10, 10)
    print('시간:', length / 30)


q7()