"""
dictionary : {key : value} 형태로 데이터를 관리하는 자료구조
key : 식별자, 유일한 값
value : 저장할 데이터, 중복 허용
"""

def study_dict() :
    # 기본 생성
    origin = {"one" : 1, "two" : 2, "three" : 3, "age" : 66}
    b = dict(one = 1, two = 2, three = 3)

    region = ["서울", "대전", "대구", "부산"]
    population = [1000, 150, 210, 300]
    c = dict(zip(region, population))

    print(b["one"])
    print(c)

    # create
    origin["four"] = 4
    print(origin)

    # read
    # key - value 쌍으로 읽기
    for entry in origin.items() :
        print(entry, type(entry))

    # key
    for key in origin.keys() :
        if ("t" in key) :
            print(origin[key])

    # value
    for v in origin :
        print(v)

    # key값으로 특정 요소를 식별
    print(origin["one"])

    # update
    origin["one"] = "하나"

    # delete
    del origin["age"]
    print(origin)

study_dict()