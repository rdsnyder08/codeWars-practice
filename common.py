def common(a, b, c):
    finalLst=[]
    counter=0
    for i in a:
        if i not in finalLst:
            x=min(b.count(i),c.count(i),a.count(i))
            counter+=i*x
            finalLst.append(i)
    print(finalLst)
        

                


    return counter

print(common([1,2,3],[5,3,2],[7,3,2]))