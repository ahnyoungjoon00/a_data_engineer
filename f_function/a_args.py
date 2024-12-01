
def study_arg1(a:int, b:int) :
    """
    타입힌트 : 사용자에게 인자의 타입에 대한 힌트를 제공
    """
    return a + b

# print(study_arg1(50, 60 ))

def study_arg2(age:int, user:str = "anonymuos") :
    """
    default-arg
    매개변수에 인자가 전달되지 않을 경우 사용할 기본값을 지정
    일반 매개변수 뒤에 작성되어야한다.
    """

    print(f"사용자 {user}의 나이는 {age}입니다.")

# study_arg2(50, "cantona")

def study_arg3(age:int, *args, user:str = "anonymous") :
    """
    가변매개변수
    매개변수의 개수를 지정할 수 없을 때 사용한다.
    사용자가 전달한 복수의 인자는 tuple안에 담겨 전달된다.
    일반 매개변수 뒤에 작성되어야한다.
    """
    print(args, type(args))
    sum = 0
    for i in args :
        sum += i
    
    print(f"가변인자의 합 : {sum}")

# study_arg3(100, 1, 2, 3, 4, 5, user = "ayj")

# 인자를 매개변수로 전달할 때,
# 어떤 매개변수에 들어가야하는 지를 
# 위치로 나타내는 방식을 위치인자 ex) 100
# 매개변수 명으로 나타내는 방식을 키워드인자 ex) user = "ayj"
# 키워드인자가 위치인자보다 뒤에 위치해야한다.

def study_arg4(age:int, *args, user:str = "anonymous", **kwargs) :
    """
    키워드 가변 매개변수
    인자를 넘길 때, 매개변수명을 지정해서 복수의 인자를 전달하면
    매개변수명을 key, 인자를 value로 가지는 dict에 담아서
    kwargs에 전달해준다.
    """

    print(kwargs, type(kwargs))
    for item in kwargs.items() :
        print(item)

# study_arg4(100, 1, 2, 3, 4, 5, user = "ayj", job = "pro", payment = 99)

def study_arg5(age:int, height:int):
    print(f"{age}살의 평균 키는 {height}입니다.")

args = (10, 25)
study_arg5(*args)