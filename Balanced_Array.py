t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        s1=s2=0
        for j in range(i+1,n):
            s1+=a[j]
        for k in range(i-1,-1,-1):
            s2+=a[k]
        if(s1==s2):
            c+=1
    if(c==0):
        print('NO')
    else:
        print('YES')