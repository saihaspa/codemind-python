def flcm(x,y):
    if(x>y):
        g=x
    else:
        g=y
    while(True):
        if((g%x==0) and (g%y==0)):
            lcm=g
            break
        g+=1
    return lcm
        
n=int(input())
a=list(map(int,input().split()))
m=a[0]
n=a[1]
lcm=flcm(m,n)
for i in range(2,len(a)):
    lcm=flcm(lcm,a[i])
print(lcm)