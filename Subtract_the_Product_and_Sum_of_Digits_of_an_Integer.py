n=int(input())
s=0
p=1
while(n>0):
    rem=n%10
    s+=rem
    p*=rem
    n=n//10
d=p-s
print("%d" %d)