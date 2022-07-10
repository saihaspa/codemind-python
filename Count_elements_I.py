m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
cnt=0
for i in a:
    if i in b:
        c.append(i)
for i in c:
    if i not in d:
        d.append(i)
        cnt+=1
print(cnt)