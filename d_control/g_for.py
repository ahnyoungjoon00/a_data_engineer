"""
for문
특정 횟수를 반복하는 반복문을 안전하게 작성할 수 있게 도와주는 문법
"""
def study_for():
    # i : 0, 1, 2, 3, 4
    for i in range(0, 5):
        print(i, '안녕 파이썬')

def study_for_sum():
    """ 1부터 10까지 정수들의 합계를 구하시오.
        1. for문을 사용한다.
        2. 4의 배수는 합계를 구할 때 제외한다.(제외 가능)
    """
    sum = 0
    for i in range(1, 11):
        if(i % 4 != 0):
            sum = sum + i
        print(sum)
    else:
        print(sum)


study_for_sum()