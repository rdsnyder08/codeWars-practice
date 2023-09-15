#Moving Zeros To The End

#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

#status: Solved

def move_zeros(lst):
    counter=0
    final_lst=[]
    for i in (lst):
        if i==0:
            counter+=1
        if i != 0:
            final_lst.append(i)
        
            
    while counter > 0:
        final_lst.append(0)
        print(final_lst)
        counter-=1
            
    


    return final_lst


print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))