# 함수
def isQueueFull():
    global SIZE, queue, front, rear
    # 1
    if ((rear+1)%SIZE == front):
        return True
    else :
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if isQueueFull():
        print("*********Full-Queue*********")
        return
    rear = (rear + 1)%SIZE
    queue[rear] = data
    print(data, "출구<--", queue, "<--입구")

def deQueue() :
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print("*********Empty-Queue*********")
        return
    front += (front+1)%SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print("*********Empty-Queue*********")
        return
    data = queue[(front+1)%SIZE]
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
print("==================================")

# deQueue
data = deQueue()
print(data, "출구<--", queue, "<--입구")
data = deQueue()
print(data, "출구<--", queue, "<--입구")
data = deQueue()
print(data, "출구<--", queue, "<--입구")
print("==================================")

enQueue("화사")
enQueue("솔라")
print("==================================")
