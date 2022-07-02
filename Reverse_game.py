def p(i):
    temp=i
    r=0
    while(i):
        rem=i%10
        r=r*10+rem
        i//=10
    print(r,end=' ')
        
n=input()
a=list(map(int,input().split()))
c=0
for i in a:
    p(i)
