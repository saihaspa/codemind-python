n=int(input())
a=list(map(int,input().split()))
b=int(input())
s=0
for i in a:
    if(i==b+1):
        break
    else:
        s=s+i
print(s)
    