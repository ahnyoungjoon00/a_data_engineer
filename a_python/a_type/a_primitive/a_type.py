a = [1, 2, 3]
b = a
a.append("a")
print(a)
print(b)
b.append("b")
print(a)
print(b)
print(len(a))

print("Hello World!")

""" literal 확인
literal : 직접 표현된 값, 변수에 할당되지 않은 값
"""

print(1)
print(1.1)
print(True)
print(False)
print("hi world")

""" type
type : 형태, 모양
type() : 인자의 타입을 변환
"""

print(type(1))
print(type(1.1))
print(type(True))
print(type(False))
print(type("hi world"))

print("""
형변환
""")

print(float(10))
print(int(True))
print(ord("h"))

print("""
숫자를 문자로 인코딩한 값
      """)
print(chr(104))

print("하 명도 강사님", "010-3329-3364")


print("""
파이썬은 객체의 boolean 변환을 지원해준다.
str = 빈 문자열이면 False
int, float = 0이면 False
None = False
""")


print(bool(0))
print(bool(100))
print(bool(''))
print(bool('aaaa'))
print(bool(None))
print(bool(1))