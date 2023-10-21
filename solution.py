"""
Range Extraction

A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Status: Solved
"""


def solution(args):
    finalArr=[]
    skippedArr=[]
    for i in args:
        if i+1 in args and i-1 in args:
            skippedArr.append(i)
        else: 
            finalArr.append(i)
    print(skippedArr)
    finalStr=''
    for i in finalArr:
        if i-1 in skippedArr:
            finalStr+='-'
        else:
            finalStr+=','
        finalStr+=str(i)

    finalStr=finalStr[1:]
        
    
    return finalStr







print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))