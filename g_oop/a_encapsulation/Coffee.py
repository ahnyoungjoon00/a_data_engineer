"""
1. 추상화
프로그램에서 필요로 하는 공통적인 속성을 추출하고, 불필요한 것은 제거하는 것
기능을 정한다 => 추상화를 한다. (Class)

2. 캡슐화
클래스 내부의 인스턴스변수에 클래스 외부에서 직접 접근하는 것을 막는 것.
인스턴스 변수 이름 앞에 __ 를 붙여 외부에서 직접 접근을 막고
getter/setter 메서드를 통해서만 접근하도록 제한

접근에 대한 권한관리
getter/setter : 읽고 쓰기
getter : 읽기

클래스 : 속성 + 기능(메서드),
메서드 : 클래스에 포함된 함수

self : 인스턴스의 주소
인스턴스 : 클래스를 바탕으로 생성된 객체
moca = Coffee('모카',10,4000)

__init__ : 초기화 함수

생성자 : 클래스명(매개변수부) => __init__ 함수를 호출
"""
class Coffee:
    def __init__(self, name, stock, price):
        #__ : 이 속성은 외부에서 접근하지 않아야 합니다.
        print('init의 self: ', self)

        # 속성, attribute
        # instance 변수
        # instance 변수앞에 __를 붙이면 외부에서 직접 접근을 금지
        self.__name = name
        self.__stock = stock
        self.__price = price
    
    # getter
    def get_name(self):
        return self.__name
    
    # setter
    def set_name(self, name):
        if(not name): # str은 공백문자열이면 False
            print('잘못된 이름입니다.')
            return
        self.__name = name

    def get_price(self):
        return self.__price
    
    # 데코레이터 함수위에 선언해 함수에 특수한 기능을 추가해주는 기능
    @property
    def stock(self):
        print('stock getter')
        return self.__stock
    
    @stock.setter
    def stock(self, stock):
        print('stock setter')
        self.__stock = stock

    def check_self_id(self):
        print(id(self))

    def __str__(self):
        return f"""
        self.name : {self.__name}
        self.stock : {self.__stock}
        self.price : {self.__price}
        """

moca = Coffee('모카', 10, 4000)
latte = Coffee('라떼', 10, 5000)

moca.set_name('')
print(moca.get_name())
print(moca.get_price())

moca.stock = 999
print(moca.stock)

latte.check_self_id()
print(id(latte))

moca.check_self_id()
print(id(moca))

print(type(moca))

#print(latte)