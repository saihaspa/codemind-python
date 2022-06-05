t=int(input())
while(t>0):
    m,n=map(int,input().split())
    ans=-1
    for i in range(n+1):
        if((i*i)%n==m):
            ans=i
            break
    print(ans)
    t-=1