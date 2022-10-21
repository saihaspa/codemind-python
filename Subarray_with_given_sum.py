def find(a,n,k):
    for i in range(n):
        cur_sum=a[i]
        j=i+1
        while(j<=n):
            if(cur_sum==k):
                print(i+1,j)
                return 1
            elif(cur_sum>k or j==n):
                break
            cur_sum+=a[j]
            j+=1
    else:
        print('-1')
    
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    find(a,n,k)
