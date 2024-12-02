from figure.Point import Point
from figure.Rectangle import Rectangle

class Trapezoid(Rectangle):
    """
    상속 :
    부모클래스의 타입(속성, 기능)을 물려받는 것.
    """
    name = '사다리꼴'
    def __init__(self, top:tuple[Point], bottom:tuple[Point]):
        # super() : 부모인스턴스에 접근
        # 부모인스턴스의 속성과 기능은 자식인스턴스를 통해 접근이 가능하다.
        super().__init__(top, bottom)

    def calculate_area(self):
        top_size = self.__cal_side_size(*self._top)
        bottom_size = self.__cal_side_size(*self._bottom)
        height = self._top[0].y - self._bottom[0].y
        return (top_size + bottom_size) * height / 2

    def __cal_side_size(self, a:Point, b:Point):
        return abs(a.x - b.x)