def countCharacterType(s):
    vowels = 0
    consonant = 0
    specialChar = 0
    digit = 0
    for i in range(0, len(s)):
        ch=s[i]
        if((ch>='a' and ch<='z')or(ch >= 'A' and ch<='Z')):
            ch=ch.lower()
            if (ch=='a' or ch=='e' or ch == 'i' or ch == 'o' or ch == 'u'):
                vowels+= 1
            else:
                consonant+= 1
        elif (ch>='0' and ch<='9'):
            digit+=1
        else:
            specialChar += 1
    print("Vowels:", vowels)
    print("Consonants:", consonant)
    print("Digits:", digit)
    print("White spaces:", specialChar)
s=input()
countCharacterType(s)