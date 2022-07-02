s=input()
t=input()
for i in range(len(s)):
    if s[i] in t:
        print('True')
        print(i)
        break
else:
    print('False')