n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=list(map(int,input().split()))
t=int(input())
c=0
for i in range(len(a)):
    for j in range(i,i+1):
        if(a[i]<t and b[j]>t):
            c+=1
        elif(a[i]==t or b[j]==t):
            c+=1
        else:
            continue
if(c>0):
    print(c)
else:
    print('0')