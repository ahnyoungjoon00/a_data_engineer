# 함수
def isStackFull():
    global SIZE, stack, top
    if (top==SIZE-1):
        return True
    else :
        return False
def isStackEmpty():
    global SIZE, stack, top
    if (top <= -1):
        return True
    else:
        return False
    
def push(data):
    global SIZE, stack, top
    checkStack = isStackFull()
    if checkStack :
        print("**********Full-Stack**********")
        return
    top += 1
    stack[top] = data
    print(stack)


def pop():
    global SIZE, stack, top
    checkStack = isStackEmpty()
    if checkStack :
        print("**********Empty-Stack**********")
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    checkStack = isStackEmpty()
    if checkStack :
        print("**********Empty-Stack**********")
        return
    return stack[top]
# 변수
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

# 메인

# Push()
push("커피")
push("녹차")
push("꿀물")
push("콜라")
push("환타")
push("펩시")

# Pop()
retData = pop()
print("pop ---------->", retData)
retData = pop()
print("pop ---------->", retData)
peekData = peek()
print("peek ---------->", peekData)
retData = pop()
print("pop ---------->", retData)
retData = pop()
print("pop ---------->", retData)
peekData = peek()
print("peek ---------->", peekData)
retData = pop()
print("pop ---------->", retData)