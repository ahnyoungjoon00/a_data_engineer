## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, current, pre
    # Case 1 : 머리 앞에 삽입 (다현, 화사)
    if (head.data == findData) : # 0
        node = Node() # 1
        node.data = insertData
        node.link = head # 2
        head = node # 3
        memory.append(node)  # 안 중요! (생략 가능)
        return
    # Case 2 : 중간 노드 앞에 삽입 (사나, 솔라)
    current = head #1
    while (current.link != None) : # 끝이 아닌동안!
        pre = current # 2
        current = current.link # 2
        if (current.data == findData) :
            node = Node() # 4
            node.data = insertData # 4
            node.link = current # 4
            pre.link = node # 5
            memory.append(node)  # 안 중요! (생략 가능)
            return
    # Case 3 : 없는 노드 앞에 삽입(=마지막에 추가) (재남, 문별)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)  # 안 중요! (생략 가능)
    return

def deleteNode(deleteData):
    global memory, head, current, pre
    # 유형 1 : 머리를 삭제할 때 (다현 삭제)
    if(head.data==deleteData):
        current=head
        head=head.link
        del(current)
        return
    
    # 유형 2 : 중간을 삭제할때(쯔위)
    current=head #1
    while(current.link!= None):
        pre = current #2
        current = current.link #2
        if(current.data==deleteData):
            pre.link = current.link #4
            del(current)
            return
    # 유형 3 : 없는 노드 삭제할때
    return
    
def searchNode(findData):
    global memory, head, current, pre
    current=head
    if(head.data==findData):
        return current
    while (current.link != None):
        current = current.link
        if(current.data==findData):
            return current
    return Node()
## 변수
memory = [] # 안 중요! (노드가 저장될 공간)
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효'] # 여러분 데이터~ 500,000...
## 메인

## (1) 연결 리스트 생성
# (1-1) 첫 노드 생성
node = Node()
node.data = dataArray[0]
head = node
memory.append(node) # 안 중요! (생략 가능)

# (1-2) 그외 노드 생성
for data in dataArray[1:] : # ['정연', '쯔위', ...
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)  # 안 중요! (생략 가능)




print("============================================================================================")
printNodes(head)
print("============================================================================================")
## (2) 데이터 삽입
insertNode('다현', '화사') # 찾을데이터, 삽입데이터
printNodes(head)
insertNode('사나', '솔라') # 찾을데이터, 삽입데이터
printNodes(head)
insertNode('재남', '문별') # 찾을데이터, 삽입데이터
printNodes(head)
print("============================================================================================")
## (3) 데이터 삭제
deleteNode('화사')
printNodes(head)
deleteNode('쯔위')
printNodes(head)
deleteNode('재남')
printNodes(head)
print("============================================================================================")
## (4) 데이터 검색
fNode = searchNode("사나")
print(f"{fNode.data}의 뮤비 실행")