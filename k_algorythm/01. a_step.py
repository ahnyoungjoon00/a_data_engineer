# # 함수 선언부
def add_data(friend):
    # 1단계 : 빈 칸 확보
    katok.append(None)
    # 마지막 자리에 친구 넣기
    klen = len(katok)
    katok[klen-1] = friend

def insert_data(position, friend):
    # 1단계 : 빈 칸 확보
    katok.append(None)
    # 2단계 : 한 칸씩 뒤로 이동
    for i in range(len(katok)-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    # 3단계 : 데이터 삽입
    katok[position] = friend

def delete_data(position):
    # 1단계 : 지우기
    katok[position] = None
    # 2단계 : 한 칸씩 앞으로 당기기
    klen = len(katok)
    for i in range(position+1, klen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[klen-1])


# 전역 선언부
katok = []
select = -1
# 메인 코드부
if __name__ == "__main__":
    while (select!=4):
        select = int(input("선택지 입력 1.추가, 2.삽입, 3.삭제, 4.종료 => "))
        if select==1:
            data = input("추가할 데이터 :")
            add_data(data)
            print(katok)
        elif select==2:
            position = int(input("삽입 위치 :"))
            data = input("삽입할 데이터 :")
            insert_data(position, data)
            print(katok)
        elif select==3:
            position = int(input("삭제할 위치 :"))
            delete_data(position)
            print(katok)
        elif select==4:
            print(katok)
            break
        else :
            print("잘못된 입력입니다.")




















# add_data("다현")
# add_data("정연")
# add_data("쯔위")
# add_data("사나")
# add_data("지효")
# print(katok)
# insert_data(3, "나연")
# print(katok)
# delete_data(4)
# print(katok)



# 데이터 추가
# 1단계 : 빈 칸 확보
# 2단계 : 빈 칸 선언
# def add_data(data):
#     katok.append(None)
#     katok[-1] = data

# 데이터 삽입 : 기존 요소간 앞에 신규 데이터 삽입
# 1단계 : 빈 칸 확보
# 2단계 : 한 칸씩 뒤로 이동(신규 데이터 자리부터 마지막까지)
# 3단계 : 3번 자리에 새 친구 넣기
# def insert_data(position, data):
#     for i in range(len(katok), position, -1):
#         katok[i] = katok[i-1]
#         katok[i-1] = None
#     katok[position] = data

# 데이터 삭제 : 사나 이탈(=4번자리)
# 1단계 : 4등 지우기
# 2단계 : 5등부터 미지막 친구까지 앞으로 한 칸씩 이동
# 3단계 : 마지막 칸 삭제
# def delete_data(position):
#     katok[position] = None
#     for i in range(position+1, len(katok)):
#         katok[i-1] = katok[i]
#         katok[i] = None
#     del katok[len(katok)-1]