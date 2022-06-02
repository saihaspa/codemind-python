def s(n):
    k=0
    c=0
    x=n
    while(n):
        d=n%10
        if(d==0):
            return 0
        elif(x%d==0):
            c+=1
        k+=1
        n//=10
    if c==k:
        return 1
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(s(i)==1):
        print(i,end=' ')