s=input()
a=[]
c,d,e,f,g=0,0,0,0,0
for i in range(len(s)):
    if s[i]=='b':
        c+=1
    elif s[i]=='a':
        d+=1
    elif s[i]=='l':
        e+=1
    elif s[i]=='o':
        f+=1
    elif s[i]=='n':
        g+=1
k=min(c,d,e//2,f//2,g)
if(k>0):
    print(k)
else:
    print(0)