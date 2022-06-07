a=input()
n=int(input())
m=int(input())
for i in a:
    for j in range(n,m+1):
        print(a[j],end='')
    break
    