n=int(input())
a=list(map(int,input().split()))
b=[]
b=set(a)
c=list(b)
s=0
for i in range(len(c)):
    if c[i]%2==0:
        s=s+c[i]
print(s)