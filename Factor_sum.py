def fact(i):
    s=0
    for j in range(1,i+1):
        if(i%j==0):
            s+=j
    return s
            
s=input().split(',')
res=[]
for i in s:
    a=fact(int(i))
    if str(a) in  s:
        res.append(int(i))
if(len(res)==0):
    print('-1')
else:
    print(*sorted(res))