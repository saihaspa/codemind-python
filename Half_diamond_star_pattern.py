def hds(n):
    for i in range(n):
        for i in range(0,i+1):
            print('*',end='')
        print()
    for i in range(1,n):
        for j in range(i,n):
            print('*',end='')
        print()
n=int(input())
if(3<=n<100):
    hds(n)
else:
    print('The pattern is not possible')
    
    