#Conditional Basics

#~~~~~~~~~~~~~~~~~~~~~

#1a. prompt the user for a day of the week, 
#    print out whether the day is Monday or not

x = input("What is the day of the week? ")
if 'mon' in x.lower():
    print('Today is Monday.')
else:
    print('Today is not Monday.')

-- What is the day of the week? Monday
-- Today is Monday.  

-- What is the day of the week?  Saturday
-- Today is not Monday.

#~~~~~~~~~~~~~~~~~~~~~

#1b. prompt the user for a day of the week, print 
#    out whether the day is a weekday or a weekend

x = input("Enter a day of the week. ")
if 'sat' in x.lower():
    print('It is a weekend.')
elif 'sun' in x.lower():
    print('It is a weekend.')
else:
    print('It is a weekday.')

-- Enter a day of the week. Monday
-- It is a weekday.

-- Enter a day of the week. sunday
-- It is a weekend.

#~~~~~~~~~~~~~~~~~~~~~

#1c  create variables and make up values for
-- the number of hours worked in one week
-- the hourly rate
-- how much the week's paycheck will be
-- write the python code that calculates the weekly paycheck. You get paid time and a half if you work 
-- more than 40 hours

hours_worked = 50
hourly_rate = 250
if hours_worked <= 40:
    paycheck_amount = hours_worked * hourly_rate
else:
    paycheck_amount = hours_worked * hourly_rate * 1.5
print("$",paycheck_amount)

-- $ 18750.0


#~~~~~~~~~~~~~~~~~~~~~

# 2.  Loop Basics - While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i 
# by one.

i = 5
while i <= 15: 
    print(i)
    i += 1
-- 5
-- 6
-- 7
-- 8
-- 9
-- 10
-- 11
-- 12
-- 13
-- 14
-- 15

#~~~~~~~~~~~~~~~~~~~~~

#2.2  Create a while loop that will count by 2's starting with 0 and 
#       ending at 100. Follow each number with a new line.

i = 0
while i <= 100: 
    print(i)
    i += 2

#~~~~~~~~~~~~~~~~~~~~~


#2.3 Alter your loop to count backwards by 5's from 100 to -10
 
 i = 100
while i >= -10: 
    print(i)
    i -= 5

#~~~~~~~~~~~~~~~~~~~~~


#2.4  Create a while loop that starts at 2, and displays the number
#      squared on each line while the number is less that 1,000,000

i = 2
while i <= 1_000_000: 
    print(i)
    i *= i

-- 2
-- 4
-- 16
-- 256
-- 65536

#~~~~~~~~~~~~~~~~~~~~~

#2.5    Write a loop that uses print to create the output shown below. 
# (Counting back by five from 100 to 5)

i = 100
while i >= 5: 
    print(i)
    i -= 5


#~~~~~~~~~~~~~~~~~~~~~
    
#2b - For Loops

#2.b.i  Write some code that prompts the user for a number, then
# shows a multiplication table up through 10 for that number. 

x = int(input("Enter a number."))
for i in range (1,11):
    print(x,"x",i,"=",x * i)

-- Enter a number.12
-- 12 x 1 = 12
-- 12 x 2 = 24
-- 12 x 3 = 36
-- 12 x 4 = 48
-- 12 x 5 = 60
-- 12 x 6 = 72
-- 12 x 7 = 84
-- 12 x 8 = 96
-- 12 x 9 = 108
-- 12 x 10 = 120


#~~~~~~~~~~~~~~~~~~~~~
 
#2.b.ii.  Create a for loop that uses print to create the output shown below:
1
22
333
4444
55555
666666
7777777
88888888
999999999

for i in range (1,10):
    print(str(i) * i)

#~~~~~~~~~~~~~~~~~~~~~

#2.c:  Break and continue

# Prompt the user for an odd number between 1 and 50. Use a loop and a break 
# statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). Use a loop 
# and the continue statement to output all the odd numbers between 1 and 50,
# except for the number the user entered.

for x in range(1,50):
    x = int(input("Enter an ODD number between 1 and 50.  "))      
    if (x % 2) != 1:
        print("Your number is not an odd number. Try again!")
    elif x < 1:
        print("Your number is not between 1 and 50. Try again!")
    elif x > 50:
        print("Your number is not between 1 and 50. Try again!")
    else:
        print("very good!")
        break
print('Number to skip is: ',x)
for n in range(1,50):
    if (n % 2) != 0 and n != x:
        print("Here is an odd number: ",n)
    elif n == x:
        print("Yikes! Skipping number: ", x)


#~~~~~~~~~~~~~~~~~~~~~

# 2.d The input function can be used to prompt for input and use that input in 
# your python code. Prompt the user to enter a positive number and write a loop 
# that counts from 0 to that number. (Hints: first make sure that the value the 
# user entered is a valid number, also note that the input function returns a 
# string, so you'll need to convert this to a numeric type.)

for n in range(1,51):
    x = input("Enter a positive number.  ")
    if x.isdigit() == False or int(x) <= 0:
        print("That is not a positive number. Try Again!")
        continue
    else:
        for number in range(0,int(x)+1):
            print(number)
            number += 1
    break
            

#~~~~~~~~~~~~~~~~~~~~~

#2e.  Write a program that prompts the user for a positive integer. Next write 
# a loop that prints out the numbers from the number the user entered down to 1.

for n in range(1,51):
    x = input("Enter a positive number.  ")
    if x.isdigit() == False or int(x) <= 0:
        print("That is not a positive number. Try again!")
        continue
    else:
        for number in range(int(x),0,-1):
            print(number)
            number -= 1
    break
  
-- Enter a positive number.  6
-- 6
-- 5
-- 4
-- 3
-- 2
-- 1


#~~~~~~~~~~~~~~~~~~~~~

#3 Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

-- for n in range(1,101):
--  if n % 3 == 0 and n % 5 == 0:
--     print("FizzBuzz")
--  elif n % 3 == 0:
--     print("Fizz")
--  elif n % 5 == 0:
--     print("Buzz")
--   else:
--     print(n)


# Display a table of powers.
-- Prompt the user to enter an integer.
-- Display a table of squares and cubes from 1 to the value entered.
-- Ask if the user wants to continue.
-- Assume that the user will enter valid data.
-- Only continue if the user agrees to.


#4  
# 
x = input("What number would you like to go up to?  ")

for n in range(1,int(x) + 1):
    print(n,n**2,n**3)
y = input("Do you want to continue? Type yes or no:  ")
while y == "yes":
    x = input("What number would you like to go up to?  ")
    for n in range(1,int(x) + 1):
        print(n,n**2,n**3)
    y = input("Do you still want to continue? Type yes or no:  ")       
print("Thank you for playing.")

    