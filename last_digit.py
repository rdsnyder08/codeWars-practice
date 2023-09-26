"""
Last Digit of a Large Number

Define a function that takes in two non-negative integers a and b and returns the last digit of a^b

Status: solved, but inelegantly"""



def last_digit(n1, n2):
    if n2 == 0:
        return 1
    n1= n1%10
    if n1 == 0:
        return 0
    if n1 == 1:
        return 1
    if n1 == 2:
        n2 = n2 % 4
        if n2 == 0:
            return 6
        return n1**n2
    if n1 == 3:
        n2 = n2 % 4
        if n2 == 0:
            return 1
        n3= n1** n2
        return n3%10
    if n1 == 4:
        n2 = n2%2
        if n2 == 0:
            return 6
        return 4
    if n1 == 5:
        return 5
    if n1 == 6:
        return 6
    if n1 == 7:
        n2 = n2 % 4
        if n2 == 0:
            return 1
        n3 = n1**n2
        return n3%10
    if n1 == 8:
        n2 = n2%4
        if n2 == 0:
            return 6
        n3 = n1**n2
        return n3%10
    if n1 == 9 :
        n2 = n2%2
        if n2 == 0:
            return 1
        else:
            return 9
    return



print(last_digit(2 ** 200, 2 ** 300))