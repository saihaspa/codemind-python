n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
min=999
c=0
for i in range(len(a)):
    if(a[i]>=x and a[i]<=y):
        c+=1
        if min>a[i]:
            min=a[i]
if(c==0):
    print(-1)
else:
    print(min)