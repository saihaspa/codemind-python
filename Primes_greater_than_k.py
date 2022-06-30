def isprime(i):
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            return 0
    else:
        return 1
        
n=int(input())
a=list(map(int,input().split()))
m=int(input())
t=0
for i in a:
    if(i==1):
        continue
    if(i>=m):
        if isprime(i):
            t+=1
print(t)