def isprime(i):
    if(i==1):
        return 0
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            return 0
    else:
        return 1
        
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if(isprime(i)):
        c+=1
print(c)