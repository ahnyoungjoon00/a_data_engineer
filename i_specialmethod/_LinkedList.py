class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # 다음 노드의 주소를 저장

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

        prev = self.__head

        while(prev.next):
            prev = prev.next
        
        prev.next = node
        self.__length += 1

    def get(self, idx):
        if(idx < 0 or idx >= self.__length):
            raise IndexError(f'length : {self.__length}')

        if(idx == 0):
            return self.__head.data

        prev = self.__head
        for _ in range(0, idx):
            prev = prev.next
        
        return prev.data

    def __str__(self):
        node = self.__head
        if(not node):
            return '[empty list]'
        
        res = '['
        while(node.next):
            res += str(node.data) + ', '
            node = node.next
        
        res += str(node.data)
        res += ']'

        return res

    # list의 가장 앞에 노드를 추가
    def prepend(self, data):
        pass

    # 인자로 전달받은 i에 노드를 추가
    def insert(self, i, data):
        pass

    def pop(self):
        """ 가장 뒤에 있는 요소를 반환하고 삭제
        """
        pass
    
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
            

        
                

        


