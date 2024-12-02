class Animal:
    # 클래스변수
    species = 'Animal'

    def __new__(cls, *args, **kwargs):
        """
        인스턴스를 생성하는 메서드
        """
        return super().___new__(cls)

    def __init__(self, name, age, life):
        """
        인스턴스를 초기화하는 메서드
        """
        self.__name = name
        self.__age = age
        self.__life = life

    @classmethod
    def create(cls, name, age, life):
        """
        타입정보로 사용할 수 있는 메서드
        클래스 맥락에서 사용되는 메서드
        """
        return Animal(name, age, life)
    
    @staticmethod
    def pretty_print(msg:str):
        """
        타입정보로 사용할 수 있는 메서드
        클래스 맥락에서 독립적인 기능
        """
        print(f'****{msg}****')
        """
        Class를 인스턴스에 담아서 
        animal = Animal()
        animal.pretty_print(msg) 형태로 쓰거나
        Animal().pretty_print(msg) 형태로 쓰는데

        staticmethod로 정의하여 사용 시,
        Animal.pretty_print(msg)로 바로 사용 가능
        """

    # instance method
    def cal_human_age(self):
        return self.__age / self.__life * 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, value):
        self.__life = value

    # instance method
    """
    이렇게 써놓으면 호출할때, 
    Class.get_name(), Class.set_name("Adam") 이런식으로 메소드를 명확히 다 써줘야함 
    @property, @setter 데코레이터로 설정해놓으면 속성처럼
    Class.name, Class.name = "Adam" 형태로 사용이 가능함
    """
    # def cal_human_age(self) :
    #     return self.__age / self.__life * 100

    # def get_name(self):
    #     return self.name

    # def set_name(self, value):
    #     self.name = value

    # def get_age(self):
    #     return self.age

    # def set_age(self, value):
    #     self.age = value

    # def get_life(self):
    #     return self.life

    # def set_life(self, value):
    #     self.life = value
