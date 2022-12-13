n=int(input())
a=list(map(int,input().split()))
m=a[0]
for i in range(len(a)):
    if(a[i]<m):
        m=a[i]
m_s=m
c=0
#kadane's algorithm
for i in a:
    if(c<0): c=0
    c+=i
    m_s=max(c,m_s)
print(m_s)