def isValid(s):
    opening="{[("
    closing="}])"
    brackets={')': '(', '}': '{', ']': '['}
    st=[]
    for char in s:
        if char in opening:
            st.append(char)
        elif char in closing:
            if len(st)==0:
                return 0
            if st[-1]==brackets[char]:
                st.pop()
            else:
                return 0
    return len(st)==0
n=int(input())
for i in range(n):
    s=input()
    if(isValid(s)):
        print('True')
    else:
        print('False')