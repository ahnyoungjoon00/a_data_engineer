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

newNode = Node()
def read_data(start):
    current = start
    while (current.link != None):
        current = current.link
        print(current.data, end = ", ")
    print()
# read_data(node1)

def add_data(data):
    newNode = Node()
    newNode.data= data
    current = node1
    while (current.link != None):
        current = current.link
        print(current.data, end = ", ")
    current.link = newNode
    print(current.link.data, end = " ")
add_data("채영")