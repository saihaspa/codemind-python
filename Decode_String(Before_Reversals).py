T=int(input())
for i in range(T):
    n,k=map(int,input().split())
    s=input()
    while k>0:
        t=s[:k]
        s=t[::-1]+s[k:]
        k-=1
    print(s)