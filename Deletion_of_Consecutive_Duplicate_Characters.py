def countDeletions(string):
    ans = 0
    for i in range(len(string) - 1):
        if (string[i] == string[i + 1]):
            ans += 1
    return ans

n=int(input())  
for i in range(n):
    string=input()
    print(countDeletions(string))