# 1. Define a function named is_two. It should accept one input and return True if the 
# passed input is either the number or the string 2, False otherwise.

def is_two(n):
    if n == 2 or n == 'two':
        return True
    else:
        return False

is_two(6) #False
is_two(2) #True
is_two('five') #False
is_two('two') #True

#---------------------------

#2  Define a function named is_vowel. It should return True if the passed string is a vowel, 
# False otherwise.

def is_vowel(n):
    if n.lower() in('a', 'e', 'i', 'o', 'u'):
        return True
    else:
        return False
    
is_vowel('t') #False
is_vowel('A') #True
is_vowel('3') #False
is_vowel('i') #True
is_vowel('u') #True

#---------------------------

#3. Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(n):
    if n.lower() not in('a', 'e', 'i', 'o', 'u'):
        return True
    else:
        return False

is_consonant('t')  # True
is_consonant('A')  # False
is_consonant('B')  # True

#---------------------------

#4. Define a function that accepts a string that is a word. The function should capitalize the first 
#letter of the word if the word starts with a consonant.

def initial_cap(word):
    word == word.lower()
    if word[0] not in('a', 'e', 'i', 'o', 'u'):
            return word.title()

initial_cap('hello')   #'Hello'
initial_cap('apple')   # nothing returns        

#---------------------------

#5.  Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.

def calculate_tip(percentage,total):
    amount_to_tip = (percentage * total) / 100
    return (f'Tip amount is ${amount_to_tip}')

calculate_tip(10,500)  # 'Tip amount is $50.0'


#---------------------------

#6. Define a function named apply_discount. It should accept a original price, and a discount 
#  percentage, and return the price after the discount is applied.

def apply_discount(orig_price,disc_perc):
    discount = (orig_price * disc_perc) / 100
    new_price = orig_price - discount
    return (f'The discounted price is: ${new_price}')

apply_discount(500,10)  # 'The discounted price is: $450.0'

#---------------------------

#7.  Define a function named handle_commas. It should accept a string that is a number that contains 
# commas in it as input, and return a number as output.

def handle_commas(number):
    number = int(number.replace(',',''))
    return number

handle_commas('76,100,020,880')  # '76100020880'

#---------------------------

#8. Define a function named get_letter_grade. It should accept a number and return the letter grade 
# associated with that number (A-F).

def get_letter_grade(number):
    if int(number) >= 90:
        letter = 'A'
    elif int(number) >= 80:
        letter = 'B'
    elif int(number) >= 70:
        letter = 'C'
    elif int(number) >= 60:
        letter = 'D'
    else:
        letter = 'F'
    return (f'Your grade is: {letter}')

get_letter_grade('82')  #'Your grade is: B'

#9  Define a function named remove_vowels that accepts a string and returns a string with all the vowels 
#  removed.

def remove_vowels(letters):
    letters = letters.replace('a','')
    letters = letters.replace('e','')
    letters = letters.replace('i','')
    letters = letters.replace('o','')
    letters = letters.replace('u','')
    letters = letters.replace('A','')
    letters = letters.replace('E','')
    letters = letters.replace('I','')
    letters = letters.replace('O','')
    letters = letters.replace('U','')
    return letters

remove_vowels('This sentence has no vowels.')  #'Ths sntnc hs n vwls.'
remove_vowels('ABCDEFGHIJKLMNOPQRSTUVWXYZ')   #'BCDFGHJKLMNPQRSTVWXYZ'
remove_vowels('abcdefghijklmnopqrstuvwxyz')   #'bcdfghjklmnpqrstvwxyz'

#10  Define a function named normalize_name. It should accept a string and return a valid python 
# identifier, that is:
# anything that is not a valid python identifier should be removed
#   leading and trailing whitespace should be removed
#   everything should be lowercase
#   spaces should be replaced with underscores
#       for example:
#           Name will become name
#           First Name will become first_name
#           % Completed will become completed

def normalize_name(name):
    bad_chars = ['~', '!','@','#','$','%','^','&','*','(',')','-','.','+']
    name = ''.join((filter(lambda x: x not in bad_chars,name)))     
    name = name.strip()
    name = name.replace(' ','_')
    name = name.lower()
    return name

normalize_name('    BA@rba##ra M*ar&q%%u+es  ')  #'barbara_marques'

#11  Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the 
# cumulative sum of the numbers in the list.
#       cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#       cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

