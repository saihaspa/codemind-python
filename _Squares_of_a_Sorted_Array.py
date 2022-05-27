n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(i**2)
b.sort()
print(*b)