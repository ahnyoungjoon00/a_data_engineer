import random
# 함수
def seqSearch(arr, fData):
    pos = -1
    for i in range(len(arr)):
        if (arr[i]==fData):
            pos = i
            break
    return pos
# 변수
dataArr = [random.randint(30, 190) for _ in range(8)]
findData = random.choice(dataArr)

# 메인
print("배열 -->", dataArr)
position = seqSearch(dataArr, findData)
if (position != -1):
    print(findData, "의 위치는", position)
else :
    print(findData,"가 존재하지 않습니다.")