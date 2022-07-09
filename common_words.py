s1=input().lower()
s2=input().lower()
if len(s1)>len(s2):
    for i in s1.split():
        for j in s2.split():
            if i==j:
                print(i,end=' ')
else:
    for i in s2.split():
        for j in s1.split():
            if i==j:
                print(i,end=' ')
