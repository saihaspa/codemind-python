n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if i not in b:
        if i%2==0:
            b.append(i)
            c+=1
print(c)