"""
문자열 연산자
문자열 결합
문자열 반복
문자열 포함여부 확인
"""
a, b = "hello", "world"

print(a + " " + b)

print(a + " " + (b + "! ") * 3)

print("i" in a)
print("he" in a)


"""
사용자에게 입력받은 메세지를 출력해주는 프로그램 구현하시오.
메세지는 [id] : massage 형식으로 출력
"""
id = input("id : ")
massage = "no sb keep going", "it is what it is" # input("massage : ")
print("[" + id + "] :", massage)

print(f"[{id}] : {massage}")
print(f"[{id}] : {massage}" + " it is what it is")

print(f"[{id:30}] : {massage!r} {massage!a}")

print("a", "b", "c", "d", sep = "/", end = "!!")