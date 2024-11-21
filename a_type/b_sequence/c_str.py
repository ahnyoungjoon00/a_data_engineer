"""
문자열 :  문자(1글자)의 배열
      : 문자를 요소로 가지는 불변시퀀스
"""

def str_read():
    msg = '몰랐죠? 사실 문자열도 시퀀스에요.'
    print('사실' in msg)
    print(max(msg), min(msg))
    print(msg[3])

    for e in msg:
        print(e)

str_read()