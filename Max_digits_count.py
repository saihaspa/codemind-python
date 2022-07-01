n=int(input())
a=list(map(int,input().split()))
max=0
for i in a:
    c=0
    while(i):
        rem=i%10
        i=i//10
        c+=1
    if max<c:
        max=c
k=0
for i in a:
    cnt=0
    while(i):
        rem=i%10
        i=i//10
        cnt+=1
    if(cnt==max):
        k+=1
print(k)
    
    