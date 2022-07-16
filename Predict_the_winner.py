n=int(input())
a=list(map(int,input().split()))
k=0
t=0
for i in range(len(a)):
    if(i%2==0):
        k=k+a[i]
    else:
        t=t+a[i]
p=abs(k-t)
if(p%4==0):
    print('X')
else:
    print('Y')