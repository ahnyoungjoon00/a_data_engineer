"""
모듈 : 함수, 변수, 클래스를 모아 놓은 파이썬 스크립트 파일 : .py
import : 외부모듈의 함수, 변수, 클래스를 현재 모듈에서 사용하기 위해 사용하는 키워드
외부모듈의 위치를 탐색하기 위해
    절대경로 : 프로젝트의 최상위 폴더(root)를 기준으로 경로를 표시 == 최상위폴더의 경로
        프로젝트의 진입점에 해당하는 모듈이 위치한 경로 == 최상위폴더의 경로
        프로젝트의 진입점에 해당하는 모듈 == 파이썬을 실행하는 스크립트 파일이 ==
        진입점으로 사용되는 모듈의 이름 : __main__
    상대경로 : 현재 파일의 위치를 기준으로 경로를 표시 (사용하지 않음)
"""
# from util.utils import calculate_hypotenuse
import util.utils
from util.utils import *
print("C module :", __name__)

def study_import() :
    """
    import : 외부모듈을 사용하기 위한 키워드
    import 모듈 명 : 모듈 전체를 import
    from 모듈 명 import 변수 or 함수 or 클래스 :
                    모델에서 특정 변수나 함수나 클래스를 가져다가 사용
    """
    # calculate_hypotenuse(3, 4)
    # util.utils.calculate_hypotenuse(3, 4)
    calculate_hypotenuse(3, 4)
study_import()