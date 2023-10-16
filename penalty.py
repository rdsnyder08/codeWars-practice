import itertools

def penalty(a_list):
    intList=[]
    for i in a_list:
        intList.append(int(i))

    #print(intList)


    combinations = list(itertools.permutations(intList,len(a_list)))
    print(combinations)
    single_int = int(''.join(map(str, combinations[0])))
    #print(single_int)
    for combo in combinations:
        current_int = int(''.join(map(str, combo)))
        if current_int < single_int:
            single_int=current_int
        
    
    finalStr= str(single_int)


    return finalStr

print(penalty(['45', '30', '50', '1']))
