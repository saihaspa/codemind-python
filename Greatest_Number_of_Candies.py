n=int(input())
a=list(map(int,input().split()))
k=int(input())
max=0
for i in range(len(a)):
    if(a[i]>max):
        max=a[i]
for i in range(len(a)):
    if((a[i]+k)>=max):
        t=True
        print(t,end=' ')
    else:
        f=False
        print(f,end=' ')