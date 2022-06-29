n=int(input())
for i in range(1,n//2):
    if (i)*(i+1)==n:
        print('YES')
        break
else:
    print('NO')