def reverse_string(string):
    length = len(string)
    for i in range(length - 1, -1, -1 ):
        yield string[i]


s = reverse_string("Hello World")
while (s != ''):
    try:
        print(s.__next__())
    except StopIteration:
        break
