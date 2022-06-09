a=int(input())

for i in range(a):
    s=input()
    c=0
    for j in s:
        if j.isdigit():
            c+=1
    if c>=1:
        print('Yes')
    else:
        print('No')