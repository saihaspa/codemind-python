n=int(input())
a=[]
c=0
for i in range(n):
    b=int(input())
    a.append(b)
t=int(input())
for i in a:
    if i<=t:
        c+=1
    else:
        c+=2
print(c)