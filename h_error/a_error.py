from random import randrange
import traceback

# 예외처리 1. 로직을 잘 작성한다.
def study_error():
    while(True):
        inp = input('숫자: ')
        if(inp == 'exit'):
            break

        if(not inp.isnumeric()):
            print('숫자를 입력하세요')
            continue
        
        if(inp == '0'):
            print('0은 안돼')
            continue

        num = int(inp)
        random = randrange(1, 10)
        print(f'{random}/{num} = {random/num}')

def study_error2():
    """
    try - except
    try블록에서 except에 지정한 예외가 발생했을 때, 
    프로그램을 멈추는 대신
    except 블록에 지정한 코드를 실행
    """
    while(True):
        try:
            inp = input('숫자: ')
            if(inp == 'exit'):
                break

            num = int(inp)
            random = randrange(1, 10)
            print(f'{random}/{num} = {random/num}')

        except ZeroDivisionError as e:
            print('0은 입력할 수 없습니다.')
            print(e)
        except ValueError:
            print('숫자를 입력하세요')

def study_error3():
    while(True):
        try:
            inp = input('숫자: ')
            if(inp == 'exit'):
                break

            num = int(inp)
            random = randrange(1, 10)
            print(f'{random}/{num} = {random/num}')
            #print(num + 'hi')

        #except Exception:
        except:
            print('예외가 발생했습니다.')
        finally:
            # 예외 발생여부와 무관하게 반드시 실행되는 코드
            print('====================')

def study_error4():
    while(True):
        try:
            inp = input('숫자: ')
            if(inp == 'exit'):
                break

            num = int(inp)
            random = randrange(1, 10)
            print(f'{random}/{num} = {random/num}')
            #print(num + 'hi')

        #except Exception:
        except:
            print('예외가 발생했습니다.')
            traceback.print_exc()
        finally:
            # 예외 발생여부와 무관하게 반드시 실행되는 코드
            print('====================')


study_error4()