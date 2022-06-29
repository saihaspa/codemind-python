n=int(input())
for i in range(1,n//2):
    if i*i==n:
        print('True')
        break
else:
    print('False')