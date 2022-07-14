s=input()
a='aeiouAEIOU'
c=0
for i in s:
    if i in a:
        c+=1
    else:
        continue
print(c)