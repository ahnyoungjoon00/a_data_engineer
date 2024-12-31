import random
# 함수
def addNum(num):
    if (num == 1):
        return 1
    return num + addNum(num-1)
# 메인
print(addNum(100))