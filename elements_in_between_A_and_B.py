n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=0
for i in range(len(a)):
    if(a[i]>=x and a[i]<=y):
        c+=1
        print(a[i],end=' ')
        
if(c==0):
    print(-1)