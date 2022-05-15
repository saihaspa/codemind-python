n=int(input())
sq=n*n
p=n
r=0
while n>0:
    rem=n%10
    r=r*10+rem
    n//=10
t=0
q=r*r
while q>0:
    rem=q%10
    t=t*10+rem
    q//=10
if t==sq:
    print('True')
else:
    print('False')
    