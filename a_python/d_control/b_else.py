"""양자택일 조건문
if(조건식) :
    코드블록
else :
    코드블록
"""

def study_else(arg) :
    """매개변수로 전달된 정수가 짝수인지, 홀수인지 판단하는 코드"""

    if arg%2 == 0 :
        print("짝수")
    else :
        print("홀수")