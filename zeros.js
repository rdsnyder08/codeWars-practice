/*
Number of trailing zeros of N!

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...


Status: Solved */



function zeros (n) {
    
    let fiveCounter=0
    
    while (n>= 5) {
        n=Math.floor(n/5)
        fiveCounter +=n
       
        
        
    
    }
    return fiveCounter
}
