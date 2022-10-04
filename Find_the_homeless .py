n=int(input())
a=[]
b=[]
for i in range(n):
    x=int(input())
    a.append(x)
for i in range(n):
    y=int(input())
    b.append(y)
c=0
cnt=0
for i in range(n):
    c=1
    for j in range(n):
        if(a[i]<=b[j]):
            b[j]=0
            c=0
            break
    if(c!=0):
        cnt+=1
print(cnt)