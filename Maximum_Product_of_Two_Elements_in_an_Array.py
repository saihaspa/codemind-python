a=list(map(int,input().split()))
max=a[0]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if ((a[i]-1)*(a[j]-1))>max:
            max=(a[i]-1)*(a[j]-1)
print(max)