s=input()
r_s=[]
for i in s.split():
    r_s.append(i[::-1])
sen=" ".join(r_s)
print(sen)