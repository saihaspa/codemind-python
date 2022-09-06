s=input()
n=int(input())
k=n%len(s)
t=n//len(s)
c=0
for i in s:
    if(i=='a'):
        c+=1
m=t*c
x=0
for i in range(k):
    if(s[i]=='a'):
        x+=1
print(m+x)