n=int(input())
r=0
p=n
while n>0:
    rem=n%10
    r=r*10+rem
    n//=10
if p==r:
    print('True')
else:
    print('False')