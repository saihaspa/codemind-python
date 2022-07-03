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
if(c==0):
    print('-1')
else:
    print(min(b),max(b))
    
    