def isugly(n):
    if(n==1):
        return 1
    if(n<=0):
        return 0
    if(n%2==0):
        return isugly(n//2)
    if(n%3==0):
        return isugly(n//3)
    if(n%5==0):
        return isugly(n//5)
    
n=int(input())
k=isugly(n)
if(k==1):
    print('Ugly Number')
else:
    print('Not Ugly Number')