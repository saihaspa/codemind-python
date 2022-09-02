n=int(input())
a=list(map(int,input().split()))
e=[]
o=[]
l=[]
for i in range(0,n):
    if(a[i]%2!=0):
        e.append(a[i])
    else:
        o.append(a[i])

j,k,f=0,0,0
while(j<len(e) and k<len(o)):
    if(f==0):
        l.append(e[j])
        j+=1
        f=1
    else:
        f=0
        l.append(o[k])
        k+=1
while(k<len(o)):
    l.append(o[k])
    k+=1
while(j<len(e)):
    l.append(e[j])
    j+=1

print(*l,end=' ')
if(n%2!=0):
    print("0")