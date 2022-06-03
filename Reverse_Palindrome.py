def palin(n):
    temp=n
    r=0
    s=0
    while(n):
        rem=n%10
        r=r*10+rem
        n//=10
    s=temp+r
    k=s
    rev=0
    while(s):
        rm=s%10
        rev=rev*10+rm
        s//=10
    if(rev==k):
        print(rev)
    else:
        palin(rev)
        
n=int(input())
palin(n)