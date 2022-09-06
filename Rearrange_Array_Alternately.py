t=int(input())
for i in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    if(n%2==0):
        for j in range((n//2)-1):
            print(a[n-j-1],end=' ')
            print(a[j],end=' ')
        print(a[n//2],end=' ')
        print(a[(n//2)-1])
    else:
        for j in range(n//2):
            print(a[n-j-1],end=' ')
            print(a[j],end=' ')
        print(a[n//2])