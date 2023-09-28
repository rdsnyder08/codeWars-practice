import re

def domain_name(url):
    arr= re.split(r'[/.]', url)
    filterarr= ['http:','https','www','com','org','net','ru']
    for i in arr:
        if i in filterarr:
            arr.remove(i)
    for i in arr:
        if len(i)== 0:
            arr.remove(i)

    return arr[0]

print(domain_name("http://google.com"))