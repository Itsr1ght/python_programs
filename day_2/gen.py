
def print_char_of_string(string):
    for i in string:
        yield i

a = print_char_of_string("Hello_World")

while(a != ''):
    try:
        print(a.__next__())
    except StopIteration:
        break