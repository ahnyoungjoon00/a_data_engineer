from _LinkedList import LinkedList

def test_append():
    list = LinkedList()
    
    for i in range(10):
        list.append(i**2)
    
    for e in list:
        print(e)
    
def test_prepend():
    list = LinkedList()
    
    for i in range(11,100):
        list.append(i)
        
    list.prepend(10000)
    print(list)
    
def test_insert():
    list = LinkedList()
    
    for i in range(10):
        list.append(i)
        
    list.insert(4, 10000)
    print(list)

def test_remove():
    list = LinkedList()
    for i in range(10):
        list.append(i**2)
    
    print(list)
    print(list.remove(25))
    print(list)

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

list_comprehension()