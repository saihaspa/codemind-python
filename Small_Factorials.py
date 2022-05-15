p=int(input())
t=1
fact=1
while t<=p:
    n=int(input())
    while n>0:
        fact=fact*n
        n-=1
    print(fact)
    fact=1
    