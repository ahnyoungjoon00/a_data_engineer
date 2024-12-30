"""
for문
특정 횟수를 반복하는 반복문을 안전하게 작성할 수 있게 도와주는 문법
"""

def study_for() :
    for i in range(1, 6) :
        print(i, "안녕 파이썬")
    print("!!!!!!!완료!!!!!!!!")
# study_for()

# --------------------------------------------

def study_for_sum() :
    """
    1부터 10까지의 합계를 구하시오
    1. for문 사용
    2. 4의 배수는 합계를 구할 때 제외한다.
    """
    sum = 0
    for i in range(1, 11) :
        if i%4 == 0 :
            continue
        else :
            sum += i
    print(sum)
study_for_sum()

# --------------------------------------------

# def study_for_sum() :
#     """
#     1부터 10까지의 합계를 구하시오
#     1. for문 사용
#     2. 4의 배수는 합계를 구할 때 제외한다.
#     """
#     sum = 0
#     for i in range(1, 11) :
#         if i%4 != 0 :
#             sum += i
#     print(sum)
# study_for_sum()