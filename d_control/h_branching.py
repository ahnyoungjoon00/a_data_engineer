"""
반복문을 탈출할 키워드: break
현재 사이클을 탈출하게 만들 키워드: continue
"""

def study_break():
    """ 특정 조건에서 반복문을 종료해야할 때
    사용자에게 입력받은 메세지를 출력하는 프로그램을 구현하세요.
    메세지는 [id]:message
    형식으로 출력합니다.
    id, message는 사용자에게 입력받습니다.
    """
    id = input('id: ')

    while(True):
        message = input('message: ')
        if('바보' in message):
            print('금칙어는 쓸 수 없습니다.')
            continue
        print(f'[{id}]: {message}')

        if(message == 'exit'):
            break
    
    print('채팅앱을 떠나셨습니다.')


def study_continue():
    """ 1부터 10까지 정수들의 합계를 구하시오.
        1. for문을 사용한다.
        2. 4의 배수는 합계를 구할 때 제외한다.(제외 가능)
    """
    sum = 0
    for i in range(1, 11):
        if(i % 4 == 0):
            continue
        sum = sum + i
    else:
        print(sum)

