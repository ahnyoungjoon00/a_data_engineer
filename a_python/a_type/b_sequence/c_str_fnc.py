str = '  Strings are immutable sequences of Unicode code points   '

#1. str의 모든 문자를 대문자로 바꿔주세요.
print(str.upper())
print("--------------------------------------")
#2. str의 길이를 출력하세요.
print(len(str))
print("--------------------------------------")
#3. str을 모두 소문자로 바꿔 출력 해주세요.
print(str.lower())
print("--------------------------------------")
#4. str에 있는 "sequences"를 "시퀀스"로 바꿔 출력 해주세요
print(str)
print(str.replace("sequences", "시퀀스"))
print("--------------------------------------")
#5. str에서 첫번째 U의 위치를 구해주세요.
print(str.find("U"))
print("--------------------------------------")
#6. str의 앞 뒤 공백을 제거해서 출력해주세요
print(str.strip())
print("--------------------------------------")
#7. str을 공백문자를 기준으로 분리해, 
#   분리된 토큰을 요소로 가지는 리스트를 만들어주세요
str_lst = str.strip().split(sep = " ")
print(str_lst)