s=input()
a=input()
for i in range(len(s)):
    if(s[i]==a):
        print('True')
        print(i)
        break
else:
    print('False')
    