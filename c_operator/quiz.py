"""
코드 블록 :
      특정 작업을 수행하는 코드 그룹
      타 프로그래밍 언어 코드블록 : {}
      파이썬의 코드블록은 들여쓰기로 표현

함수 : 
      이름이 있는 코드 블록, 이름으로 코드블록을 호출할 수 있다.
      경우에 따라서 호출부로 인수를 전달하기 위한 매개변수가 존재 가능하다.
      경우에 따라서 결과값을 반환할 수 있다.

      def 함수명(매개변수, ...) :
            코드블록, ...
            return문
      표현식 : 값을 부여하거나 계산하는 형태의 연산
      return문 : 
            return 표현식(흔히 procedure라 부름) | None(없을수도 있단 얘기)
            return문을 수행하면 표현식을 반환값으로 해 현재의 함수호출을 떠난다(=끝낸다).

docString : document String
      함수, 클래스, 모듈 등을 설명하기 위한 텍스트
      함수의 첫 줄에 multiline string으로 작성

      파이썬 줄(line)
            물리적 line : 실제 코드 창의 한 줄
            논리적 line : 하나의 표현식
        파이썬은 암묵적으로 물리적인 line과 논리적인 line이 같다고 가정
"""

a = "가나다라마바사 \
아자차카타파하 \
가나다라마바사 \
아자차카타파하 "
# 이렇게 작성한 경우 한 줄(line)으로 인식 가능 "\" 뒤에는 띄어쓰기를 포함해 아무것도 붙으면 안되는 구조


def q1():
    """q1. 밑변의 길이가 3, 높이가 4인 직각 삼각형의 빗변의 길이를 구하시오."""
    a, b = 3, 4
    print("c = ", (a**2 + b**2) ** 0.5)


def q2():
    """q2. 사용자로부터 입력받은 숫자가 짝수인지 판단하는 코드를 작성하시오.
      단, 입력값은 정수만 입력됩니다."""
    inp = int(input("숫자만 입력 : "))
    # print(inp)
    print(int(inp) % 2 == 0)


def q3():
    """q3. 아래 논리연산의 결과값을 예상해보시오."""
    a, b, c, d = True, False, False, False
    print(a or b and c or d)


def q4():
    """q4. 사용자가 입력한 문자가 (y or Y)인지 확인하는 코드를 작성하시오."""
    inp = input("문자만 입력 : ")
    # print(inp)
    print("y ? :", str(inp) == "y" or str(inp) == "Y")


# q1()
# q2()
# q3()
# q4()


"""q1 함수의 추상화"""
def calculate_hypotenuse(base, height):
    """밑변의 길이가 a, 높이가 b인 직각 삼각형의 빗변의 길이를 구하시오."""
    square = base ** 2 + height ** 2
    print(square ** 0.5, "------")
    return square ** 0.5
calculate_hypotenuse(5, 7)
calculate_hypotenuse(99, 100)


def calculate_time() :
    """
    밑변의 길이가 10, 높이가 10인 직각삼각형의 빗변(km)을
    30km/h로 달릴 때 걸리는 시간을 구하시오"""
    length = calculate_hypotenuse(10, 10)
    print(f"시간 : {length / 30}")
calculate_time()