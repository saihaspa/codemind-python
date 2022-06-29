n=int(input())
a=list(map(int,input().split()))
max=a[0]
for i in a:
    if(max<i):
        max=i
print(max)