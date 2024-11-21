from NaverAPI import NaverAPI
from error.errors import *
import traceback

if __name__ == '__main__':
    try:
        api = NaverAPI(3)
        api.connect()
    except IllegalPropertyError as e:
        traceback.print_exc()
        print('IllegalPropertyError가 발생')
    except TimeoutError as e:
        traceback.print_exc()
        print('TimeoutError가 발생')