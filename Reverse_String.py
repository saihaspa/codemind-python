s=input()
st=s.split()[::-1]
a=[]
for i in st:
    a.append(i)
print(*a,end=' ')