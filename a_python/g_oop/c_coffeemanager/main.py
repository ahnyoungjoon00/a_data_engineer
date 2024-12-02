from typing import List
from Coffee import Coffee
from Menu import Menu
from Sales import Sales

if __name__ == '__main__':
    drinks:List[Coffee] = [
        Coffee('아메리카노', 10, 0, 3, 2000, 3000),
        Coffee('모카', 10, 0, 3, 3000, 4000),
        Coffee('라떼', 10, 0, 3, 4000, 5000),
    ]

    Menu(Sales(), drinks).main_menu()