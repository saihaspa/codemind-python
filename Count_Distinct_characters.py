s=input()
d=[]
c=0
for i in s.lower():
    if i==' ':
        continue
    if i not in d:
        d.append(i)
        c+=1
print(c)
