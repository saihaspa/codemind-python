n=int(input())
for i1 in range(n):
    n1=int(input())
    c=c1=c2=0
    l1=[int(n1)  for n1 in input().split()]
    for i in l1:
        if(i%2!=0):
            c+=1
    if(n1==1):
        print("0")
    else:
        print(c//2)