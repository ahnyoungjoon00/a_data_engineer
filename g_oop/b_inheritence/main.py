from before.figure.Triangle import Triangle
from before.figure.Point import Point
from before.figure.Rectangle import Rectangle
from before.figure.Trapezoid import Trapezoid

# 해당 스크립트 파일이 진입점으로 사용될 때 동작할 코드
if __name__ == '__main__':
    triangle = Triangle(top=Point(5,5), bottom=(Point(0), Point(5)))
    area = triangle.calculate_area()
    print(triangle.name, area)
    print(triangle.name, triangle.left_point())
    print(triangle.name, triangle.right_point())

    small_tri = Triangle(top=Point(5,3), bottom=(Point(0), Point(5)))
    print(small_tri.name, small_tri.calculate_area())
    print(small_tri.name, small_tri.left_point())
    print(small_tri.name, small_tri.right_point())

    rectangle = Rectangle(top=(Point(0,5), Point(5,5)), 
                          bottom=(Point(0), Point(5)))
    print(rectangle.name, rectangle.calculate_area())
    print(rectangle.name, rectangle.left_point())
    print(rectangle.name, rectangle.right_point())

    trapezoid = Trapezoid(top=(Point(3,5), Point(8,5)), 
                          bottom=(Point(0), Point(10)))
    print(trapezoid.name, trapezoid.calculate_area())
    print(trapezoid.name, trapezoid.left_point())
    print(trapezoid.name, trapezoid.right_point())

    print('======================================')
    figures = [triangle, small_tri, rectangle, trapezoid]
    for e in figures:
        print(e.name, e.calculate_area())
        print(e.name, e.left_point())
        print(e.name, e.right_point())

    # Triangle.name = '작은 삼각형'
    # print(small_tri.name)
    # print(triangle.name)