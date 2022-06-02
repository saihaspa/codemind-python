n=int(input())
temp=n
sum=0
while(n>0):
    fact=1
    i=1
    d=n%10
    while(i<=d):
        fact=fact*i
        i+=1
    sum=sum+fact
    n//=10
if(sum==temp):
    print("The number %d is a strong number" %temp)
else:
    print("The number %d is not a strong number" %temp)