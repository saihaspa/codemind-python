n=int(input())
a=list(map(int,input().split()))
b=[]
b=set(a)
c=list(b)
dc=0
for i in range(len(c)):
    if c[i]%2==0:
        dc+=1
print(dc)