s=input()
a=[]
c=-1
for i in s.split():
    c+=1
    if(c%2==0):
        a.append(i[::-1])
    else:
        a.append(i)
print(*a,end=' ')