a=int(input())
b=int(input())
d=0
for i in range(a,b+1):
    c=0
    for j in range(i,b+1):
        c+=j
        if(c%2!=0):
            d+=1
print(d)