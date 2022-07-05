def ispalin(i):
    temp=i
    t=temp[::-1]
    if t==i:
        return 1
    else:
        return 0
s=input()
s=s.lower()
c=0
for i in s.split():
    if ispalin(i):
        c+=1
print(c)