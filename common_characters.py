s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
a=[]
c=0
for i in s1:
    if i in s2:
        if i==" ":
            continue
        if ord(i) not in a:
            a.append(ord(i))
            c+=1
for i in s2:
    if i in s1:
        if i==" ":
            continue
        if ord(i) not in a:
            a.append(ord(i))
            c+=1
if(c==0):
    print('-1')
else:
    a.sort() 
    for i in a:
        print(chr(i),end='')