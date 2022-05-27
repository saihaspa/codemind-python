n=int(input())
a=list(map(int,input().split()))
k=0
p=0
for i in range(0,n):
    if(a[i]%2==0):
        k+=1
    else:
        p+=1
print("%d"%k,end=' ')
print("%d"%p)