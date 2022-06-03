r=int(input())
a=list(map(int,input().split())) 
k=0
for i in range(r):
    c=0
    for j in range(i+1,r):
        if(a[i]==a[j]):
            c+=1
    k=k+c%2
print(k)