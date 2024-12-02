import traceback

def test_a() :
    try :
        test_b()
    except :
        traceback.print_exc()
        print("예외 발생")

def test_b() :
    test_c()

def test_c() :
    a = "A"
    print(f"{a + 10}")


test_a()