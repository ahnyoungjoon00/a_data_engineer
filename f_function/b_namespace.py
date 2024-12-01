"""
namespace : 변수가 저장되는 공간

builtin : 파이썬의 기본내장함수 및 기본 예외가 저장되는 공간
global : 전역에 선언된 변수가 저장되는 공간 
local : 함수 내부에 선언된 변수가 저장되는 공간

파이썬의 변수는 functional scope를 가진다.
: 함수안에서 선언된 변수는 함수안에서 사용가능하다.

block scope
: 변수의 수명주기가 코드블록을 따라가는 경우,
"""

global_var = "global_var" # 함수 외부에서 선언되는 변수
var = "전역변수"

def study_builtin() :
    print(dir(__builtins__))

# study_builtin()

def study_namespace() :
    # print(dir(global_var))
    global global_var
    global_var = "수정된 전역변수"
    

    outer_var = "outer_var" # 함수 내부에서 선언된 변수

    def inner_fnc() :
        inner_var = "inner_var"
        # outer_var = "outer_var" # 이렇게 해서는 수정이 안돼

        # nonlocal :
        # 지역 내부에서 한 뎁스 위에 있는 
        # local namespace의 변수를 사용하겠다는 의미
        nonlocal outer_var
        outer_var = "수정된 outer_var"

        if(True) :
            if_var = "if_var"
        print(if_var)

    print("호출 전 outer:", outer_var)
    inner_fnc()
    print("호출 후 outer:",outer_var)

print("호출 전 global:", global_var)
study_namespace()
print("호출 전 global:",global_var)


# 외부 namespace에서 내부 namespace에 저장된 변수를 사용할 수는 없다.
# print(outer_var)