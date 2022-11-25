n=input()
c=0
s=0
x=[]
for i in list(set(n)):
    for j in n:
        if i==j:
            c+=1
    if c==1:
        s+=1
    else:
        x.append([c,i])
    c=0
a=max(x)
b=min(x)
d=(b[0]-a[0])
if s>1:
    print('Not Valid')
else:
    if d==0 or d==1:
        print('Valid String')
    else:
        print('Not Valid')
        