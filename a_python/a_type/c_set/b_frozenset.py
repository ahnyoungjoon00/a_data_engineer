"""
set(집합) : 중복을 허용하지 않고 순서가 없는 자료구조
set : mutable 객체
frozen_set = immutable 객체
집합과 동일하나 add, remove와 같은 객체의 변경는 불가능
"""
def study_set() :
    set_a = frozenset({'백지영', '윤도현', '김경호', '김경호'})
    set_b = frozenset({'김경호', '라나델레이', '아델', '박정현'})
    set_c = frozenset({'김경호', '백지영'})

    # create
    set_a.add("로제")
    print(set_a)

    # read
    for e in set_a :
        print("a집합 : ", e)
    
    # update(수정)는 안된다
    # set_a라는 집합을 수정하는게 됨
    # 수정을 위해선 기준(식별자)이 필요함
    # list는 인덱스라는 식별자를 통해 값을 수정\

    # remove 후에 add 하는 방식은 값을 특정하는 게 아니라 "수정"의 개념이 아님
    # set은 요소를 특정할 수단이 없기 때문에 "수정"이라고 하지 않음

    # delete
    set_a.remove("로제")
    print(set_a)
    
    # 부분집합 여부 확인
    print(set_a <= set_c)

    # 진부분집합 여부 확인
    print(set_a < set_c)

    # 상위집합 여부 확인
    print(set_a >= set_c)
    
    # 진상위집합 여부 확인
    print(set_a > set_c)

    # 합집합
    union = set_a | set_b | set_c
    print(union)

    # 교집합
    intersection = set_a & set_b & set_c
    print(intersection)

    # 차집합
    difference = set_a - set_b
    print(difference)

    # 대칭차 : 합집합 - 교집합
    symetric_difference = set_a ^ set_b
    print(symetric_difference)

study_set()