n=int(input())
a=list(map(int,input().split()))
c=0
dc=0
for i in range(0,n):
    c=0
    while(a[i]!=0):
        rem=a[i]%10
        c+=1
        a[i]//=10
    if(c%2==0):
        dc+=1
print("%d"%dc)
