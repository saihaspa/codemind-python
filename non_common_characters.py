s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
a=[]
d=[]
for i in s1:
    if i not in s2:
        if i==" ":
            continue
        if ord(i) not in a:
            a.append(ord(i))
for i in s2:
    if i not in s1:
        if i==" ":
            continue
        if ord(i) not in a:
            a.append(ord(i))
a.sort() 
for i in a:
    print(chr(i),end='')
        
    