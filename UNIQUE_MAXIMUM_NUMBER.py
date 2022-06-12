n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if i not in b and a.count(i)==1:
        b.append(i)
        c+=1
if(c==0):
    print('-1')
max=0
else:
    for i in b:
        if max<i:
            max=i
    print(max)
    