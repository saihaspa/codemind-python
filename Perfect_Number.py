n=int(input())
p=n
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==p:
    print('True')
else:
    print('False')