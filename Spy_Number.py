n=int(input())
s=0
p=1
while(n>0):
    rem=n%10
    s+=rem
    p*=rem
    n=n//10
if(s==p):
    print('Spy Number')
else:
    print('Not Spy Number')
