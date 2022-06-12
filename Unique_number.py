n=int(input())
a=[]
t=0
while(n):
    rem=n%10
    n//=10
    if rem not in a:
        a.append(rem)
    else:
        t=1
if(t==0):
    print('Unique Number')
else:
    print('Not Unique Number')