n=int(input())
a=list(map(int,input().split()))
min=999
for i in a:
    c=0
    while(i):
        rem=i%10
        i=i//10
        c+=1
    if min>c:
        min=c
k=0
for i in a:
    cnt=0
    while(i):
        rem=i%10
        i=i//10
        cnt+=1
    if(cnt==min):
        k+=1
print(k)
    
    