m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c,d=0,0
for i in range(len(b)):
    c=0
    for j in range(len(a)):
        if(b[i]==a[i]):
            c+=1
    if(c>0):
        d+=1
if(d>0):
    print('Yes')
else:
    print('No')