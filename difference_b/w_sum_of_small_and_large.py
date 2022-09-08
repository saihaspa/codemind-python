s=input()
t=0
k=0
d=[]
for i in s.split():
   d.append(i) 
for j in d:
    k=k+ord(min(j))
    t+=ord(max(j))
print(t-k)