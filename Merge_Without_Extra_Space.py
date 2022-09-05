t=int(input())
for i in range(t):
    n,b=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    d=a+b
    d.sort()
    print(*d)