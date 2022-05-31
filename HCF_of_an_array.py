n=int(input())
a=list(map(int,input().split()))
j=1
hcf=a[0]
while(j<n):
    if(a[j]%hcf==0):
        j+=1
    else:
        hcf=a[j]%hcf;
print("%d"%hcf)
    