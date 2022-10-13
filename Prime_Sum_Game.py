a,b,c,d=map(int,input().split())
for i in range(a,b+1):
    for j in range(c,d+1):
        k=i+j
        for t in range(2,k):
            if(k%t==0):
                break
        else:
            break
    else:
        print('Takahashi')
        break
else:
    print('Aoki')