n=int(input())
for i in range(n):
    m=int(input())
    l=list(map(int,input().split()))
    t=sorted(l)
    if l==t:
        print('0')
    else:
        print(max(l)-min(l))