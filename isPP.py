import math

def isPP(n):
    i=2
    while i <= math.ceil(math.sqrt(n)):
        m=0
        while i**m <= n:
            if i**m == n:
                return [i,m]
            m+=1
        i+=1
    return None 