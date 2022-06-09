a=int(input())
for i in range(a):
    s=input()
    c=0
    for j in s:
        c+=1
    if s==s[::-1]:
        if(c%2==0):
            print('YES',end=' ')
            print('EVEN')
        else:
            print('YES',end=' ')
            print('ODD')
    else:
        print('NO')