a=input().split()
c=[]
d=[]
for i in a:
    for j in i:
        if j.isalpha():
            c.append(j)
        else:
            d.append(j)
c.sort()
k,l=0,0
for i in a:
    for j in range(len(i)):
        if i[j] in c:
            print(c[k],end='')
            k+=1
        else:
            print(d[l],end='')
            l+=1
    print(end=' ')
    