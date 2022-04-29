n=int(input())
s=0
t=n*n
while(t>0):
    rem=t%10
    s+=rem
    t=t//10
if s==n:
    print('Neon Number')
else:
    print('Not Neon Number')