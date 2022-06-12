n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    if a[i]==0:
        b.append(a[i])
for i in range(len(a)):
    if a[i]==1:
        b.append(a[i])
print(*b)