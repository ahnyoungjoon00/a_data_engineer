from before.figure.Point import Point
class Rectangle:
    name = '사각형'
    def __init__(self, top:tuple[Point], bottom:tuple[Point]):
        self.__top = top
        self.__bottom = bottom

    def left_point(self):
        # 윗변의 왼쪽 좌표와 아랫변의 왼쪽 좌표중 더 x값이 작은 좌표
        left_top = self._min_x(*self.__top)
        left_bottom = self._min_x(*self.__bottom)
        return self._min_x(left_top, left_bottom)
    
    def right_point(self):
        right_top = self._max_x(*self.__top)
        right_bottom = self._max_x(*self.__bottom)
        return self._max_x(right_top, right_bottom)
    
    def _max_x(self, a:Point, b:Point):
        if(a.x >= b.x):
            return a
        return b

    def _min_x(self, a:Point, b:Point):
        if(a.x <= b.x):
            return a
        return b

    def calculate_area(self):
        point_a, point_b = self.__bottom
        height = self.__top[0].y - point_a.y
        return abs(point_a.x - point_b.x) * height