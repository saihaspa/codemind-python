n=int(input())
s=input()
t=s.replace(".","B")
if "HH" in s:
    print('NO')
else:
    print('YES')
if "HH" not in s:
    print(s.replace(".","B"))
