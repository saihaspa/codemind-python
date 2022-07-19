def balanced_string_split(s):
    e=0
    ares=0
    max=0
    for char in s:
        if char=='L':
            e+=1
        else:
            ares+=1
        if e==ares:
            max+=1
            e=0
            ares= 0
    return max
s=input()
print(balanced_string_split(s))