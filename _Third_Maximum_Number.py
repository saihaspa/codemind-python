n=int(input())
a=list(map(int,input().split()))
a=set(a)
a=sorted(a)
if(n>=3):
    print(a[-3])
else:
    print(a[-1])