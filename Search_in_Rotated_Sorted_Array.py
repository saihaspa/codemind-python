n=int(input())
a=list(map(int,input().split()))
b=int(input())
t=0
n=0
for i in range(len(a)):
    if a[i]==b:
        t=i
        n+=1
if(n==0):
    print('-1')
else:
    print(t)