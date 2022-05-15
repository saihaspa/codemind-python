n=int(input())
s=0
p=n
while n>0:
    rem=n%10
    s=s+rem
    n//=10
if(p%s==0):
    print('True')
else:
    print('False')
