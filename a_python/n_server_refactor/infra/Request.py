class Request :
    def __init__(self, param:dict) :
        self.__param = param
    
    @property
    def param(self):
        return self.__param