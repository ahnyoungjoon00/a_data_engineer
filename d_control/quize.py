def q1(hasEgg):
    """ 매개변수로 계란의 유무를 입력 받고
    개발자가 사올 우유의 개수를 출력해주는 코드를 작성하세요.
    """
    milkCnt = 1
    if(hasEgg):
        milkCnt = 6
    
    print(f'우유 {milkCnt}개 사왔어!')


def q2(number):
    """ 매개변수로 전달된 숫자가, 양수인지, 음수인지, 0인지 판단하는 코드를 작성하시오"""
    if(number > 0):
        print('양수입니다.')
    else:
        if(number < 0):
            print('음수입니다.')
        else:
            print('0입니다.')

def q3(score):
    """ 매개변수로 점수를 전달 받아 등급을 출력하세요
	90점 이상이면 A
	80점 이상 90점 미만이면 B
	70점 이상 80점 미만이면 C
	60점 이상 70점 미만이면 D
	60점 미만이면 F 로 등급입니다.

    만약 점수의 한자릿수가 5이상이라면
    +등급을 추가로 부여해주세요.
    ex) 90점 : A
        95점 : A+
    """
    grade = None

    if(score >= 90):
        grade = 'A'
    elif(score >= 80):
        grade = 'B'
    elif(score >= 70):
        grade = 'C'
    elif(score >= 60):
        grade = 'D'
    else:
        grade = 'F'
        print('당신은', grade)
        return
    
    if(score % 10 >= 5):
        grade = grade + '+'
    
    print('당신은', grade)

# q3(90)

# q3 문제에서 시험점수의 기준은 사실 100점 만점이었습니다.
# 위 조건에 부합하도록 입력값에 대한 검증을 수행해주세요.


def validate(card):
    return card == '가위' or card == '바위' or card == '보'

def q4():
    """
    단판 가위바위보를 하는 프로그램을 구현해주세요.
    사용자로부터 userA와 userB의 패를 입력받으세요
    패 : 가위 | 바위 | 보
    userA와 userB 게임결과를 userA 기준에서 (승|무|패)를 출력해주세요.
    """
    userA = input('userA 가위! 바위! 보: ')
    if(not validate(userA)):
        print('잘못된 입력값 입니다.')
        return
    
    userB = input('userB 가위! 바위! 보: ')
    if(not validate(userB)):
        print('잘못된 입력값 입니다.')
        return

    # 빠른 리턴
    # 함수를 종료할 수 있는 조건일 때 코드블록을 수행한 이후 함수를 바로 종료시키면
    # 후속 로직의 복잡도가 내려간다.
    if(userA == userB):
        print('비겼다.')
        return
    
    if(userA == '가위' and userB == '바위'):
        print('졌습니다.')
        return

    if(userA == '바위' and userB == '보'):
        print('졌습니다.')
        return

    if(userA == '보' and userB == '가위'):
        print('졌습니다.')
        return
    
    print('이겼습니다.')

# q4()

def q5():
    """ 사용자가 결제한 금액만큼 메세지를 출력할 수 있는 프로그램을 구현합니다.

    메세지는 건당 5000원입니다.

    출력되는 메세지 양식은 아래와 같습니다.
    [id]: message (남은 결제 금액)

    결제금액은 사용자로부터 입력받습니다.

    id는 사용자로부터 입력받습니다.

    메세지를 출력하기 위한 비용이 부족하면
    '충전금액이 부족합니다.' 를 출력하고 프로그램을 종료합니다.

    사용자가 비속어를 사용하면
    '비속어는 사용할 수 없습니다.' 를 출력하고 입력창으로 돌아갑니다.
    이때 비용은 부과되지 않습니다.

    비속어 사전 : '강아지', '새'
    """
    id = input('id: ')
    balance = int(input('충전 금액: '))

    while(True):
        msg = input('msg: ')
        if(balance < 5000):
            print('잔액이 모자랍니다.')
            break;
        
        if('강아지' in msg or '새' in msg):
            print('비속어는 쓰실 수 없습니다.')
            continue

        balance -= 5000
        print(f'[{id}]: {msg} ({balance}원)')

        if(msg == 'exit'):
            break;

def valid(card):
    """
    인자로 전달받은 문자열이 '가위', '바위', '보' 집합의 요소인지 판단
    """
    return card == '가위' or card == '바위' or card == '보'

def q6() :
    """
    가위바위보를 하는 프로그램을 구현해주세요.
    사용자로부터 userA와 userB의 패를 입력받으세요
    패 : 가위 | 바위 | 보
    2선승 제도를 따를 것이며
    userA기준에서 승무패를 출력해주시면 됩니다.

    1. 가위바위보를 만든다
    2. 2선승 여부를 판단한다
    3. 승무패를 출력한다

    특정 조건에서 반복을 수행하는 while문을 사용해야한다.
    탈출 조건은 userA가 2승을 하거나 2패를 할 경우
    """
    
    while(True):
        # userA와 userB의 패를 사용자로부터 입력받기 -- presentation layer

        # q4()을 재사용가능한 함수형태로 바꿔보기, 함수명 : play_game  -- business layer
            # 입력계층에서 받은 userA와 userB의 패를 매개변수로 전달받아서
            # 가위바위보를 수행하고 게임결과(win, lose, semi) 를 반환하는 함수

        # play_game함수가 반환한 값으로 승, 무, 패 카운트 증가시키기  -- business layer

        # 만약 승 또는 패 카운트가 2보다 크거나 같아지면 
        # 승무패 결과를 출력하고  -- presentation layer

        # 프로그램을 종료하기

