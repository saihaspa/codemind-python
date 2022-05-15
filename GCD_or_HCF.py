n,k=map(int,input().split())
gcd=0
for i in range(1,n+1):
    if n%i==0 and k%i==0:
        gcd=i
print(gcd)