class Point :
    def __init__(self, x, y = 0) :
        self.__x = x
        self.__y = y

    @property
    def x(self) :
        return self.__x
    
    @property
    def y(self) :
        return self.__y
    
    def __str__(self):
        return f'({self.__x}, {self.__y})'
    

    