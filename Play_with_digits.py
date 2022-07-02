n=input()
a=list(map(int,input().split()))
c=0
for i in a:
    
    while(i):
        rem=i%10
        c=c+rem
        i//=10
print(c)