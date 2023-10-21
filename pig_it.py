"""
Simple Pig Latin

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Status: solved"""

def pig_it(text):
    splitWords=text.split(' ')
    print(splitWords)
    finalStr=''
    for i in splitWords:
        finalStr+=' '
        if len(i)==1:
            if ord(i)<= 122 and ord(i)>=65:
                finalStr+=i+'ay'
            else:
                finalStr+=i
        else:
            finalStr+=i[1:]+i[0]+'ay'
    print(finalStr)
    
    

    return finalStr[1:]

print(pig_it('Pig latin is cool'))