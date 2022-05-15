n=int(input())
s=0
dc=0
p=0
for i in range(1,n+1):
    if(n%i==0):
        p+=1
if p==2:
    while(n):
        rem=n%10
        n=n//10
        dc+=1
        fc=0
        for i in range(1,rem+1):
            if rem%i==0:
                fc+=1
        if fc==2:
            s+=1
    if s==dc:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')
    