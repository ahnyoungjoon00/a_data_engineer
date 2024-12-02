""" 변수
값 또는 데이터를 저장할 수 있는, 이름이 붙은 메모리 공간
"""

age = 34
cnt = 34
score = 34

print(id(34))
print(id(age))
print(id(cnt))
print(id(score))

print("1. 변수를 선언하고 값을 할당합니다.")
intVar = 1
floatVar = 1.0
boolTrue = True
strVar = "hi"

print(intVar)
print(floatVar)
print(boolTrue)
print(strVar)
print(age)
print(cnt)

print("2. 변수의 타입")
print(type(intVar))
print(type(floatVar))
print(type(boolTrue))
print(type(strVar))
print(type(age))
print(type(cnt))


print("3. 여러 변수를 한번에 선언하고 할당 할 수 있다")
a, b, c, d, e = 1, 1.0, True, False, "hi"
print(a)
print(b)
print(c)
print(d)
print(e)


print("4. 같은 값이라면 여러 변수에 한번에 할당 할 수 있다.")
f = g = h = "number4"
print(f)
print(g)
print(h)

print("5. 비어있는 변수는 None 할당")
empty = None
print(empty)