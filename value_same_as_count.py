n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    x=a.count(i)
    if x==i:
        if x not in b:
            b.append(x)
            c+=1
print(c)