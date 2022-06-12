def most_frequent(a):
    return max(set(a), key =a.count)
n=int(input())
a=list(map(int,input().split()))
print(most_frequent(a))