
prime = []
composite = []
composite_multiply = []
max_num = 100
flag = False
count = 0
begin = 1

for begin in range( begin, max_num + 1):
    
    flag = False

    for j in range( 2, (begin//2+1) ):
        if begin % j == 0:
            flag = True
            break

    if not flag and begin != 1:
        prime.append(begin)

    for j in range( 1, begin+1 ):
        if begin % j == 0:
            if j not in composite_multiply:
                composite_multiply.append(j)
            count += 1
    if count > 2:
        composite.append(begin)
    count = 0

print(f"prime numbers from 1 to 100 is \n {prime}")
print(f"composite numbers from 1 to 100 is \n {composite}")
print(f"composite uses these numbers for multiplication \n {composite_multiply}")