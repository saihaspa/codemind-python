n=int(input())
for i in range(n,0,-1):
    for j in range(1,n+1,1):
        if(i+j==n+1 or i==j):
            print(i,end=' ')
        else:
            print(end=' ')
    print()