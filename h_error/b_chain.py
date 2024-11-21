def test_a():
    try:
        test_b()
    except:
        print('예외가 발생했습니다.')

def test_b():
    test_c()

def test_c():
    a = 'A'
    print(f'{a + 10}')

test_a()
    