s=input()
a='aeiouAEIOU'
b=[]
c=0
for i in s:
    if i==' ':
        continue
    if i in a:
        if i not in b:
            b.append(i)
            c+=1
if(c==0):
    print(-1)
else:
    print(*b,end=' ')