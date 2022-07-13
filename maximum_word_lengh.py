s=input()
a=[]
for i in s.split():
    a.append(i)
max=0
for i in a:
    if len(i)>max:
        max=len(i)
print(max)