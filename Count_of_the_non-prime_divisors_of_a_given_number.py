def prime(t):
    for j in range(2,int(t**0.5)+1):
        if(t%j==0):
            return 1
    else:
        return 0
n=int(input())
c=1
for i in range(1,n+1):
    if(n%i==0):
        if(prime(i)):
            c+=1
print(c)