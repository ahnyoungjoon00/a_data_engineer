# 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

        
def read_data(start):
    current = start
    while (current.link != None):
        current = current.link
        print(current.data, end = ", ")
    print()



        



# 변수
memory=[]
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]
# 메인
node = Node()
node.data = dataArray[0]
print(node, dataArray[0])
head = node
print(head)
memory.append(node) # 생략해도 문제는 없음(안 중요!)

# {1} 데이터 노드 생성 및 연결
for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)
read_data(head)

# {2} 데이터 삽입
def insert_node(findData, insertData):
    global memory, head, current, pre
    # 유형 1 : 맨 앞에 삽입되는 경우
    if (head.data==findData):
        node = Node() # 1
        node.data = insertData
        node.link = head # 2
        head = node # 3
        memory.append(node)
        return
    current = head # page24, 1
    while(current.link != None):
        pre = current # page24, 2
        current = current.link
        if (current.data==findData):
            node = Node() # page24, 4 
            node.data=insertData # page24, 4
            node.link=current # page24, 4
            pre.link = node # page24, 5
            memory.append(node)
            return
    # 없는 노드 앞에 삽입(= 마지막에 추가해버림림)
    node= Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

insert_node("다현", "윈터") # 위치를 찾을 데이터, 삽입할 데이터
read_data(head)
insert_node("사나", "솔라") # 위치를 찾을 데이터, 삽입할 데이터
read_data(head)
insert_node("지젤", "닝닝") # 위치를 찾을 데이터, 삽입할 데이터
read_data(head)