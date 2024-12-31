# 함수

# 변수
SIZE = 5
stack = [None, None, None, None, None]
top = -1

# 메인

# Push()
top +=1
stack[top] = "커피"
top +=1
stack[top] = "녹차"
top +=1
stack[top] = "꿀물"
print(stack)

# Pop()
data = stack[top]
stack[top] = None
top -= 1
print("pop :", data, top)

data = stack[top]
stack[top] = None
top -= 1
print("pop :", data, top)

data = stack[top]
stack[top] = None
top -= 1
print("pop :", data, top)
