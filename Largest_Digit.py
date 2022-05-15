n=int(input())
k=0
while n>0:
    rem=n%10
    n//=10
    if k<rem:
        k=rem
print(k)
    