n=int(input())
a=list(map(int,input().split()))
k=sum(a)
if k%2==0:
    print('1')
else:
    print('0')