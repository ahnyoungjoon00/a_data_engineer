"""
반복문

while(조건식) :
    조건식이 참일 때, 반복실행할 코드블록
"""
# while(True) : 무한루프
#     print("비상!!!")

def study_while_count() :
    """ '안녕 파이썬'을 다섯번 출력하는 while문 작성"""
    count = 0
    while (count < 5) :
        print("안녕 파이썬!")
        count += 1
    print("!!!!!!!!!!!완료!!!!!!!!!!!")

# study_while_count()
# --------------------------------------------------------

# def study_while(id, pw) :
#     """
#     사용자로부터 아이디와 비밀번호를 입력받아
#     인증정보가 일치하면 로그인 처리,
#     일치하지 않으면 다시 입력받도록하는 프로그램 구현
#     id : python
#     pw : 1111
#     """
#     if id == "python" and pw == "1111" :
#         print("로그인 되었습니다.")
#     else :
#         print("로그인에 실패했습니다.")

# study_while("python", "1111")
# study_while("java", "1111")
# study_while("python", "2222")

# --------------------------------------------------------
# def study_while(id, pw) :
#     """
#     사용자로부터 아이디와 비밀번호를 입력받아
#     인증정보가 일치하면 로그인 처리,
#     일치하지 않으면 다시 입력받도록하는 프로그램 구현
#     id : python
#     pw : 1111
#     """
#     while not(str(id) == "python" and str(pw) == "1111") :
#         print("로그인에 실패했습니다.")
#         return
#     print("로그인 되었습니다.")

# study_while("python", "1111")
# study_while("java", "1111")
# study_while("python", "2222")

# --------------------------------------------------------

def study_while() :
    # stored_id = 'python'
    # stored_password = '1111'
    # try_cnt = 0
    user = "anonymous"
    count = 0
    while (user == "anonymous") :
        id = input("id : ")
        pw = input("pw : ")

        if (id == "python") and (pw == "1111") :
            print("로그인")
        else :
            count += 1
            print(f"{count}/5회 로그인 실패,")
        
        if (count >= 5) :
            print("5회 로그인 실패로 권한이 막혔습니다.,")
            user = "blocked"
study_while()