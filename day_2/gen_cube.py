
def get_cube(max_num):
    for num in range(max_num):
        yield num * num * num

n = get_cube(100)

while n!='':
    try:
        print(n.__next__())
    except StopIteration:
        break