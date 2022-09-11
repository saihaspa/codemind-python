s=input()
t=s.split()
n=len(t)
for i in range(n):
    for j in range(i+1,n):
        if(len(t[i])>len(t[j])):
            temp=t[i]
            t[i]=t[j]
            t[j]=temp
        if(len(t[i])==len(t[j])):
            t.sort()
        for k in t:
            print(k,end=' ')
        break
    break