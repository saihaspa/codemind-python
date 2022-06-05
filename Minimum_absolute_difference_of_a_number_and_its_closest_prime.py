def prime(i):
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            return 0
    else:
        return 1
n=int(input())
temp=n
for i in range(n,n+110):
    if prime(i):
        k=i
        break
for t in range(n,n-100,-1):
    if prime(t):
        p=t
        break
if((k-temp)>(temp-t)):
    print(temp-t)
elif((k-temp)==(temp-t)):
    print(k-temp)
else:
    print(k-temp)