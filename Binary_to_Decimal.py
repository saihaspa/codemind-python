t=int(input())
for i in range(t):
    n=int(input())
    k=0
    i=0
    while(n!=0):
        rem=n%10
        k=k+rem*(2**i)
        n//=10
        i+=1
    print(k)