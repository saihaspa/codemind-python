n=int(input())
for i in range(n):
    t=int(input())
    a=list(map(int,input().split()))
    b=[]
    c=0

    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if(a[i]+a[j] ) in a:
                c+=1
    if(c==0):
        print(-1)
    else:
        print(c)
        