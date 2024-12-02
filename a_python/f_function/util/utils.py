def calculate_hypotenuse(base, height):
    """밑변의 길이가 a, 높이가 b인 직각 삼각형의 빗변의 길이를 구하시오."""
    square = base ** 2 + height ** 2
    print(square ** 0.5)
    return square ** 0.5
# calculate_hypotenuse(5, 7)