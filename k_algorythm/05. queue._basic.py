# 함수

# 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1
# 메인

# enQueue
rear += 1
queue[rear] = "나연"
print("출구<--", queue, "-->입구")
rear += 1
queue[rear] = "모모"
print("출구<--", queue, "-->입구")
rear += 1
queue[rear] = "지효"
print("출구<--", queue, "-->입구")

# deQueue
front += 1
data = queue[front]
queue[front] = None
print("식사 :", data, "\n", "출구<--", queue, "-->입구")
front += 1
data = queue[front]
queue[front] = None
print("식사 :", data, "\n", "출구<--", queue, "-->입구")
front += 1
data = queue[front]
queue[front] = None
print("식사 :", data, "\n", "출구<--", queue, "-->입구")