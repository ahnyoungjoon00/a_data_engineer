# 함수
def addNum(num):
    if (num<=1):
        return 1
    return num * addNum(num-1)
# 메인
print(addNum(5))


# 함수
def countDown(num):
    if (num==0):
        print("발사!!!!!!!!!!!")
    else :
        print(f"{num}!!!")
        countDown(num-1)
# 메인
countDown(5)

# 함수
def printStar(num):
    if (num>0):
        printStar(num-1)
        print("*"*num)
# 메인
printStar(5)

