"""Simple Fun #15: Addition without Carrying

A little boy is studying arithmetics. He has just learned how to add two integers, written one below another, column by column. But he always forgets about the important part - carrying.

Given two integers, find the result which the little boy will get.

Status: Solved"""

def addition_without_carrying(a,b):
    if a>b or a==b:
        list_a = [int(x) for x in str(a)]
        list_b = [int(x) for x in str(b)]
    if b>a:
        list_a = [int(x) for x in str(b)]
        list_b = [int(x) for x in str(a)]
    print(list_a)
    print(list_b)
    while len(list_a) > len(list_b):
        list_b.insert(0,0)
    print(list_a)
    print(list_b)
    list_final=[]
    i=0
    while i<len(list_b):
        s= list_b[i]+list_a[i]
        list_final.append(s%10)
        i+=1



    return int(''.join(map(str, list_final)))

addition_without_carrying(99,999)