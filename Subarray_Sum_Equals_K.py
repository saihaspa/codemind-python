n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(n):
    s=0
    for j in range(i,n):
        s+=a[j]
        if s>k:
            break
        if s==k:
            c+=1
print(c)