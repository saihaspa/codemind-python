n = int(input())
for i in range(n,0,-1):
    for j in range(n,i,-1):
        print(j,end=" ")
    for j in range(1,i*2):
        print(i,end=" ")
    for j in range(i+1,n+1):
        print(j,end=" ")
    print("")
for i in range(1,n):
    for j in range(n,i,-1):
        print(j,end=" ")
    for j in range(1,i*2):
        print(i+1,end=" ")
    for j in range(i+1,n+1):
        print(j,end=" ")
    print("")