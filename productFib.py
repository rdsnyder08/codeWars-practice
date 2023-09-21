'''
Product of consecutive Fib numbers

DESCRIPTION:
The Fibonacci numbers are the numbers in the following integer sequence (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.

productFib(714) # should return (21, 34, true), 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return (34, 55, false), 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
-----
productFib(714) # should return [21, 34, true], 
productFib(800) # should return [34, 55, false], 
-----
productFib(714) # should return {21, 34, 1}, 
productFib(800) # should return {34, 55, 0},        
-----
productFib(714) # should return {21, 34, true}, 
productFib(800) # should return {34, 55, false}, 




status: Solved!


'''


def productFib(prod):
    fib_one= 0
    fib_two=1
    while (fib_one*fib_two < prod):
        new_fib = fib_one + fib_two
        fib_one = fib_two
        fib_two = new_fib
        print(fib_two)
    if fib_one*fib_two == prod:
        return [fib_one , fib_two , True]
    if fib_one*fib_two != prod:
        return [fib_one , fib_two , False]