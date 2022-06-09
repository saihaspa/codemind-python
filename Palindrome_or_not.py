a_string =input()
def palindrome(string):
    string = string.lower()
    return string == string[::-1]
if(palindrome(a_string)):
    print('True')
else:
    print('False')
