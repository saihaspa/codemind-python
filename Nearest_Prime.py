n=int(input())
for p in range(n):
    i=int(input())
    for j in range(i,i-11,-1):
        c=0
        for k in range(1,j+1):
            if(j%k==0):
                c+=1
        if(c==2):
            np=j
            d=i-np
            break
    for j in range(i,i+11):
        c=0
        for k in range(1,j+1):
            if(j%k==0):
                c+=1
        if(c==2):
            sp=j
            e=sp-i
            break
    if(d<e or d==e):
        print(np)
    else:
        print(sp)
    
        