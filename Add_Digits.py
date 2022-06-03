
def fun(n):
    dc=0
    temp=n
    while(n):
        dc+=1
        n=n//10
    if(dc==1):
        return temp
    if(dc>1):
        s=0
        while(temp):
            r=temp%10
            s=s+r
            temp=temp//10
        return fun(s)
n=int(input())
k=fun(n)
print(k)    