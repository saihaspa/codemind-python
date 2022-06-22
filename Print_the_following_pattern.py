n=int(input())
b=0
for i in range(n,0,-1):
    b+=1
    for j in range(b,n+1):
        print(j,end=' ')
    print()