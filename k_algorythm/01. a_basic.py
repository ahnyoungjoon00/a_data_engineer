# 함수 선언부

# 전역 선언부
katok = ["다현", "정연", "쯔위", "사나", "지효"]
# 메인 코드부
print(katok)

# 데이터 추가
# 1단계 : 빈 칸 확보
katok.append(None)
# 2단계 : 빈 칸 선언
katok[5] = "모모"
print(katok)

# 데이터 삽입 : 기존 요소간 앞에 신규 데이터 삽입
# 1단계 : 빈 칸 확보
katok.append(None)
# 2단계 : 한 칸씩 뒤로 이동(신규 데이터 자리부터 마지막까지)
katok[6] = katok[5]
katok[5] = None
print(katok)
katok[5] = katok[4]
katok[4] = None
print(katok)
katok[4] = katok[3]
katok[3] = None
print(katok)
# 3단계 : 3번 자리에 새 친구 넣기
katok[3] = "미나"
print(katok)

# 데이터 삭제 : 사나 이탈(=4번자리)
# 1단계 : 4등 지우기
katok[4] = None
print(katok)
# 2단계 : 5등부터 미지막 친구까지 앞으로 한 칸씩 이동
katok[4] = katok[5]
katok[5] = None
print(katok)
katok[5] = katok[6]
katok[6] = None
print(katok)
# 3단계 : 마지막 칸 삭제
del(katok[6])
print(katok)