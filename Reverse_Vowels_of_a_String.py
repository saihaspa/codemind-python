def isVowel(c):
    if (c == 'a'or c == 'A' or c == 'e' or
        c == 'E' or c == 'i' or c == 'I' or
        c == 'o' or c == 'O' or c == 'u' or c == 'U'):
        return True
    return False
def reverserVowel(string):
    j = 0
    vowel = [0] * len(string)
    string = list(string)
    for i in range(len(string)):
        if isVowel(string[i]):
            vowel[j]=string[i]
            j+=1
    for i in range(len(string)):
        if isVowel(string[i]):
            j-=1
            string[i]=vowel[j]
    return ''.join(string)
string=input()
print(reverserVowel(string))