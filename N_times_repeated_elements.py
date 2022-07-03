n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=[]
d=0
for i in a:
    x=a.count(i)
    if(x==b):
        if i not in c:
            c.append(i)
            d+=1
if(d==0):
    print('-1')
else:
    print(*c,end=' ')
    