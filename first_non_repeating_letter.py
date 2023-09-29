"""
First non-repeating character

Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

Status: solved"""


def first_non_repeating_letter(s):
  letter_arr=[*s]
  print (letter_arr)
  lower_arr = [x.lower() for x in letter_arr]
  print(lower_arr)
  for i in lower_arr:
    if lower_arr.count(i) == 1 and i != ' ':
      return letter_arr[lower_arr.index(i)]
  return ''

print(first_non_repeating_letter('stress'))
    
         
        




  

  

  


      


