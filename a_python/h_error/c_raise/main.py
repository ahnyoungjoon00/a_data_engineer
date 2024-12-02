from NaverAPI import NaverAPI
from error.errors import *
import traceback

if __name__ == "__main__" :
    try :
        api = NaverAPI(10)
        api.connect()
    except IllegalPropertyError as e:
        print(e)
        traceback.print_exc()
        print("IllegalPropertyError가 발생")
    except TimeoutError as e :
        print(e)
        print("TimeoutError가 발생")
