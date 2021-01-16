# 1. Define a function named is_two. It should accept one input and return True if the 
# passed input is either the number or the string 2, False otherwise.


# is_two defines a single parameter, n, which can be anything, and returns a boolean value

def is_two(n):
   return n == 2 or  n == '2':

      
is_two(2)
is_two(6)
is_two('5')
is_two('2')






#---------------------------

#2  Define a function named is_vowel. It should return True if the passed string is a vowel, 
# False otherwise.

# string --> boolean
def is_vowel(n):
    return n.lower() in('aeiou')
   
is_vowel('t')
#is_vowel('A')
#is_vowel('3')
#is_vowel('i')
#is_vowel('u')

#---------------------------

#3. Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(c):
    return c.isalpha() and not is_vowel(c)


is_consonant('t')  # True
is_consonant('A')  # False
is_consonant('3')   #False
is_consonant('B')  # True

#---------------------------

#4. Define a function that accepts a string that is a word. The function should capitalize the first 
#letter of the word if the word starts with a consonant.

def capitalize_if_consonant(word):
    first_letter = word[0]
    if is_consonant(first_letter):
        return word.title()
    else: 
        return word

initial_cap('hello')   #'Hello'
initial_cap('apple')   #'apple'        

#---------------------------

#5.  Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.

def calculate_tip(percentage,total):
    amount_to_tip = (percentage * total)
    amount_to_tip = round(amount_to_tip,2)
    return (f'Tip amount is ${amount_to_tip}')

calculate_tip(.10,523.17) #'Tip amount is $52.32'


#---------------------------

#6. Define a function named apply_discount. It should accept a original price, and a discount 
#  percentage, and return the price after the discount is applied.

def apply_discount(orig_price,disc_perc):
    discount = (orig_price * disc_perc)
    new_price = orig_price - discount
    return (f'The discounted price is: ${new_price}')

apply_discount(534.60,.10)  #'The discounted price is: $481.14'

#---------------------------

#7.  Define a function named handle_commas. It should accept a string that is a number that contains 
# commas in it as input, and return a number as output.

# handle_commas(s: str) --> float

def handle_commas(number):
    return float(number.replace(',',''))
    

handle_commas('76,100,020,880')  # 76100020880.0
#---------------------------

#8. Define a function named get_letter_grade. It should accept a number and return the letter grade 
# associated with that number (A-F).

# get_letter_grade(numeric: float) --> str

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

# remove_vowels(s: str) --> str

def remove_vowels(string):
    #look at each letter in hte string
    # if it's a vowel, it should not be included in the 
    #new string
    new_string = []
    for character in string:
        if not is_vowel(character):
            new_string.append(character)
    #change list to string using ''.join            
    return ''.join(new_string)

remove_vowels('abcdefghijklmnopqrstuvwxyz')  #'bcdfghjklmnpqrstvwxyz'

# ANOTHER WAY :
def remove_vowels(string):
    return "".join([c for c in string if not is_vowel(c)])

remove_vowels("Wow. This is amazing!") #'Ww. Ths s mzng!'



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


# a better way:
def normalize_name(name):
    name = name.lower()
    name = name.strip()
    name = name.replace(' ','_')
   
    output = ''
    for letter in name: 
        if letter.isidentifier():
            output += letter
    return output

normalize_name('    BA@rba##ra M*ar&q%%u+es  ')  # 'barbara_marques'

####  Zach's way:  (includes debugging print lines)

#normalize_name(s: str)  --> str
def normalize_name(s):
    valid_identifier = []
    #remove anything that's not whitespace or alphanum
    print("Removing non-whitespace or alnum")
    print()
    for character in s:
        print(f"- Inside for loop. Processing {character}")
        if character.isidentifier() or character == ' ':
            print(f"   Adding {character} to list...")
            valid_identifier.append(character)
        print(f"    valid_identifier: {valid_identifier}")
    #convert back to string
    valid_identifier = "".join(valid_identifier)
    valid_identifier = valid_identifier.lower()
    print("Lowercased and converted to a string.")
    valid_identifier = valid_identifier.strip()
    valid_identifier = valid_identifier.replace(" ","_")
    return valid_identifier

normalize_name('Ha#b$c%d^e&f*g(h!)')  #'habcdefgh'





#11  Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the 
# cumulative sum of the numbers in the list.
#       cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#       cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

#cumulative_sum(l: list[int]) --> list[int]

def cumulative_sum(num_list):
    sums = [num_list[0]]
    print(f"Starting out. sums: {sums}")
    # for each number in the list, add it to the previous total
    for n in num_list[1:]:
        print(f"- Start of for loop. Processing {n}")
        previous_total = sums[-1]
        sums.append(previous_total + n)
        print(f"    End of for loop. sums: {sums}")
    
cumulative_sum([1,2,3,4,5,6,7,8,9,10])  #
# Starting out. sums: [1]
# - Start of for loop. Processing 2
#     End of for loop. sums: [1, 3]
# - Start of for loop. Processing 3
#     End of for loop. sums: [1, 3, 6]
# - Start of for loop. Processing 4
#     End of for loop. sums: [1, 3, 6, 10]
# - Start of for loop. Processing 5
#     End of for loop. sums: [1, 3, 6, 10, 15]
# - Start of for loop. Processing 6
#     End of for loop. sums: [1, 3, 6, 10, 15, 21]
# - Start of for loop. Processing 7
#     End of for loop. sums: [1, 3, 6, 10, 15, 21, 28]
# - Start of for loop. Processing 8
#     End of for loop. sums: [1, 3, 6, 10, 15, 21, 28, 36]
# - Start of for loop. Processing 9
#     End of for loop. sums: [1, 3, 6, 10, 15, 21, 28, 36, 45]
# - Start of for loop. Processing 10
#     End of for loop. sums: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

