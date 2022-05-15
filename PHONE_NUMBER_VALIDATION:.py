a=int(input())
c=0
i=0
b=a
while a>0:
    c+=1
    a//=10
if c==10:
    if b/10000000000==0:
        print('Invalid')
    else:
        print('Valid')
else:
    print('Invalid')
    