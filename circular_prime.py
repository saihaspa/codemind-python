def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
temp=n
if(prime(n)):
    r=0
    while(n):
        rem=n%10
        r=r*10+rem
        n//=10
    if(prime(r)):
        print("circular prime")
    else:
        print('prime but not a circular prime')
else:
    print('not prime')