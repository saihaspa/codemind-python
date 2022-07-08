n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
s=0
c=0
for i in range(len(a)):
    if(a[i]>=x and a[i]<=y):
        c+=1
        s=s+a[i]
        
if(c==0):
    print(-1)
else:
    print(s)