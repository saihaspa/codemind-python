a=int(input())
h=a//3600
m=(a-(3600*h))//60
s=(a-(3600*h)-(m*60))
print("H:M:S-",end='')
print(h,end='')
print(":",end='')
print(m,end='')
print(":",end='')
print(s)