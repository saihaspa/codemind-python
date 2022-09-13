n=int(input())
a=list(map(int,input().split()))
max=0
s=0
for i in range(0,n-1,1):
    max=0
    for j in range(i+1,n,1):
        if(a[j]>max):
            max=a[j]
    a[i]=max
for i in range(0,n-1):
    print(a[i],end=' ')
a[n-1]=-1
print(a[n-1])