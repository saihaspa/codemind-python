def prime(n):
    for j in range(2,int(n**0.5)+1):
        if(n%j==0):
            return 0
    else:
        return 1

n=int(input())
a=list(map(int,input().split()))
x=min(a)
y=max(a)
u=a.index(x)
v=a.index(y)
c=0
if(u>v):
    u,v=v,u
for i in range(u,v+1):
    if(a[i]==1 or a[i]==0):
        continue
    if(prime(a[i])):
        c+=1
        
print(c)