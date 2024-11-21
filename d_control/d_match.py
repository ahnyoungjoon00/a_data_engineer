"""
등위비교일때 사용하는 제어문
==
"""
def study_match(status):
    match status:
        case 400:
            print('Bad request')
        case 401 | 402:
            print('Not allowed')
        case 404:
            print('Not found')
        case 418:
            print('Im a teapot')
        case _:
            print('등록되지 않은 상태코드입니다.')

study_match(400)