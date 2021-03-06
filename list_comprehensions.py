# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases
#  every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

#~~~~~~~~~~~~~~~~~~~~    

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a 
# variable named uppercased_fruits to hold the output of the list comprehension. Output 
# should be ['MANGO', 'KIWI', etc...]

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

-- ['MANGO', 'KIWI', 'STRAWBERRY', 'GUAVA', 'PINEAPPLE', 'MANDARIN ORANGE']


#~~~~~~~~~~~~~~~~~~~~

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax 
# to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
capitalized_fruits = [fruit.title() for fruit in fruits]
print(capitalized_fruits)

-- ['Mango', 'Kiwi', 'Strawberry', 'Guava', 'Pineapple', 'Mandarin Orange']


#~~~~~~~~~~~~~~~~~~~~  

# Exercise 3 - Use a list comprehension to make a variable named 
# fruits_with_more_than_two_vowels. Hint: You'll need a way to check 
# if something is a vowel.

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

def is_vowel(string):
    string = string.lower()
    return string in ["a", "e", "i", "o", "u"]

def count_vowels(string):
    count = 0
    for letter in string:
        if is_vowel(letter):
            count += 1
    return count

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) > 2]

print(fruits_with_more_than_two_vowels)
            
-- ['mango', 'kiwi', 'strawberry']


#~~~~~~~~~~~~~~~~~~~~   

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

def is_vowel(string):
    string = string.lower()
    return string in ["a", "e", "i", "o", "u"]

def count_vowels(string):
    count = 0
    for letter in string:
        if is_vowel(letter):
            count += 1
    return count

fruits_with_only_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) == 2]

print(fruits_with_only_two_vowels)

-- ['mango', 'kiwi', 'strawberry']


#~~~~~~~~~~~~~~~~~~~~   


# Exercise 5 - make a list that contains each fruit with more than 5 characters

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_more_than_five_characters = [fruit for fruit in fruits if len(fruit) > 5]
print(fruits_with_more_than_five_characters)

-- ['strawberry', 'pineapple', 'mandarin orange']


#~~~~~~~~~~~~~~~~~~~~   
# Exercise 6 - make a list that contains each fruit with exactly 5 characters

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_five_characters = [fruit for fruit in fruits if len(fruit) == 5]
print(fruits_with_five_characters)

-- ['mango', 'guava']

#~~~~~~~~~~~~~~~~~~~~   
# Exercise 7 - Make a list that contains fruits that have less than 5 characters

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_less_than_five_characters = [fruit for fruit in fruits if len(fruit) < 5]
print(fruits_with_less_than_five_characters)

-- ['kiwi']

#~~~~~~~~~~~~~~~~~~~~   
# Exercise 8 - Make a list containing the number of characters in each fruit. Output
#  would be [5, 4, 10, etc... ]

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

number_of_characters = [len(fruit) for fruit in fruits]
print(number_of_characters)

-- [5, 4, 10, 5, 9, 15]

#~~~~~~~~~~~~~~~~~~~~   
# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only 
# the fruits that contain the letter "a"

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruits_with_letter_a)
            
-- ['mango', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
#~~~~~~~~~~~~~~~~~~~~  
#  
# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

even_numbers = [number for number in numbers if number%2 == 0] 
print(even_numbers)

-- [2, 4, 6, 8, 10, 256, -8, -4, -2]

#~~~~~~~~~~~~~~~~~~~~  
 
# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

odd_numbers = [number for number in numbers if number%2 == 1] 
print(odd_numbers)

-- [3, 5, 7, 9, 11, 13, 17, 19, 23, 5, -9]
#~~~~~~~~~~~~~~~~~~~~  
 
# Exercise 12 - Make a variable named positive_numbers that holds only the 
# positive numbers

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

positive_numbers = [number for number in numbers if number > 0] 
print(positive_numbers)

-- [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, 5]

#~~~~~~~~~~~~~~~~~~~~   
# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

negative_numbers = [number for number in numbers if number < 0] 
print(negative_numbers)

--  [-8, -4, -2, -9]

#~~~~~~~~~~~~~~~~~~~~   

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of
#  numbers with 2 or more numerals

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

two_or_more_digits = [number for number in numbers if len(str(abs(number))) >= 2] 
print(two_or_more_digits)

-- [10, 11, 13, 17, 19, 23, 256]

#~~~~~~~~~~~~~~~~~~~~  

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list
#  with each element squared. Output is [4, 9, 16, etc...]

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
numbers_squared = [(number ** 2) for number in numbers] 
print(numbers_squared)

-- [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 169, 289, 361, 529, 65536, 64, 16, 4, 25, 81]

#~~~~~~~~~~~~~~~~~~~~   

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers 
# that are both odd and negative.

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

odd_and_negative = [number for number in numbers if (number % 2 == 1) and (number < 0)] 
print(odd_and_negative)

-- [-9]

#~~~~~~~~~~~~~~~~~~~~   
# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing 
# each number plus five. 

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

numbers_plus_five = [(number + 5) for number in numbers] 
print(numbers_plus_five)

-- [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 22, 24, 28, 261, -3, 1, 3, 10, -4] 

#~~~~~~~~~~~~~~~~~~~~   
# BONUS Make a variable named "primes" that is a list containing the prime numbers 
# in the numbers list. *Hint* you may want to make or find a helper function that 
# determines if a given number is prime or not.

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

primes = [number for number in numbers if (number > 1) and (for i in range(2, number):
             if (number % i) != 0 )] 
print(primes)