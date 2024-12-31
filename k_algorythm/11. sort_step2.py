import random
# 함수
def selectSoft(arr):
    # n = len(arr)
    # for i in range(n-1):
    #     minIdx = i
    #     for j in range(i+1, n):
    #         if(arr[minIdx] > arr[j]):
    #             minIdx = j
    #     arr[i], arr[minIdx] = arr[minIdx], arr[i]
    # return arr
    
    for i in range(len(arr)-1):
        MinIdx = i
        for j in range(i+1, len(arr)):
            if (arr[MinIdx] > arr[j]):
                MinIdx = j
        arr[i], arr[MinIdx] = arr[MinIdx], arr[i]
    return arr
        
# 변수
dataArr = [random.randint(30, 190) for _ in range(8)]

# 메인
print("정렬 전 -->", dataArr)
dataArr = selectSoft(dataArr)
print("정렬 후 -->", dataArr)