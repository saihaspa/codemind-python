r=int(input())
c=int(input())
a=[list(map(int,input().split())) for i in range(r)]
s=0
for i in range(r):
    for j in range(c):
        s=s+a[i][j]
print(s)