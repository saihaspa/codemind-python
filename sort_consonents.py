a=input().split()
v='aeiou'
for i in a:
    c=[]
    for j in i:
        if j not in v and j.isalpha():
            c.append(j)
    c.sort()
    y=0
    for x in range(len(i)):
        if i[x] not in v and i[x].isalpha():
            print(c[y],end='')
            y+=1
        else:
            print(i[x],end='')
    print(end=' ')
