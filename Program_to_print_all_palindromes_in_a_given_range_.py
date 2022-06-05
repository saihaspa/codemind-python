def palin(i):
    temp=i
    r=0
    while(i):
        rem=i%10
        r=r*10+rem
        i//=10
    if(r==temp):
        return 1
    else:
        return 0
a=int(input())
b=int(input())
for i in range(a,b):
    if palin(i):
        print(i,end=' ')
    else:
        continue