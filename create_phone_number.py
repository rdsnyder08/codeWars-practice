
#Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

#Status: solved



def create_phone_number(n):
    
    n.insert(0, '(' )
    n.insert(4,')')
    n.insert(5, ' ')
    n.insert(9,'-')
    n=''.join(str(i) for i in n)
    return n

print(create_phone_number([0,1,2,3,4,5,6,7,8,9]))
