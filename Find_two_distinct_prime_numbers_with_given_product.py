n=int(input())
t=0
for i in range(2,n):
    if n%i==0:
        for j in range(1,i+1):
            if i%j==0:
                t+=1
        if(t==2):
            print(i,n//i,end=' ')
            break
    if(i==n-1):
        print('-1')
    
    