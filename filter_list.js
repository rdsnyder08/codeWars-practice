function filter_list(l) {
    numbers =[]
    for (i=0 ; i<l.length;  i++){
        if (typeof l[i] === "number"){
            numbers.push(l[i])
        }
    }   
    return numbers

    // Return a new array with the strings filtered out
}


console.log(filter_list([1,2,'a','b']))