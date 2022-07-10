n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    for j in range(i+1,n):
        if a[i]>=a[j]:
            c=1
            break
if c==0:
    print('yes')
else:
    print('no')