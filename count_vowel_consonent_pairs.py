k=input()
v=['a','e','i','o','u','A','E','I','O','U']
co=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
c=0
i=0
j=len(k)-1
while i<(len(k)//2) and j>=(len(k)//2):
    if k[i] in v and k[j] in co:
        c+=1
    elif k[i] in co and k[j] in v:
        c+=1
    i+=1
    j-=1
print(c)