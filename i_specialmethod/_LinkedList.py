class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None # 다음 노드의 주소를 저장

# 위와 동일한 역할을 그냥함수로 구성
# def node(data) :
#     data = data
#     prev = None
#     next = None
#     return prev, data, next

class LinkedList:
    """
    duck typing : 만약 어떤 새가 오리처럼 걷고, 헤엄치고, 
    소리내면 그 새는 오리라고 볼 수 있다.
    오리타입을 상속받지 않더라도, 오리타입에 선언된 기능을 구현하고 있다면
    해당 클래스는 오리탑으로 다룰 수 있는 것으로 간주한다.
    """
    def __init__(self):
        self.__head = None # 첫번째 노드의 주소를 저장
        self.__length = 0  # 리스트의 길이


    def append(self, data):
        node = Node(data)

        if(self.__head == None):
            self.__head = node
            self.__length += 1
            return
        else :
            current = self.__head
            while(current.next):
                current = current.next
            current.next = node
            node.prev = current
            node.next = None
            self.__length += 1

    def get(self, idx):
        if(idx < 0 or idx >= self.__length):
            raise IndexError(f'length : {self.__length}, {idx}는 유효하지 않은 index입니다.')

        if(idx == 0):
            return self.__head.data

        prev = self.__head
        for _ in range(0, idx):
            prev = prev.next
        return prev.data

    def __str__(self):
        node = self.__head
        if(not node):
            return '[empty list!!]'
        
        res = '['
        while(node.next):
            res += str(node.data) + ', '
            node = node.next
        
        res += str(node.data)
        res += ']'
        return res

    # list의 가장 앞에 노드를 추가
    def prepend(self, data):
        node = Node(data)

        self.__length += 1
        if (self.__head == None) :
            # node.prev = None
            self.__head = node
            # node.next = None
        else :
            self.__head.prev = node
            node.next = self.__head
            self.__head = node
            # self.__head.prev = None

    # 인자로 전달받은 i에 노드를 추가
    def insert(self, idx, data):
        node = Node(data)
        if(idx < 0 or idx >= self.__length):
            raise IndexError(f'length : {self.__length}')
        if(idx == 0):
            node.prepend()

    def pop(self):
        """ 
        가장 뒤에 있는 요소를 반환하고 삭제
        """
        if(self.__head == None):
            print("빈 리스트 입니다.")
            return
        else :
            current = self.__head
            while(current.next):
                current = current.next
            current = self.__head
            current.prev = None
            current.next = None
            current = self.__head.prev
            # self.__length -= 1

    
    # 매개변수로 전달받은 data를 삭제하고 성공여부를 True/False 로 반환
    def remove(self, data):
        node = self.__head
        if(node.data == data):
            self.__head = node.next
            self.__length -= 1
            return True
        
        while(node.next):
            current = node.next
            if(current.data == data):
                node.next = current.next
                self.__length -= 1
                return True
            
            node = current
        
        return False
    
    def __iter__(self):
        return LinkedList.Iterator(self.__head)
    
    class Iterator:
        """
        제어반전 : 
        우리가 작성한 코드의 호출을 외부에 맡기는 것
        """
        def __init__(self, node):
            self.__node = node
            self.__call_cnt = 1

        def __iter__(self):
            return self

        def __next__(self):
            if(self.__node == None):
                #print('이제 멈춥니다')
                raise StopIteration
            
            print(f'{self.__call_cnt}번째 호출입니다.')

            data = self.__node.data
            self.__node = self.__node.next
            self.__call_cnt += 1
            return data
            

        
                

        


