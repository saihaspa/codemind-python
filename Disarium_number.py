n=int(input())
t=n
c=0
while n>0:
    rem=n%10
    n//=10
    c+=1
l=t
s=0
while t>0:
    r=t%10
    t//=10
    s=s+(r**c)
    c-=1
if s==l:
    print('True')
else:
    print('False')