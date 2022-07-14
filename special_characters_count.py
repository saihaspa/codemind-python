s=input()
sp=0
for i in range(len(s)):
    if(s[i].isalpha()):
        continue
    elif(s[i].isdigit()):
        continue
    elif(s[i]==' '):
        continue
    else:
        sp+=1
print(sp)