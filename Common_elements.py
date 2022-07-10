m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
for i in a:
    if i in b:
        c.append(i)
for i in c:
    if i not in d:
        d.append(i)
print(*d,end=' ')