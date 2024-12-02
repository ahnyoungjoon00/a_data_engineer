from before.figure.Triangle import Triangle
from before.figure.Rectangle import Rectangle
from before.figure.Trapezoid import Trapezoid

from before.figure.Point import Point
# 해당 스크립트 파일이 진입점으로 사용될 때, 동작할 코드
if __name__ == "__main__" :
    triangle = Triangle(top = Point(5, 5), bottom =(Point(0), Point(5)))
    area = triangle.calculate_area()
    print("삼각형 넓이 :", area)
    print(f"왼쪽 {triangle.left_point()}", f"오른쪽 {triangle.right_point()}")
    print(Triangle.name)

    small_tri = Triangle(top = Point(5, 3), bottom =(Point(0), Point(5)))
    print("삼각형 넓이 :", small_tri.calculate_area())
    print(f"왼쪽 {triangle.left_point()}", f"오른쪽 {triangle.right_point()}")

    rectangle = Rectangle(top = (Point(0, 5), Point(5, 5)),
                          bottom = (Point(0), Point(5)))
    print(rectangle.name, rectangle.calculate_area())
    print(rectangle.name, rectangle.left_point())
    print(rectangle.name, rectangle.right_point())

    trapezoid = Trapezoid(top = (Point(3, 5), Point(8, 5)),
                          bottom = (Point(0), Point(10)))
    print(trapezoid.name, trapezoid.calculate_area())
    print(trapezoid.name, trapezoid.left_point())
    print(trapezoid.name, trapezoid.right_point())

    Triangle.name = "작은 삼각형"
    print(small_tri.name)
    print(triangle.name) # Triangle의 이름을 여기서 바꾸면 이 이후부터 전체가 바뀌게 되는거임


    print("====================================================")

    figure = [triangle, small_tri, rectangle, trapezoid]
    for e in figure :
        print(e.name, e.calculate_area())
        print(e.name, e.left_point())
        print(e.name, e.right_point())