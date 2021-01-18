# Import Exercises

# 1. Import and test 3 of the functions from your functions exercise file.

# Import each function in a different way:

# * import the module and refer to the function with the . syntax,
# * use from to import the function directly,
# * use from and give the function a different name

# import with . syntax

import functions_exercises
functions_exercises.calculate_tip(.15,215)  #Tip amount is $32.25

# import using from
from functions_exercises import get_letter_grade
get_letter_grade(85)  # 'Your grade is: B'

# import using from and rename
from functions_exercises import handle_commas as com
com('81,345,678')  # 81345678.0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Use the `itertools module` for the following exercises

# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

from itertools import permutations 
print (len(list(permutations(['a','b','c','1','2','3'], 6))))   #720

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#2  How many different ways can you combine two of the letters from "abcd"?

print(len(list(permutations(['a', 'b', 'c','d'], 2))))   #12

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Save this file as profiles.json inside of your exercises directory. Use the load function from the 
# json module to open this file, it will produce a list of dictionaries. Using this data, write some 
# code that calculates and outputs the following information:

import json
with open('profiles.json') as profiles:
    data = json.load(profiles)
    print(data)

