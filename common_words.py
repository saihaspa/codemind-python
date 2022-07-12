s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
d=[]
c=0
for i in s2.split():
    if i in s1.split():
        d.append(i)
        c+=1
if(c==0):
    print(-1)
else:
    print(*d)
        