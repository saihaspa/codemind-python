m=int(input())
n=int(input())
s=0
for i in range(1,m):
    if(m%i==0):
        s=s+i
if(s==n):
    print('Amicable')
else:
    print('Not Amicable')