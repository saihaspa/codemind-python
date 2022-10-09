n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if(a[i-1]%2==0 and a[i+1]%2!=0):
        c+=1
    if(a[i-1]%2!=0 and a[i+1]%2==0):
        c+=1
if((a[n-2]%2==0 and a[0]%2!=0) or (a[n-2]%2!=0 and a[0]%2==0)):
    c+=1
if((a[n-1]%2==0 and a[1]%2!=0) or (a[n-1]%2!=0 and a[1]%2==0)):
    c+=1
print(c)