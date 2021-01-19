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
 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Total Number of Users:

print(len(profiles))  #19

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Number of Active Users:
len([profile for profile in profiles if profile['isActive']]) #9

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Number of Inactive Users:

len([profile for profile in data if not profile['isActive']])  #10

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Grand total of balances for all users:

def dec_balance():
    for d in profiles:
        d["balance"] = d["balance"].replace("$", "")
        d["balance"] = d["balance"].replace(",", "") 
        d["balance"] = float(d["balance"])
        continue
dec_balance()

def grand_total_balances():
     grand_total_balances.total = int(0)
     for d in profiles:
        grand_total_balances.total += d["balance"]
     print(f"Grand Total of Balances of All Users:  {grand_total_balances.total}")        
grand_total_balances()


Same problem below: but with debugging print statements
def dec_balance():
    for d in profiles:
        d["balance"] = d["balance"].replace("$", "")
        print(f" - $ removed: {d['balance']}")       
        d["balance"] = d["balance"].replace(",", "") 
        print(f"   - , removed: {d['balance']}")
        d["balance"] = float(d["balance"])
        print("     changed to float")
        continue
dec_balance()

def grand_total_balances():
     grand_total_balances.total = int(0)
     for d in profiles:
        grand_total_balances.total += d["balance"]
     print(f"Grand Total of Balances of All Users:  {grand_total_balances.total}")        
grand_total_balances()   #$52667.02

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 ### Average Balance Per User: 

average_balance = round(grand_total_balances.total / (len(data)),2)
print(f"The average balance per user is ${average_balance}")  #The average balance per user is $2771.95

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### User with the lowest balance:

id_minbalance = min(profiles, key = lambda x : x["balance"])
print("The user with the lowest balance is: " + id_minbalance["_id"])  

# The user with the lowest balance is: 54e23c3e0fd8074c2ca52667


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### User with the highest balance:

id_maxbalance = max(profiles, key = lambda x : x["balance"])
print("The user with the highest balance is: " + id_maxbalance["_id"])

# The user with the highest balance is: 54e23c3e54e4094147a3b1da


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Most common favorite fruit:

import statistics 
from statistics import mode 

print(mode([d['favoriteFruit'] for d in profiles]))   #strawberry
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Least common favorite fruit: 

print(min([d['favoriteFruit'] for d in profiles]))  #apple


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Total Number of Unread Messages for All Users: 

# My coding logic didn't get me there:  

unread_messages = []
for d in profiles:
    unread = d["greeting"]
    for i in unread:
        if i.isdigit():
            unread_messages.append(i)
print(unread_messages)


#Was able to piece together code that works -- but I don't understand why it works

def number_in_msg(s):
    return ''.join([c for c in s if c.isdigit()])
unread_msgs = [number_in_msg(profile['greeting']) for profile in profiles]
sum([int(message) for message in unread_msgs])   #210
