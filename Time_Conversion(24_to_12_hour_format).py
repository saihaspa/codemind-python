n=input()
s1=n[0]+n[1]
s1=int(s1)
s2=n[2]+n[3]+n[4]
k=''
l=''
if s1>=0 and s1<=11:
    k+=' AM'
else:
    k+=' PM'
s2+=k
if s1==0:
    l+='12'
    l+=s2
elif s1>0 and s1<=12:
    if s1<=9:
        l+='0'
        l+=str(s1)
        l+=s2
    else:
        l+=str(s1)
        l+=s2
else:
    if s1-12<=9:
        l+='0'
        l+=str(s1-12)
        l+=s2
    else:
        l+=str(s1-12)
        l+=s2
print(l)
    
    