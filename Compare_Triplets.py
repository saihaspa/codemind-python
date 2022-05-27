a=list(map(int,input().split()))
b=list(map(int,input().split()))
k=0
p=0
for i in range(0,3):
    if a[i]>b[i]:
        k+=1
    elif a[i]<b[i]:
        p+=1
    else:
        continue
print("%d"%k,end=' ')
print("%d"%p)