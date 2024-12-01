"""
다중 조건문

if a :
    aa
else :
    if b :
        bb
    else :
        if c :
            cc
        else 
    ~~~~

    ---->>>>>

if a :
    aa
elif b :
    bb
elif c :
    cc
else : 
    dd
"""


def study_elif(score) :
    """ 매개변수로 점수를 전달 받아 등급을 출력하세요
	90점 이상이면 A
	80점 이상 90점 미만이면 B
	70점 이상 80점 미만이면 C
	60점 이상 70점 미만이면 D
	60점 미만이면 F 로 등급입니다.
    """
    if score >= 90 :
        print("A")
    elif score >= 80 :
        print("B")
    elif score >= 70 :
        print("C")
    elif score >= 60 :
        print("D")
    else :
        print("F")

import time
for i in range(50, 101, 5) :
    study_elif(i)
    time.sleep(0.5)

