"""
등위비교일때 사용하는 제어문
"""

def study_match(status) :
    match status :
        case 400 :
            print("Bad Request")
        case 401 | 402 :
            print("Not Allowed")
        case 404 :
            print("Not Found")
        case 418 :
            print("Im a Teapot")
        case _ :
            print("등록되지 않은 상태코드입니다.")

error_lst = [400, 401, 402, 403, 404, 405, 418]
for i in error_lst :
    study_match(i)