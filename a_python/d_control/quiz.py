# def q1(TF) :
#     """
#     매개변수로 계란의 유무를 입력 받고,
#     개발자가 사올 우유의 개수를 출력해주는 코드 작성
#     """
#     if TF == True :
#         print("우유 6팩 구매")
#     else :
#         print("우유 1개 구매")
# q1(1)


# def q2(egg) :
#     """
#     매개변수로 계란의 유무를 입력 받고,
#     개발자가 사올 우유의 개수를 출력해주는 코드 작성
#     """
#     if egg >= 2 :
#         print("우유 6개 구매")
#     else :
#         print("우유 1개 구매")

# import time
# for i in range(1, 10) :
#     q2(i)
#     time.sleep(0.5)

def q1(hasEgg) :
    """
    매개변수로 계란의 유무를 입력 받고,
    개발자가 사올 우유의 개수를 출력해주는 코드 작성
    """
    milkCnt = 1
    if (hasEgg) :
        milkCnt = 6

    print(f"우유 {milkCnt}개 구매")
q1(False)

#----------------------------------------------------------------------------------------------------------------------------------

# def q2(number) :
#     """
#     매개변수로 전달된 숫자가, 양수인지, 음수인지, 0인지 판단하는 코드를 작성하시오
#     """
#     if number == 0 :
#         print("0")
#     elif number > 0 :
#         print("양수")
#     else : 
#         print("음수")

# import time
# for i in range(-3, 4) :
#     q2(i)
#     time.sleep(0.5)

def q2(number) :
    if number > 0 :
        print("양수")
    else :
        if number == 0 :
            print("0")
        else :
            print("음수")

import time
for i in range(-3, 4) :
    q2(i)
    time.sleep(0.5)

#----------------------------------------------------------------------------------------------------------------------------------

# def q3(score) :
#     """ 매개변수로 점수를 전달 받아 등급을 출력하세요
# 	90점 이상이면 A
# 	80점 이상 90점 미만이면 B
# 	70점 이상 80점 미만이면 C
# 	60점 이상 70점 미만이면 D
# 	60점 미만이면 F 로 등급입니다.

#     만약 점수의 1의 자리가 5이상이라면
#     + 등급을 추가로 부여해주세요.
#     ex) 90점 : A
#         95점 : A+
#     """
#     if score >= 90 :
#         return "A"
#     elif score >= 80 :
#         return "B"
#     elif score >= 70 :
#         return "C"
#     elif score >= 60 :
#         return "D"
#     else :
#         return "F"

# def q3_1(score) :
#         grade = q3(score)
#         if score%10 >= 5 and grade != "F":
#             print(grade + "+등급")
#         else :
#             print(grade + "등급")
            
# q3_1(87)

def q3(score) :
    """ 매개변수로 점수를 전달 받아 등급을 출력하세요
	90점 이상이면 A
	80점 이상 90점 미만이면 B
	70점 이상 80점 미만이면 C
	60점 이상 70점 미만이면 D
	60점 미만이면 F 로 등급입니다.

    만약 점수의 1의 자리가 5이상이라면
    + 등급을 추가로 부여해주세요.
    ex) 90점 : A
        95점 : A+
    """
    if score >= 90 :
        grade = "A"
    elif score >= 80 :
        grade = "B"
    elif score >= 70 :
        grade = "C"
    elif score >= 60 :
        grade = "D"
    else :
        grade = "F"
        print("F등급")
        return

    if score%10 >= 5 :
        print(grade + "+등급")
    else :
        print(grade + "등급")

#----------------------------------------------------------------------------------------------------------------------------------

# def q4(userA, userB) :
#     """
#     단판 가위바위보를 하는 프로그램을 구현해주세요.
#     사용자로부터 userA와 userB의 패를 입력받으세요
#     패 : 가위 | 바위 | 보
#     userA와 userB 게임결과 (승|무|패)를 출력해주세요.
#     """
#     if not(userA in ["가위", "바위", "보"] or userB in ["가위", "바위", "보"]) :
#         print("잘못된 입력값입니다.")
#         return
#     if userA == userB :
#         print("무")
#         return
#     elif (userA == "가위" and userB == "보") or (userA == "바위" and userB == "가위") or (userA == "보" and userB == "바위") :
#         print("승")
#         return
#     else :
#         print("패")

# userA = input("userA :")
# userB = input("userB :")
# q4(userA, userB)

# import time
# for A in ["가위", "바위", "보"] :
#     for B in ["가위", "바위", "보"] :
#         print("userA :", A, "userB :", B)
#         q4(A, B)
#         time.sleep(0.5)


def validate(card) :
    return card == "가위" or card == "바위" or card == "보"

def q4(userA, userB) :
    userA = input()
    if not validate(userA) :
        print("잘못된 입력값입니다.")
        return
    userB = input()
    if not validate(userB) :
        print("잘못된 입력값입니다.")
        return
    # --------------------------------------------------
    if userA == userB :
        print("무")
        return
    
    if (userA == "가위" and userB == "보") :
        print("승")
        return
    if (userA == "바위" and userB == "가위") :
        print("승")
        return
    if (userA == "보" and userB == "바위") :
        print("승")
        return
    
    print("패")

q4("가위", "바위")

# -----------------------------------------------

def q5() :
    """
    사용자가 결제한 금액만큼 메세지를 출력할 수 있는 프로그램 구현
    메세지는 건당 5000원입니다.

    1. 출력 메세지 양식은 아래와 같다.
    [id] : massage (남은 결제 금액)
    결제금액, id 는 사용자로부터 입력받는다.
    
    2. 메세지 출력하기 위한 비용이 부족하면
    '충전금액이 부족합니다.'를 출력하고 프로그램 종료

    3. 사용자가 비속어 사용하면
    '비속어는 사용할 수 없습니다.'를 출력하고 입력창으로 돌아갑니다.
    이때, 비용은 부과되지 않습니다.
    비속어 사전 : '강아지', '새'
    """

    id = input("id :")
    money = int(input("충전금액 :"))

    while (True) :
        if money < 5000 :
            print("충전금액이 부족합니다.")
            break

        massage = input("massage :")
        if '새' in massage or '강아지' in massage :
            print("비속어는 사용할 수 없습니다.")
            continue
        else :
            money -= 5000
            print(f"[{id}] : {massage} ({money}원)")

q5()

# ----------------------------------------------------------------------------------

# def valid(card) :
#     return card == "가위" or card == "바위" or card == "보"

# def q6() :
#     """
#     가위바위보를 하는 프로그램 구현
#     userA, userB를 입력받으세요
#     패 : 가위 | 바위 | 보
#     3판 2선승 제도
#     userA기준에서 승무패를 출력
#     """    
#     event = 0
#     win, semi, lose = 0, 0, 0
#     while (event < 3) :
#         userA = input("A 패 입력 : ")
#         if not valid(userA) :
#             print("잘못된 입력값입니다.")
#             return
        
#         userB = input("B 패 입력 : ")
#         if not valid(userB) :
#             print("잘못된 입력값입니다.")
#             return

#         event += 1
#         if userA == userB :
#             semi += 1
#         elif (userA == "가위" and userB == "보") or (userA == "바위" and userB == "가위") or (userA == "보" and userB == "바위") :
#             win += 1
#         else :
#             lose += 1

#         if (win == 2) or (lose == 2) :
#             break
        
#     if (win-lose) > 0 :
#         print(f"승리! {win}승 | {semi}무 | {lose}패")
#     elif (win-lose) < 0 :
#         print(f"패배! {win}승 | {semi}무 | {lose}패")
#     else :
#         print(f"무승부! {win}승 | {semi}무 | {lose}패")
# q6()

# ----------------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------

# import numpy as np
# def q6() :
#     """
#     가위바위보를 하는 프로그램 구현
#     userA, userB를 입력받으세요
#     패 : 가위 | 바위 | 보
#     3판 2선승 제도
#     1. 가위바위보를 만든다
#     2. 2선승 여부를 판단한다.
#     3. 승무패를 출력한다.

#     특정 조건에 반복을 수행하는 while문을 사용해야 함.
#     탈출 조건은 userA가 2승 혹은 2패를 할때
#     """
#         # 입력계층 :사용자로부터 입력받기 -- persentation layer
#         # q4()를 재사용가능한 함수 형태로 바꿔보기, 함수명 :play_game() -- business layer
#             # 입력계층에서 받은 userA와 userB의 패를 매개변수로 전달받아서
#             # 가위바위보를 수행하고 결과(win, lose, semi)를 반환하는 함수 
         
#         # play_game()가 반환한 값을 승, 무, 패 카운트 -- business layer
        
#         # 만약 승, 패 카운트가 2가 되면
#         # 승무패 결과를 출력하고 -- presentation layer
         
#         # 종료!   
#     win, semi, lose = 0, 0, 0
#     while(True) :
#         userA = np.random.choice(["가위", "바위", "보"])
#         if not valid(userA) :
#             print("잘못된 입력값입니다.")
#             return
#         userB = np.random.choice(["가위", "바위", "보"])
#         if not valid(userB) :
#             print("잘못된 입력값입니다.")
#             return
#     # -----------------------------------
#         res = play_game(userA, userB)
#         win, semi, lose = res_count(win, semi, lose, res)

#         if (win == 2) or (lose == 2) :
#             break
#     # -----------------------------------
#     if (win == 2) :
#         print(f"승리! {win}승 | {semi}무 | {lose}패")
#     elif (lose == 2) :
#         print(f"패배! {win}승 | {semi}무 | {lose}패")

# q6()

# ---------------------------------------------------------------------------

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
        userA = input("A 패 입력 : ")
        if not valid(userA) :
            print("잘못된 입력값입니다.")
            return
        userB = input("B 패 입력 : ")
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
        print(f"승리! {win}승 | {semi}무 | {lose}패")
    elif (lose == 2) :
        print(f"패배! {win}승 | {semi}무 | {lose}패")

q6()