"""
set(집합) : 중복을 허용하지 않고 순서가 없는 자료구조
set : mutable 객체
frozen_set : immutable 객체
"""

def study_set():
    set_a = {'백지영', '윤도현', '김경호', '김경호'}
    set_b = {'김경호', '라나델레이', '아델', '박정현'}
    set_c = {'김경호', '백지영'}

    # C
    set_a.add('로제')

    # R
    for e in set_a:
        print('a집합 : ', e)

    # U : set_a라는 집합을 수정
    #    수정을 위해서는 식별자가 필요하다.
    #     a list의 3번 인덱스에 있는 값을 '파이썬'으로 변경
    #     key값이 'mc' 인 학원의 이름을 변경
    #  set은 요소를 특정할 수단이 없기 때문에 수정이 없음

    # D
    set_a.remove('로제')
    print(set_a)

    #  부분집합여부 확인
    print(set_a <= set_c)

    # 진부분집합여부 확인
    print(set_a < set_c)

    # 상위집합여부 확인
    print(set_a >= set_c )

    # 진상위집합여부 확인
    print(set_a > set_c )

    # 합집합 
    union = set_a | set_b | set_c
    print(union)

    # 교집합
    intersection = set_a & set_b
    print(intersection)

    # 차집합
    difference = set_a - set_b
    print(difference)

    # 대칭차 : 합집합 - 교집합
    symmetric_difference = set_a ^ set_b
    print(symmetric_difference)





study_set()
