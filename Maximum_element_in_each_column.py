r,c=map(int,input().split())
a=[list(map(int,input().split())) for i in range(r)]
for i in range(c):
    k=a[0][i]
    for j in range(r):
        if k<a[j][i]:
            k=a[j][i]
    print(k)
        