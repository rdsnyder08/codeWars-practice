function tribonacci(signature,n){
    let accumulator = signature;
    while (accumulator.length <= n){
        for (i in accumulator) {
            let newValue = accumulator[i]+accumulator[i+1]+accumulator[i+2]
            console.log(newValue)
        }
    }
    return accumulator

  
}

console.log(tribonacci([1,1,1], 10))