n=int(input())
d=n%10
if(d==0):
    print(n//10)
elif(d<0):
    print((n//10)-1)
else:
    print(n//10)