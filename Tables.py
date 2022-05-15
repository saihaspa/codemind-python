n,r=map(int,input().split())
t=n
for i in range(1,r+1):
    if i%2==0:
        continue
    else:
        print(t,'x',i,'=',n*i)