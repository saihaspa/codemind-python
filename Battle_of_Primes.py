def prime(t):
    for j in range(2,int(t**0.5)+1):
        if(t%j)==0:
            return 0
    else:
        return 1
def fun(s):
    for i in range(1,20):
        t=s+i
        if(prime(t)):
            return i
    
a=int(input())
b=int(input())
s=0
s=a+b
k=fun(s)
print(k)