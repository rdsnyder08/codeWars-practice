"""
Human Readable Time

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

status:solved
"""

def make_readable(seconds):
    s=seconds
    hh=0
    mm=0
    ss=0
    while s>=3600:
        hh+=1
        s-=3600
    while s>=60:
        mm+=1
        s-=60
    ss=s
    finalStr=""
    if hh>= 10:
        finalStr+=str(hh)
    elif hh>=0:
        finalStr+= "0"+str(hh)
    else: 
        finalStr+="00"
    finalStr+=":"
    if mm>= 10:
        finalStr+=str(mm)
    elif mm>=0:
        finalStr+= "0"+str(mm)
    else: 
        finalStr+="00"
    finalStr+=":"
    if ss>= 10:
        finalStr+=str(ss)
    elif ss>=0:
        finalStr+= "0"+str(ss)
    else: 
        finalStr+="00"
    
    

    return finalStr


print(make_readable(86399))
    
