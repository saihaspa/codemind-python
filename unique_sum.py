n=int(input())
a=list(map(int,input().split()))
b=set(a)
s=0
for i in b:
    s=s+i
print(s)