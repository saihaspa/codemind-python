n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    for j in range(i+1,n):
        if a[i] is a[j]:
            print(a[i])
            break