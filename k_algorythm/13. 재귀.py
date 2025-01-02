import random
# 함수
def openbox():
    global count
    print("상자 열기")
    count -= 1
    if (count==0):
        print("*****선물 넣기*****")
        return
    openbox()
    print("상자 닫기")

# # 메인
count = 10
openbox()

# print("상자 열기")
#     print("상자 열기")
#         print("상자 열기")
#             print("상자 열기")
#                 print("상자 열기")
#                     print("상자 열기")
#                         print("상자 열기")
#                             print("상자 열기")
#                                 print("상자 열기")
#                                     print("상자 열기")
#                                         print("*****선물 넣기*****")
#                                     print("상자 닫기")
#                                 print("상자 닫기")
#                             print("상자 닫기")
#                         print("상자 닫기")
#                     print("상자 닫기")
#                 print("상자 닫기")
#             print("상자 닫기")
#         print("상자 닫기")
#     print("상자 닫기")
# print("상자 닫기")