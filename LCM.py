m,n=map(int,input().split())
if(m>n):
    min1=m
else:
    min1=n
while(1):
    if((min1)%m==0 and (min1)%n==0):
        print("%d" %min1)
        break
    min1=min1+1

    
