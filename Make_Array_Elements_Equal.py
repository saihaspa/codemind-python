n=int(input())
a=list(map(int,input().split()))
s=list(set(a))
if(len(s)==1):
    print('0')
else:
    m=0
    for i in range(len(a)):
        c=0
        for j in range(i,len(a)):
            if a[i]==a[j]:
                c+=1
        if(c>m):
            m=c
    print(m)