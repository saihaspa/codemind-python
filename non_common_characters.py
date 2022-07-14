s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
a=[]
for i in s1:
    if i not in s2:
        if i==" ":
            continue
        if i not in a:
            a.append(i)
for i in s2:
    if i not in s1:
        if i==" ":
            continue
        if i not in a:
            a.append(i)
a.sort() 
for i in a:
    print(i,end='')