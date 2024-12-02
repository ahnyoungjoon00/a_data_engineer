from abc import ABC, abstractmethod
from figure.Point import Point

class Figure(ABC):
    """
    추상클래스 (abstract class)
    구체화 되지 않은 클래스이기 때문에 인스턴스화를 할 수 없다.
    추상클래스를 상속한 뒤 오버라이드를 통해 추상메서드를 모두 구현(implement)한
    구현 클래스(concreate class) 를 만들어야 인스턴스화가 가능하다.
    """
    name=None
    
    @property
    @abstractmethod
    def name(self):
        pass

    # 자식클래스에서 추상메서드를 오버라이드를 하지 않을 경우
    # 에러를 발생시킨다.
    @abstractmethod
    def left_point(self):
        pass

    @abstractmethod
    def right_point(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass
    
    def _max_x(self, a:Point, b:Point):
        if(a.x >= b.x):
            return a
        return b

    def _min_x(self, a:Point, b:Point):
        if(a.x <= b.x):
            return a
        return b