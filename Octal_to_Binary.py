for _ in range(int(input())):
    n=int(input())
    i=0
    d=0
    b=0
    while(n):
        d=d+(n%10)*(pow(8,i))
        n//=10
        i=i+1
    i=1
    while(d):
        b=b+(d%2)*i
        d//=2
        i*=10
    print(b)