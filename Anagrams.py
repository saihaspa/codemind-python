def check(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("True")
    else:
        print("False")        
s1=input()
s2=input()
s1=s1.upper()
s2=s2.upper()
check(s1,s2)