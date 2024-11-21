"""
다중조건문
"""

def study_elif(score):
    """ 매개변수로 점수를 전달 받아 등급을 출력하세요
	90점 이상이면 A
	80점 이상 90점 미만이면 B
	70점 이상 80점 미만이면 C
	60점 이상 70점 미만이면 D
	60점 미만이면 F 로 등급입니다.
    """
    if(score >= 90):
        print('A등급')
    elif(score >= 80):
        print('B등급')
    elif(score >= 70):
        print('c등급')
    elif(score >= 60):
        print('d등급')
    else:
        print('F')

study_elif(77)