n=int(input())
a=list(map(int,input().split()))
k=sum(a)
m=[]
for i in a:
    if k%i==0:
        m.append(i)
print(max(m))
        