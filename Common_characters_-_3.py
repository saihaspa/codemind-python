s=input()
l=s.split()
e=''
c=0
l1=list(l[0])
l.remove(l[0])
for i in l1:
    if i.islower():
        for j in range(len(l)):
            if i not in l[j] and i not in e:
                break
        else:
            if i not in e:
                    e+=i
                    c+=1
    else:
        continue
if(c>0):
    print(min(e))
else:
    print('-1')