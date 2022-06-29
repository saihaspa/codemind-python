n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s=s+i
k=s//n
for i in a:
    if i==k:
        print('True')
        break
else:
    print('False')