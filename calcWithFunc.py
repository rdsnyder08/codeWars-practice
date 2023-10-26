"""
Calculating With Functions

Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:

Status:solved"""

import math

def zero(func=None):
    if func is None:
        return 0
    else:
        return func(0) #your code here
def one(func=None):
    if func is None:
        return 1
    else:
        return func(1) #your code here
def two(func=None):
    if func is None:
        return 2
    else:
        return func(2) #your code here
def three(func=None):
    if func is None:
        return 3
    else:
        return func(3) #your code here
def four(func=None):
    if func is None:
        return 4
    else:
        return func(4) #your code here
def five(func=None):
    if func is None:
        return 5
    else:
        return func(5)
def six(func=None):
    if func is None:
        return 6
    else:
        return func(6) 
def seven(func=None):
    if func is None:
        return 7
    else:
        return func(7)
def eight(func=None):
    if func is None:
        return 8
    else:
        return func(8) #your code here
def nine(func=None):
    if func is None:
        return 9
    else:
        return func(9) #your code here

def plus(num):
    def adder(x):
        return x+num
    return adder #your code here
def minus(num):
    def subtracter(x):
        return x-num
    return subtracter #your code here
def times(num):
    def multiplier(x):
        return x * num
    return multiplier
def divided_by(num):
    def divider(x):
        return math.floor(x/num)
    return divider#your code here


print(seven(times(five())))