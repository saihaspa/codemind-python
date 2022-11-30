s=input()
a=[]
for i in s:
    if i.isdigit():
        a.append(int(i))
a=list(set(a))
b=[]
k=[]
a.sort()
for i in a:
    if i%2==0:
        k.append(i)
    else:
        b.append(i)
if len(k)==0:
    print('-1')
else:
    t=min(k)
    z=b+k
    z.sort(reverse=True)
    for i in z:
        if i==t:
            y=i
            continue
        else:
            print(i,end='')
    print(y)