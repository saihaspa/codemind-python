n=int(input())
a=list(map(str,input().split()))
b=[]
s=''
d=''
for i in a:
    s+=i
f=int(s)
f=f+1
d=str(f)
for i in d:
    b.append(i)
print(*b)