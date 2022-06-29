n=int(input())
s=n*n
c=0
t=n
while(t!=0):
    c+=1
    t//=10
l=s%(10**c)
if(l==n):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')