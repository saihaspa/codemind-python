s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
a=[]
for i in s1:
    if i in s2:
        if i==" ":
            continue
        if ord(i) not in a:
            a.append(ord(i))

for i in s2:
    if i in s1:
        if i==" ":
            continue
        if ord(i) not in a:
            a.append(ord(i))
a.sort() 
c=0
for i in a:
    c+=1
print(c)