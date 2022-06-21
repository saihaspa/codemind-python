n=int(input())
m=0
for i in range(n):
    s=input()
    if(s=='++X' or s=='X++'):
        m+=1
    else:
        m-=1
print(m)