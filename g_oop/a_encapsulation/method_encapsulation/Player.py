"""
객체의 자율성
Player 객체의 역할 : 연주
객체가 맡은 역할을 어떻게 수행할지에 대해
객체에게 전적으로 맡겨야한다.
"""

class Player:

    def __init__(self, instrument):
        self.__instrument = instrument

    def play(self):
        self.__prepare()
        self.__start()
        self.__ing()
        self.__end()
        self.__curtain_call()
    
    def __prepare(self):
        print(self.__instrument + '를 연주할 준비 중입니다.')

    def __start(self):
        print(self.__instrument + '를 연주할 시작합니다.')

    def __ing(self):
        print('연주중...')

    def __end(self):
        print(self.__instrument + '를 연주를 끝냅니다.')
    
    def __curtain_call(self):
        print('커튼콜이 울려퍼집니다.')