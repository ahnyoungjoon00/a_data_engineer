from typing import List
from figure.Figure import Figure
from figure.Rectangle import Rectangle
from figure.Point import Point
from figure.Trapezoid import Trapezoid
from figure.Triangle import Triangle

if __name__ == '__main__':
    triangle = Triangle(top=Point(5,5), bottom=(Point(0), Point(5)))
    small_tri = Triangle(top=Point(5,3), bottom=(Point(0), Point(5)))
    rectangle = Rectangle(top=(Point(0,5), Point(5,5)), 
                         bottom=(Point(0), Point(5)))
    trapezoid = Trapezoid(top=(Point(3,5), Point(8,5)), 
                          bottom=(Point(0), Point(10)))

    print('======================================')
    # Figure타입으로 다루어질 수 있는 인스턴스만 저장해야하는 list
    figures:List[Figure] = [triangle, small_tri, rectangle, trapezoid]
    
    for e in figures:
        print(e.name, e.calculate_area())
        print(e.name, e.left_point())
        print(e.name, e.right_point())
