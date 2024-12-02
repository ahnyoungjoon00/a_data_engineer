import numpy as np

def valid(card) :
    return card == "가위" or card == "바위" or card == "보"

def play_game(userA, userB) :
        if userA == userB :
            return "semi"
        elif (userA == "가위" and userB == "보") or (userA == "바위" and userB == "가위") or (userA == "보" and userB == "바위") :
            return "win"
        else :
            return "lose"

def res_count(win, semi, lose, res) :
    match res :
        case "semi" :
            semi += 1
        case "win" :
            win += 1
        case "lose" :
            lose += 1
    return win, semi, lose

def q6() :
    """
    가위바위보를 하는 프로그램 구현
    userA, userB를 입력받으세요
    패 : 가위 | 바위 | 보
    3판 2선승 제도
    1. 가위바위보를 만든다
    2. 2선승 여부를 판단한다.
    3. 승무패를 출력한다.

    특정 조건에 반복을 수행하는 while문을 사용해야 함.
    탈출 조건은 userA가 2승 혹은 2패를 할때
    """
        # 입력계층 :사용자로부터 입력받기 -- persentation layer
        # q4()를 재사용가능한 함수 형태로 바꿔보기, 함수명 :play_game() -- business layer
            # 입력계층에서 받은 userA와 userB의 패를 매개변수로 전달받아서
            # 가위바위보를 수행하고 결과(win, lose, semi)를 반환하는 함수 
         
        # play_game()가 반환한 값을 승, 무, 패 카운트 -- business layer
        
        # 만약 승, 패 카운트가 2가 되면
        # 승무패 결과를 출력하고 -- presentation layer
         
        # 종료!   
    win, semi, lose = 0, 0, 0
    while(True) :
        userA = np.random.choice(["가위", "바위", "보"])
        if not valid(userA) :
            print("잘못된 입력값입니다.")
            return
        userB = np.random.choice(["가위", "바위", "보"])
        if not valid(userB) :
            print("잘못된 입력값입니다.")
            return
    # -----------------------------------
        res = play_game(userA, userB)
        win, semi, lose = res_count(win, semi, lose, res)

        if (win == 2) or (lose == 2) :
            break
    # -----------------------------------
    if (win == 2) :
        # print(f"승리! {win}승 | {semi}무 | {lose}패")
        return "승"
    elif (lose == 2) :
        # print(f"패배! {win}승 | {semi}무 | {lose}패")
        return "패"

# q6()
import time
score, count = 0, 0
while (-10 <= score <= 10) :
    result = q6()
    count += 1
    if result == "승" :
        score += 1
    else :
        score -= 1
    print(f"{count}회 진행... {score}편항")
    time.sleep(0.2)