from before.figure.Point import Point

class Triangle :
    # 클래스 변수
    # 클래스로부터 생성된 모든 인스턴스들이 공유하는 변수
    name = "삼각형"

    # tuple(Point) 해석 : Point클래스의 인스턴스만 저장한 tuple이어야한다는 힌트
    def __init__(self, top:Point, bottom:tuple[Point]) :
        self.__top = top
        self.__bottom = bottom

    def left_point(self) :
        """
        가장 왼쪽 좌표
        """
        point_a, point_b = self.__bottom
        if (point_a.x <= point_b.x) :
            return point_a
        
        return point_b

    def right_point(self) :
        """
        가장 오른쪽 좌표
        """
        point_a, point_b = self.__bottom
        if (point_a.x >= point_b.x) :
            return point_a
        
        return point_b

    # 인스턴스 매서드
    # 인스턴스를 생성한 뒤 사용할 수 있는 매서드
    # 인스턴스의 주소를 참조하고 있는 reference 변수를 통해 사용 가능
    def calculate_area(self) :
        point_a, point_b = self.__bottom
        return abs((point_a.x - point_b.x) * (self.__top.y - point_a.y) / 2)