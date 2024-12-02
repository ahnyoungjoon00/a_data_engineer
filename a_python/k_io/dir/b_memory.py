"""
메모리 내에서 이비출력 데이터를 다루어야할 때 사용
"""
from io import BytesIO, StringIO
from os import path

def study_byteIO() :
    filepath = path.dirname(path.realpath(__file__))
    with open(f"{filepath}/test.txt", "rb") as file :
        byte_stream = BytesIO()
        byte_stream.write(file.read())
        byte_stream.seek(2)
        byte_stream.write(b'\nfrom bytestream')
        byte_stream.seek(0)
        print(byte_stream.read())
# study_byteIO()

def study_stringIO() :
    filepath = path.dirname(path.realpath(__file__))
    with open(f"{filepath}/test.txt", "r") as file :
        string_stream = StringIO()
        string_stream.write(file.read())
        string_stream.write('\nfrom stringstream')
        string_stream.seek(0)
        print(string_stream.read())
study_stringIO()