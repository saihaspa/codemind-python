def prime(n):
    if(n==1):
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
rev=0
if(prime(n)):
    while(n):
        r=n%10
        rev=rev*10+r
        n//=10
    if(prime(rev)):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')
        
        