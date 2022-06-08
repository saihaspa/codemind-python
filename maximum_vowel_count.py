n=input()
c=[]
z=n.split(' ')
for i in z:
    vowel=sum(letter in'aeiou'for letter in i.lower())
    c.append(vowel)
m=max(c)
print(m)
