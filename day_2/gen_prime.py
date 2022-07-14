max_num = 1000

def prime(max_num):
    for i in range(2, max_num + 1):
        flag = False
        for j in range(2, i//2 + 1):
            if i % j ==0:
                flag = True
                break
        if not flag:
            yield i

num = prime(max_num)

while(num != ''):
    try:
        print(num.__next__())
    except StopIteration:
        break