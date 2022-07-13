s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
a=[]
for i in s1.split():
    for j in s2.split():
        if i==j and s1.count(i)==1 and s2.count(j)==1:
                a.append(i)
print(len(a))