from overrides import overrides
from figure.Point import Point
from figure.Figure import Figure

class Triangle(Figure):
    # 클래스 변수
    # 클래스로부터 생성된 모든 인스턴스들이 공유하는 변수
    name = '삼각형'

    # tuple[Point] : Point클래스의 인스턴스만 저장한 tuple이어야 한다는 힌트
    def __init__(self, top:Point, bottom:tuple[Point]):
        self.__top = top
        self.__bottom = bottom

    # @overrides : 실행시점에, 해당 메서드가 부모클래스에 존재하는 메서드인지 체크
    # 부모클래스의 메서드와 선언부가 동일한지 체크
    @overrides
    def left_point(self):
        """
        가장 왼쪽 좌표
        """
        left_bottom = self._min_x(*self.__bottom)
        return self._min_x(left_bottom, self.__top)
    
    @overrides
    def right_point(self):
        """
        가장 오른쪽 좌표
        """
        right_bottom = self._max_x(*self.__bottom)
        return self._max_x(right_bottom, self.__top)

    # 인스턴스 메서드
    # 인스턴스를 생성한 뒤 사용할 수 있는 메서드
    # 인스턴스의 주소를 참조하고 있는 reference 변수를 통해 사용할 수 있다.
    @overrides
    def calculate_area(self):
        point_a, point_b = self.__bottom
        return abs(point_a.x - point_b.x) * (self.__top.y - point_a.y) / 2

    def info(self):
        print('삼각형입니다.')