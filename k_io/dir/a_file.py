"""
io = input + output
입출력 : 프로그램이 외부와 데이터를 주고 받는 과정
        ex) 파일에서 데이터 읽기, 파일에 데이터 쓰기 -> 네트워크 통신
입력 : 외부에서 우리 메모리로
출력 : 우리 메모리에 있는 것을 외부로
"""
from os import path
def study_write() :
    filepath = path.dirname(path.realpath(__file__))
    file = open(f"{filepath}/test.txt", "w")
    file.write("hello io")
    file.close()
# study_write()

def study_read() :
    filepath = path.dirname(path.realpath(__file__))
    file = open(f"{filepath}/test.txt", "r")
    txt = file.read()
    print(txt)
    file.close()
# study_read()

def study_write_byte() :
    filepath = path.dirname(path.realpath(__file__))
    file = open(f"{filepath}/test_b.txt", "wb")
    file.write(b"hello io")
    file.close()
# study_write_byte()

def study_read_byte() :
    filepath = path.dirname(path.realpath(__file__))
    file = open(f"{filepath}/test_b.txt", "rb")
    txt = file.read()
    print(txt)
    file.close()
# study_read_byte()

def study_read_with() :
    filepath = path.dirname(path.realpath(__file__))
    with open(f"{filepath}/test.txt", "r") as file :
        txt = file.read()
        print(txt)
# study_read_with()

def study_append() :
    filepath = path.dirname(path.realpath(__file__))
    file = open(f"{filepath}/test.txt", "a")
    file.write("\nhello append")
    file.close()
# study_append()

def study_read_with2() :
    filepath = path.dirname(path.realpath(__file__))
    with open(f"{filepath}/test.txt", "r") as file :
        for line in file :
            print(line)
study_read_with2()