import math
n,x=map(int,input().split())
temp=n
while(n):
    last=n%(10**x)
    break
rev="".join(reversed(str(temp)))
while(int(rev)):
    first=(int(rev))%(10**x)
    break
r="".join(reversed(str(first)))
if(int(r)>last):
    print(int(r)-last)
else:
    print(last-int(r))