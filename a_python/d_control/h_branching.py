"""
반복문을 탈출할 키워드 : break
현재 싸이클을 탈출하게 만드는 키워드 : continue
"""

def study_break() :
    """
    특정 조건에서 반복문을 종료해야할 때
    사용자에게 입력받은 메세지를 출력하는 프로그램 구현
    메세지는 [id] : massage 형식
    id, massage는 사용자에게 입력받습니다.
    """
    id = input("id :")

    while (True) :
        massage = input("massage :")
        print(f"[{id}] : {massage}")
        if (massage == "exit") :
            break
    print("채팅종료")
study_break()

# ---------------------------------------------------------

def study_continue() :
    """
    1부터 10까지의 합계를 구하시오
    1. for문 사용
    2. 4의 배수는 합계를 구할 때 제외한다.
    """
    sum = 0
    for i in range(1, 11) :
        if i%4 == 0 :
            continue
        sum += i
    else :
        print(sum)
study_continue()