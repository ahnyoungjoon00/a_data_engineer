# 함수
def isQueueFull():
    global SIZE, queue, front, rear
    # 1
    if (front == -1) & (rear != SIZE-1):
        return False
    elif (front == -1) & (rear == SIZE-1):
        return True
    elif (front != -1) & (rear == SIZE-1):
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False
    # # case 1 : rear가 마지막이 아닐때(기본)
    # if (rear != SIZE-1):
    #     return False
    # # case 2 : rear는 마지막이 맞고, front가 -1일때, (진짜 full)
    # elif (rear == SIZE-1) & (front == -1):
    #     return True
    # # case 3 : rear는 마지막, front가 -1이 아님(앞쪽 빈칸)
    # elif (rear == SIZE-1) & (front != -1):
    #     for i in range(front+1, SIZE, 1):
    #         queue[i-1] =queue[i]
    #         queue[i] = None
    #     front -= 1
    #     rear -= 1
    #     return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front >= rear):
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if isQueueFull():
        print("*********Full-Queue*********")
        return
    rear+=1
    queue[rear] = data
    print(data, "출구<--", queue, "<--입구")

def deQueue() :
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print("*********Empty-Queue*********")
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print("*********Empty-Queue*********")
        return
    data = queue[front+1]
    return data
# 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1
# 메인

# enQueue
enQueue("나연")
enQueue("모모")
enQueue("지효")
enQueue("정연")
enQueue("사나")
enQueue("쯔위")
print("==================================")

# deQueue
data = deQueue()
print(data, "출구<--", queue, "<--입구")
data = deQueue()
print(data, "출구<--", queue, "<--입구")
data = deQueue()
print(data, "출구<--", queue, "<--입구")
print("==================================")
# peek
data = peek()
print(data, "출구<--", queue, "<--입구")
data = peek()
print(data, "출구<--", queue, "<--입구")
data = peek()
print(data, "출구<--", queue, "<--입구")
print("==================================")


enQueue("나연")
enQueue("모모")
print("==================================")
