def decimalToBinary(n):
    k=0
    if(n>1):
        decimalToBinary(n//2)
    k=n%2
    print(k,end='')
     
t=int(input())    
for i in range(t):
    n=int(input()) 
    decimalToBinary(n)
    print()