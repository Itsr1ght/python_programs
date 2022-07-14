
max_num = 50

def fibonacci(max_num):
    first,second = 0,1
    yield first
    for i in range(max_num):
        third = first + second
        first = second 
        second = third
        yield first

num = fibonacci(max_num)
while num!='':
    try:
        print(num.__next__())
    except StopIteration:
        break
