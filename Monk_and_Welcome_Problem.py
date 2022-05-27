n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=[]
for i in range(0,n):
    s.append(a[i]+b[i])
for i in range(n):
    print("%d"%s[i],end=' ')
