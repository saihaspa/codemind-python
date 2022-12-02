for _ in range(int(input())):
    n=int(input())
    s=input()
    k=-1
    for i in range(n):
        if s.count(s[i])==1:
            k=s[i]
            break
    print(k)