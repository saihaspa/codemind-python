s=input()
s=s.split()
k=chr(ord(min(s[-1])))
m=k
t=k.lower()
for i in s[-1]:
    if t in i:
        print(i)
        break
else:
    print(m)