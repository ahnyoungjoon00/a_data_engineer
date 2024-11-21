"""
문자열 연산자
문자열 결합
문자열 반복 
문자열 포함여부 확인
"""

a, b = 'hello', 'world'

# helloworld로 만들고 싶다면
print(a + b)

# helloworldworldworld
print(a + b * 3)

# hello 안에 he 지 확인
print('he' in a)

"""
사용자에게 입력받은 메세지를 출력해주는 프로그램을 구현하시오
메세지는 [{id}]: {message}
형식으로 출력합니다.
"""
id = input('id: ')
message = input('message: ')
print('[' + id + ']: ' + message)

# f-strings
print(f'[{id:30}]: {message}')

print('a', 'b', 'c', 'd', sep='/', end='\n')
print('a', 'b', 'c', 'd', sep='/', end='\n')