n=int(input())
a=list(map(int,input().split()))
t=0
t=sum(a)

ma=k=mi=l=a[0]
for i in range(1,n):
    ma=max(ma+a[i],a[i])
    k=max(k,ma)
    mi=min(mi+a[i],a[i])
    l=min(l,mi)
if n==1:
    print(a[0])
if l==t:
    print(k)
else:
    print(max(k,t-l))