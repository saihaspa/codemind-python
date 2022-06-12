n=int(input())
d=[]
i=0
while(n>0):
    t=n%10
    d.append(t)
    n//=10
    i+=1
for j in range(i-1,-1,-1):
    if d[j]==6:
        d[j]=9
        break
for k in range(i-1,-1,-1):
    print(d[k],end='')
    