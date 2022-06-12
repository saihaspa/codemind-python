def cnt(t):
    if t<0:
        return 0
    if t==0:
        return 1
    return cnt(t-1)+cnt(t-2)+cnt(t-3)
t=int(input())
print(cnt(t))