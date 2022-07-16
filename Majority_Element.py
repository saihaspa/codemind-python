n=int(input())
a=list(map(int,input().split()))
k=n/2
for i in a:
    if(a.count(i)>k):
        print(i)
        break