s=input()
for i in range(len(s)):
    if s.count(s[i])==1:
        print(i)
        break
    else:
        continue
else:
    print('-1')