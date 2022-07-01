n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if i==0 or i==1:
        c+=1
if(c==n):
    print('True')
else:
    print('False')
    