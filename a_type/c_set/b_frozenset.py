"""
set(집합) : 중복을 허용하지 않고 순서가 없는 자료구조
set : mutable 객체
frozen_set : immutable 객체
"""

def study_set():
    set_a = frozenset({'백지영', '윤도현', '김경호', '김경호'})
    set_b = frozenset({'김경호', '라나델레이', '아델', '박정현'})
    set_c = frozenset({'김경호', '백지영'})

    # R
    for e in set_a:
        print('a집합 : ', e)

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
