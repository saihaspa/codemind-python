n=int(input())
a=list(map(int,input().split()))
flag=0
for i in range(len(a)):
    if a[i]%2!=0:
        if(i%2==0):
            print('False')
            break
else:
    print('True')