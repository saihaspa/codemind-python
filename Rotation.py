t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    while k:
        j=a[n-1]
        for i in range(n-2,-1,-1):
            a[i+1]=a[i]
        a[0]=j
        k-=1
    for i in range(0,n):
        if(i!=n-1):
            print(a[i],end=' ')
        else:
            print(a[i])