#Kebabize

#Modify the kebabize function so that it converts a camel case string into a kebab case.

#the returned string should only contain lowercase letters

#status: solved


def kebabize(st):
    kebab_case=''
    for letter in st:
        if letter.islower():
            kebab_case+=letter
        elif letter.isupper():
            if len(kebab_case) == 0:
                kebab_case+=letter.lower()
            else: 
                kebab_case += '-' + letter.lower()

    
    
    return kebab_case
    
    