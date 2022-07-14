s=input()
s=s.lower()
c=0
for i in s:
    if i==' ':
        continue
    if s.count(i)==1:
        c+=1
print(c)
       