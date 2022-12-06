s=input()
c=0
for i in range(len(s)):
    if s[i]=='I':
        c+=1
    elif s[i]=='V':
        if(s[i-1]=='I' and i>0):
            c+=3
        else:
            c+=5
    elif(s[i]=='X'):
        if(s[i-1]=='I' and i>0):
            c+=8
        else:
            c+=10
    elif(s[i]=='L'):
        if(s[i-1]=='X' and i>0):
            c+=30
        else:
            c+=50
    elif(s[i]=='C'):
        if(s[i-1]=='X' and i>0):
            c+=80
        else:
            c+=100
    elif(s[i]=='D'):
        if(s[i-1]=='C' and i>0):
            c+=300
        else:
            c+=500
    elif(s[i]=='M'):
        if(s[i-1]=='C' and i>0):
            c+=800
        else:
            c+=1000
print(c)