s=input().split()
t,j='',''
p=[]
for i in s:
    a=''
    j+='a'
    h=i[0]
    if h in 'aeiouAEIOU':
        a+=i
        a+='ma'
    else:
        for k in range(1,len(i)):
            a+=i[k]
        a+=h
        a+='ma'
    a+=j
    p.append(a)
print(*p)