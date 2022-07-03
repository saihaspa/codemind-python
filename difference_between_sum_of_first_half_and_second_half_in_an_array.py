n=int(input())
a=list(map(int,input().split()))
mid=n//2
s=0
sum=0
diff=0
for i in range(0,mid):
    s=s+a[i]
for i in range(mid,n):
    sum=sum+a[i]
diff=abs(s-sum)
print(diff)