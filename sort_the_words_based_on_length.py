a=input().split()
a=sorted(a)
a.sort(key=len)
print(*a)