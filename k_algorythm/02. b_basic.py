class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2
node3 = Node()
node3.data = "사나"
node2.link = node3
node4 = Node()
node4.data = "모모"
node3.link = node4
node5 = Node()
node5.data = "나연"
node4.link = node5

print(node1.data, end=" ")
print(node2.data, end=" ")
print(node3.data, end=" ")
print(node4.data, end=" ")
print(node5.data, end=" ")
print("\n==================================")

print(node1.data, end=" ")
print(node1.link.data, end=" ")
print(node1.link.link.data, end=" ")
print(node1.link.link.link.data, end=" ")
print(node1.link.link.link.link.data, end=" ")
print("\n==================================")

# 데이터 삽입
# 1단계 : 새 노드 준비
newNode = Node()
newNode.data = "카리나"
# 2단계 : 노드 링크를 삽입 위치의 링크로 지정
newNode.link = node2.link
# 3단계 : 기존 데이터의 링크를 새로운 데이터로 지정
node2.link = newNode

print(node1.data, end=" ")
print(node1.link.data, end=" ")
print(node1.link.link.data, end=" ")
print(node1.link.link.link.data, end=" ")
print(node1.link.link.link.link.data, end=" ")
print(node1.link.link.link.link.link.data, end=" ")
print("\n==================================")

# 데이터 삭제
# 1단계 : 삭제 대상 링크 끊어서 이전 데이터랑 잇기 
node3.link = node4.link
del(node3)

print(node1.data, end=" ")
print(node1.link.data, end=" ")
print(node1.link.link.data, end=" ")
print(node1.link.link.link.data, end=" ")
print(node1.link.link.link.link.data, end=" ")
print("\n==================================")