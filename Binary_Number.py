n=int(input())
for i in range(2**n):
    b=bin(i)[2:]
    print(str(b).zfill(n))