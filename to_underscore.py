"""
Convert PascalCase string into snake_case

Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. 

Lowercase characters can be numbers. 

If the method gets a number as input, it should return a string.

Status: solved
"""


def to_underscore(string):
    if type(string) == int:
        return str(string)
    uppers = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    snake = ['_a','_b','_c','_d','_e','_f','_g','_h','_i','_j','_k','_l','_m','_n','_o','_p','_q','_r','_s','_t','_u','_v','_w','_x','_y','_z']
    for i in string:
        if i in uppers:
            index= uppers.index(i)
            string = string.replace(uppers[index], snake[index] )
    return string[1:]