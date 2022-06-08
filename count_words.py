def cntwords(str):
    vowel=set('aeiouAEIOU')
    c=0
    for i in str.split():
        i=list(i)
        n=len(i)-1
        if i[0] in vowel and i[n] not in vowel:
            c=c+1
    return c
str=input()
print(cntwords(str))