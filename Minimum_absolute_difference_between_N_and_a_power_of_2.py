N=int(input())
t=0
min=999
for i in range(1,N+1):
    t=abs(N-(2**i))
    if(min>t):
        min=t
print(min)
    