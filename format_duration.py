"""
Human Readable Duration Format

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.


Status: solved
"""


import math

def format_duration(seconds):
    if seconds==0:
        return 'now'
    y,d,h,m,s=0,0,0,0,0
    sCounter = seconds
    y=int(math.floor(sCounter/31536000))
    sCounter-=y*31536000
    
    d=int(math.floor(sCounter/86400))
    sCounter -= d*86400
    h=int(math.floor(sCounter/3600))
    sCounter-=h*3600
    m=int(math.floor(sCounter/60))
    sCounter-=m*60
    s=sCounter
    print(y)
    print('years')
    print(d)
    print('days')
    print(h)
    print('hours')
    print(m)
    print('minutes')
    print(s)
    print('seconds')
    finalArr=[]
    if y>1:
        finalArr.append(str(y)+" years")
    elif y>0:
        finalArr.append(str(y)+" year")
    if d>1:
        finalArr.append(str(d)+" days")
    elif d>0:
        finalArr.append(str(d)+" day")
    if h>1:
        finalArr.append(str(h)+" hours")
    elif h>0:
        finalArr.append(str(h)+" hour")
    if m>1:
        finalArr.append(str(m)+" minutes")
    elif m>0:
        finalArr.append(str(m)+" minute")
    if s>1:
        finalArr.append(str(s)+" seconds")
    elif s>0:
        finalArr.append(str(s)+" second")
    
    if len(finalArr)>1:
        finalArr[-1]="and " + finalArr[-1]

    for i in range(0, len(finalArr)-2):
        finalArr[i]=finalArr[i]+','
    for i in range(1, len(finalArr)):
        finalArr[i]= ' '+finalArr[i]
    
    finalStr=''
        
    for i in finalArr:
        finalStr+=i
    
    return finalStr
    



    
    


print(format_duration(3662))