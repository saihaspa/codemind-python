def calcAngle(h,m):
    if h==12:
        h=0
    if m==60:
        m=0
        h+=1
        if(h>12):
            h=h-12
    hour_angle=0.5*(h*60+m)
    minute_angle=6*m
    angle=abs(hour_angle-minute_angle)
    angle=min(360-angle,angle)
    return angle
h,m=map(int,input().split(':'))
print(calcAngle(h,m))
