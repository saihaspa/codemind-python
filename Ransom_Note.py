a,b=map(str,input().split())
e=0
for i in range(len(a)):
    c=a.count(a[i])
    d=b.count(a[i])
    if(c>d):
        e=1
        break
if e:
    print('False')
else:
    print('True')