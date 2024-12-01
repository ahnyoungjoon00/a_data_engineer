from _LinkedList import LinkedList
# a = [1, 2, 3, 4, 5, 6]
# print(a+5)
def test_append():
    list = LinkedList()
    
    for i in range(10):
        list.append(i**2)
    # print(list.__length)
    print(sum(list))
    # return list
    for e in list:
        print(e)
# test_append()
# print(type(test_append()))

def test_append_basic2() :
    list = LinkedList()

    for i in range(10) :
        list.append(i**2)
    
    # for i in range(10) :
    #     print(list.get(i))

    for e in list :
        print(e)
    # print(list.__dict__)
    # print(list)
# test_append_basic2()

def test_get():
    list = LinkedList()
    
    for i in range(10):
        list.append(i**2)
    print(list)
    print(list.get(5))
test_get()

def test_prepend():
    list = LinkedList()

    list.prepend(5555555)
    for i in range(10,50, 5):
        list.append(i)
        
    list.prepend(10000)
    print(list)
# test_prepend()
def test_insert():
    list = LinkedList()
    
    for i in range(10):
        list.append(i)
        
    list.insert(4, 10000)
    print(list)
# test_insert()

def test_pop():
    list = LinkedList()
    for i in range(10):
        list.append(i**2)
    
    print(list)
    print(list.pop())
    print(list)
# test_pop()
def test_remove():
    list = LinkedList()
    for i in range(10):
        list.append(i**2)
    
    # print(list)
    # print(list.remove(25))
    # print(list)
# test_remove()
def list_comprehension():
    """
    [expression for item in iterable if condition]
    """
    list = LinkedList()
    for i in range(10):
        list.append(i**2)
    
    numbers = [(n, m) for n in list if n % 2 == 0 for m in list if m % 2 != 0]
    print(LinkedList.__dict__)
    print(numbers)
# list_comprehension()
def dict_comprehension():
    dict = {'name': 'hmd', 'age':15, 'job':'lec'}
    """
    [expression for item in iterable if condition]
    """
    values = [n for n in dict.values()]
    print(values)

    keys = [n for n in dict.keys()]
    print(keys)

    items = [n for n in dict.items()]
    print(items)

# list_comprehension()