s=input()
a='aeiou'
b=[]
for i in s:
    if i==' ':
        continue
    if i in a:
        b.append(i)
c=0
for i in a:
    if i not in b:
        c=1
        break
if(c==0):
    print('True')
else:
    print('False')