n=int(input())
a=list(map(int,input().split()))
s=0
sum=0
for i in range(0,n):
    if i%2==0:
        s=s+a[i]
    else:
        sum=sum+a[i]
if(sum-s==0):
    print('YES')
else:
    print('NO')
