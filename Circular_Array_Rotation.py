n,k,t=map(int,input().split())
a=list(map(int,input().split()))
for j in range(t):
    p=int(input())
    while k:
        j=a[n-1]
        for i in range(n-2,-1,-1):
            a[i+1]=a[i]
        a[0]=j
        k-=1
    print(a[p])