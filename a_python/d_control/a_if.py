"""제어문
    코드의 흐름을 제어하는 문법
    조건문 : if, elif, else

    조건식 : 결과가 진리값인 연산(비교, 논리 연산)
    조건식의 결과가 참이면 코드블록을 실행, 아니면 건너뜀

    # 형태
    if (조건식) :
        코드블록
"""


def study_if(arg) :
    """
    인수가 짝수인지 홀수인지 판단하는 코드 작성
    """
    if (arg % 2) == 0 :
        print("짝수")
    else :
        print("홀수")
# study_if 함수에 숫자를 인수로 전달하여 결과를 확인
study_if(5)


# import time
# for i in range(0, 10) :
#     study_if(i)
#     time.sleep(0.2)


def study_sum_if(a, b, c) :
    """
    3개 인수를 전달 받아 인수를 더한 값이 짝수인지 홀수인지 판단하는 코드 작성
    """
    sum = a + b + c
    if (sum % 2) == 0 :
        print("짝수")
    else :
        print("홀수")
study_sum_if(5, 4, 7)