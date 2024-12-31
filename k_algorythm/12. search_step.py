import random
# 함수
def binSearch(arr, fData):
    pos = -1
    start = 0
    end = len(arr)-1
    while (start <= end):
        mid = (start+end)//2
        if (arr[mid] == fData):
            pos = mid
            break
        elif (arr[mid] < fData):
            start = mid+1
        else :
            end = mid-1
    return pos
# 변수
dataArr = sorted([random.randint(30, 190) for _ in range(8)])
findData = random.choice(dataArr)

# # 메인
print("배열 -->", dataArr)
position = binSearch(dataArr, findData)
if (position != -1):
    print(findData, "의 위치는", position)
else :
    print(findData,"가 존재하지 않습니다.")