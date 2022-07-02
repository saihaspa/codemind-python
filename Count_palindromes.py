def palin(i):
    temp=i
    r=0
    while(i):
        rem=i%10
        r=r*10+rem
        i//=10
    if(temp==r):
        return 1
        
n=input()
a=list(map(int,input().split()))
c=0
for i in a:
    if palin(i):
        c+=1
print(c)