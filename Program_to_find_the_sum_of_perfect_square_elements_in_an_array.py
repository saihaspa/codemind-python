import math
def persq(i):
    for j in range(0,i):
        if(i==1):
            return 1
        else:
            if(math.sqrt(i)==j):
                return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if(persq(i)):
        c=c+i
print(c)