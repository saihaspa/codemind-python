n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    temp=a[i]
    for j in range(len(a)):
        if(temp>a[j]):
            c+=1
    print(c,end=' ')
    c=0