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
