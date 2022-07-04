n=int(input())
a=list(map(int,input().split()))
if(n%2==0):
    for i in range(0,n//2):
        print(a[i],a[n-i-1],end=' ')
else:
    for i in range(0,(n//2)):
        print(a[i],a[n-i-1],end=' ')
    print(a[n//2],'0')   