n=int(input())
#b=0
for i in range(n,0,-1):
    #b+=1
    for j in range(1,i+1):
        print(chr(64+i),end=' ')
    print()