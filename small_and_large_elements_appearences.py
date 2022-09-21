s=input()
a=[]
for i in s:
    if(i==' '):
        continue
    else:
        a.append(ord(i))
k=min(a)
t=max(a)
cnt,c,p,n=0,0,0,0
for j in a:
    p=a.count(k)
    n=a.count(t)
print(chr(k),end=' ')
print(p,end=' ')
print(chr(t),end=' ')
print(n,end=' ')