n=int(input())
a=list(map(int,input().split()))
for i in range(n-1):
    if a[i+1]>a[i]:
        print('no')
        break
else:
    print('yes')