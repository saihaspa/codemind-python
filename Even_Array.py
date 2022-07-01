n=int(input())
a=list(map(int,input().split()))
c=0
cnt=0
for i in a:
    c+=1
    if i%2==0:
        cnt+=1
if(c==cnt):
    print('True')
else:
    print('False')