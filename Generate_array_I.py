n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(len(a)):
    if(i%2!=0):
        b.append(a[i])
    else:
        c.append(a[i])
l=[]
for i in range(len(b)):
    s=b[i]
    while(s):
        l.append(c[i])
        s-=1
print(*l)