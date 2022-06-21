s=input()
c="aeiou"
b=[]
m=0 
for i in range(len(s)):
    if s[i] in c:
        b.append(s[i])
for i in c:
    if i not in b:
        m+=1
        print(i,end=' ')
if m==0:
    print('0')
        