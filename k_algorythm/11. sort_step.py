# 함수
import random
def findMinIndex(arr):
    minIdx = 0
    for i in range(1, len(arr), 1):
        if (arr[minIdx] > arr[i]):
            minIdx = i
    return minIdx

def sortArr(arr):
    newArr = []
    for _ in range(len(arr)):
        minPos = findMinIndex(arr)
        newArr.append(arr[minPos])
        del[arr[minPos]]
    print(newArr)
    return newArr
# 변수
before = [random.randint(30, 190) for _ in range(8)]
after = []

# 메인
# print("정렬 전 -->", before)
# for _ in range(len(before)):
#     minPos = findMinIndex(before)
#     after.append(before[minPos])
#     del[before[minPos]]
# print("정렬 후 -->", after)

after = sortArr(before)
after