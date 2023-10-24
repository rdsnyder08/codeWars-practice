"""
Directions Reduction

Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away.

The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [] (nil in Clojure).

In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

Task
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South.
The Clojure version returns nil when the path is reduced to nothing.
The Rust version takes a slice of enum Direction {North, East, West, South}.

Status: Solved
"""
def dir_reduc(arr):
    i=0
    finalArr= arr
    x=len(finalArr)
    while i<x-1:
        if finalArr[i]=="NORTH" and finalArr[i+1]=="SOUTH":
            finalArr.pop(i+1)
            finalArr.pop(i)
            i = 0
        elif finalArr[i]=="SOUTH" and finalArr[i+1]=="NORTH":
            finalArr.pop(i+1)
            finalArr.pop(i)
            i = 0

        elif finalArr[i]=="WEST" and finalArr[i+1]=="EAST":
            finalArr.pop(i+1)
            finalArr.pop(i)
            i = 0

        elif finalArr[i]=="EAST" and finalArr[i+1]=="WEST":
            finalArr.pop(i+1)
            finalArr.pop(i)
            i = 0
        
        
        
        x=len(finalArr)
        i+=1
    x=len(finalArr)
    i=0
    while i<x-1:
        if finalArr[i]=="NORTH" and finalArr[i+1]=="SOUTH":
            finalArr.pop(i+1)
            finalArr.pop(i)
            i = 0
        elif finalArr[i]=="SOUTH" and finalArr[i+1]=="NORTH":
            finalArr.pop(i+1)
            finalArr.pop(i)
            i = 0

        elif finalArr[i]=="WEST" and finalArr[i+1]=="EAST":
            finalArr.pop(i+1)
            finalArr.pop(i)
            i = 0

        elif finalArr[i]=="EAST" and finalArr[i+1]=="WEST":
            finalArr.pop(i+1)
            finalArr.pop(i)
            i = 0
        
        
        
        x=len(finalArr)
        i+=1
        
    print(finalArr)


    return finalArr