/*Array.diff

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order. 

status: passed/completed */




function arrayDiff(a, b) {
    parsedArr = []
    for (i in a){
        console.log(a[i])
        if (!b.includes(a[i])){
            parsedArr.push(a[i])
        }
    }
    return parsedArr
  
}

console.log(arrayDiff([1,2,2,2,3],[2]))