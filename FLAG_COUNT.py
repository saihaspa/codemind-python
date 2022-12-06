n=int(input())
r=0
x=2
for i in range(n):
    t=r
    r=x
    x+=t
print(r)
