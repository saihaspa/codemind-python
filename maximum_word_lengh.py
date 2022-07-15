s1=input()
max=0
for i in s1.split():
    if len(i)>max:
        max=len(i)
print(max)
