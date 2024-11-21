"""
변수와 함수가 저장되는 공간
builtin : 파이썬의 기본내장함수 및 기본 예외가 저장되는 공간
global : 전역에 선언된 변수가 저장되는 공간
local : 함수 내부에 선언된 변수가 저장되는 공간

파이썬의 변수는 functional scope를 가진다.
함수안에서 선언된 변수는 함수 안에서 사용이 가능하다.

block scope:
변수의 생명주기가 코드블록을 따라가는 경우
"""

global_var = 'global_var'
var = '전역변수'

def study_builtin():
    print(dir(__builtins__))

# study_builtin()

def study_namespace():
    global global_var
    global_var = '수정된 global_var'

    # local var
    outer_var = 'outer_var'

    def inner_fnc():
        inner_var = 'inner_var'

        # nonlocal : 
        # 지역 내부에서 한 뎁스 위에 있는
        # local namespace의 변수를 사용하겠다는 의미
        nonlocal outer_var
        outer_var = '수정된 outer_var'

        if(True):
            if_var = 'if_var'
        
        print(if_var)
    
    print(outer_var)
    inner_fnc()
    print(outer_var)

print(global_var)
study_namespace()
print(global_var)

# 외부 namespace에서 내부 namespace에 저장된 변수를 사용할 수는 없다.
#print(outer_var)