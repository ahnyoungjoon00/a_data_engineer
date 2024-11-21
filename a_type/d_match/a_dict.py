"""
dict : key-value 형태로 데이터를 관리하는 자료구조
key : 식별자, 유일한 값
value : 저장할 데이터, 중복을 허용한다.
"""

def study_dict():
    origin = {"one":1, "two":2, "three":1, "age":45}
    a = dict(one=1, two=2, three=3)

    region = ['서울', '대구', '부산']
    population = [100, 300, 500]
    c = dict(zip(region, population))
    
    print(origin['age'])
    print(c['대구'])

    # C
    origin['four'] = 4
    print(origin)

    # R
    # key-value 쌍으로 읽기
    for entry in origin.items():
        print(entry)
        print(type(entry))

    # key
    for key in origin.keys():
        if('t' in key):
            print(origin[key])

    # value
    for v in origin:
        print(v)

    # key값으로 특정 요소를 식별
    print(origin['one'])

    # U
    origin['one'] = '하나'

    # D
    del origin['one']
    print(origin)

study_dict()