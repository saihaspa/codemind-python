a,b=map(int,input().split())
if a==10 and b==1:
    print('Yes')
elif(a==1 and b==10):
    print('Yes')
elif(a==b+1 or b==1+a):
    print('Yes')
else:
    print('No')