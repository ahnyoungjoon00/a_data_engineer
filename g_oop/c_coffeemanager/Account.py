class Account:
    __instance = None
    __init = False

    # 인스턴스를 생성  
    # 메모리에 인스턴스의 데이터를 저장하기 위한 공간을 확보하고, 그 공간의 주소를 가지는 
    # 참조변수를 반환하는 함수
    def __new__(cls):
        print('new 호출')
        # cls : 클래스 객체
        # super() : Account 클래스의 부모클래스 인스턴스에 접근하는 함수
        if(cls.__instance == None):
            cls.__instance = super().__new__(cls)
        
        return cls.__instance

    # 인스턴스를 초기화
    # 인자로 인스턴스로 찾아가기 위한 주소를 담고 있는 참조변수를 받아서
    # 메모리상의 주소(인스턴스) 에 들어갈 데이터를 초기화
    def __init__(self):
        cls = type(self)
        if(not cls.__init):
            self.__balance = 100000 # 잔액
            self.__sales_volume = 0 # 매출
            self.__expenses = 0 # 지출
            cls.__init = True

    # 인스턴스를 생성하지 않고, 타입정보 만으로도 사용할 수 있는 메서드
    @classmethod
    def get_instance(cls):
        if(cls.__instance == None):
            return cls()
        return cls.__instance

    def regist_expenses(self, budget):
        if(self.balance > budget):
            self.__balance -= budget
            self.__expenses += budget
            return True
        return False
    
    def regist_sales(self, pay_price):
        self.__balance += pay_price
        self.__sales_volume += pay_price

    @property
    def balance(self):
        return self.__balance

    @property
    def sales_volume(self):
        return self.__sales_volume

    @property
    def expenses(self):
        return self.__expenses

