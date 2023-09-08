function isPrime(num) {
    if (num < 2){
        return false
    }
    if (num %2 === 0){
        return false
    }
    if (num %3 === 0){
        return false
    }
    if (num %5 === 0){
        return false
    }
    if (num %7 === 0){
        return false
    }
    if (num %11 === 0){
        return false
    }
    if (num %13 === 0){
        return false
    }
    if (num %17 === 0){
        return false
    }
    if (num %19 === 0){
        return false
    }
    

    let list_o_primes = []
    let list_o_composites=[]
    let n=2
    
    while (n <= num){
        if (!list_o_composites.includes(n)){
            //console.log(n, ' is prime')
            list_o_primes.push(n)
            let p=2
            while (n*p <= num){
                list_o_composites.push(p*n)
                p++
            }
            
        }
        n++
    }
    if (list_o_primes.includes(num)){
        return true
    } else {
        return false
    }

 
}

console.log(isPrime(0), '0')
console.log(isPrime(1), '1')
console.log(isPrime(2), '2')
console.log(isPrime(73), '73')
console.log(isPrime(75), '75')
console.log(isPrime(-1), '-1')