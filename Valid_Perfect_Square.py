import math
n=int(input())
for i in range(n):
    a=int(input())
    for i in range(1,a):
        if(math.sqrt(a)==i):
           print('True')
           break
        else:
            continue
    else:
        print('False')