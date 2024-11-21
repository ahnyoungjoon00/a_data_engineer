from figure.Point import Point
from figure.Figure import Figure

class Rectangle(Figure):
    name = '사각형'

    def __init__(self, top:tuple[Point], bottom:tuple[Point]):
        # _ : 클래스외부에서 접근하면 안되는 변수를 나타내기 위한 관습
        # __와 다르게 파이썬이 변수명을 변경하지 않는다.
        # 보통 protected(상속계층에 있을 때만 접근) 접근제한을 나타내기 위해 표현
        self._top = top
        self._bottom = bottom

    # overrid
    # 부모클래스로부터 상속받은 기능을 재정의
    # 자식클래스에 알맞은 메서드로 변경 => 부모클래스에서 정의한 기능의 내용을 변경 X
    #                                 부모클래스에서 정의한 기능의 내용을 구현하기 위한 방식을 변경 o
    # 자식클래스가 부모로부터 상속받은 메서드를 오버라이드 했다면, 자식이 오버라이드한 메서드가 호출
    # 아니라면, 부모의 메서드가 호출
    def left_point(self):
        # 윗변의 왼쪽 좌표와 아랫변의 왼쪽 좌표중 더 x값이 작은 좌표
        left_top = self._min_x(*self._top)
        left_bottom = self._min_x(*self._bottom)
        return self._min_x(left_top, left_bottom)
    
    def right_point(self):
        right_top = self._max_x(*self._top)
        right_bottom = self._max_x(*self._bottom)
        return self._max_x(right_top, right_bottom)

    def calculate_area(self):
        point_a, point_b = self._bottom
        height = self._top[0].y - point_a.y
        return abs(point_a.x - point_b.x) * height