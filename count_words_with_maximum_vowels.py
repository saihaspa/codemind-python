s=input()
b='aeiouAEIOU'
d=[]
for i in s.split():
    d.append(i)
max=0
for i in d:
    c=0
    for j in i:
        if j in b:
            c+=1
    if(c>max):
        max=c
s=0
for i in d:
    k=0
    for j in i:
        if j in b:
            k+=1
    if(k==max):
        s+=1
print(s)