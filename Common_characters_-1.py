s=input()
s=s.lower()
l=s.split()
e=''
c=0
l1=list(l[0])
l.remove(l[0])
for i in l1:
    for j in range(len(l)):
        if i not in l[j] and i not in e:
            break
    else:
        e+=i
        c+=1

if(c>0):
    print(e)
else:
    print('-1')