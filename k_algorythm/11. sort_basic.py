# 함수
def findMinIndex(arr):
    # minIdx = 0
    # for i in range(1, len(arr), 1):
    #     if (arr[minIdx] > arr[i]):
    #         minIdx = i
    # return minIdx
    defaultIdx = 0
    for i in range(len(arr)):
        if (arr[defaultIdx] > arr[i]) :
            defaultIdx = i
    return defaultIdx
# 변수
testArray = [55, 88, 33, 77]

# 메인
minPos = findMinIndex(testArray)
print("최솟값-->", testArray[minPos])