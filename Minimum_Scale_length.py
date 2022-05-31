n=int(input())
a=list(map(int,input().split()))
j=1
min_sc=a[0]
while(j<n):
    if(a[j]%min_sc==0):
        j+=1
    else:
        min_sc=a[j]%min_sc;
print("%d"%min_sc)
    