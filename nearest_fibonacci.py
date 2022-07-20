def nearestFibonacci(num):
    if (num == 0):
        print(0)
        return
    first = 0
    second = 1
    third = first + second
    while (third <= num):
        first = second
        second = third
        third = first + second
    if (abs(third - num)>=abs(second - num)):
        ans =  second
    else:
        ans = third
    k=ans
    return k
   
def Fibonnacci(givenNumber):
    number1 = 1
    number2 = 1
    nextFibo = number1 + number2
    while nextFibo <= givenNumber:
        number1 = number2
        number2 = nextFibo
        nextFibo = number1 + number2
    return nextFibo
n=int(input())
nextFibo=Fibonnacci(n)
k=nearestFibonacci(n)
if((n-k)>(nextFibo-n)):
    print(nextFibo)
elif((n-k)==(nextFibo-n)):
    print(k,end=' ')
    print(nextFibo)
else:
    print(k)