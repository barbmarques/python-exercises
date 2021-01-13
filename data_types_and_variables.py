# Create a Python script file named data_types_and_variables.py. Inside it, write some 
# Python code, that is, variables and operators, to describe the following scenarios. 
# Do not worry about the real operations to get the values, the goal of these exercises 
# is to understand how real world conditions can be represented with code.


# You have rented some movies for your kids: The little mermaid (for 3 days), Brother 
# Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're 
# going to like it). If price for a movie per day is 3 dollars, how much will you have 
# to pay?

little_mermaid = 3
brother_bear = 5
hercules = 1
print(3 * (little_mermaid + brother_bear + hercules))


# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380,
# and Facebook 350. How much will you receive in payment for this week? You worked 10 
# hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google_rate = 400
amazon_rate = 380
facebook_rate = 350
google_hours = 6
amazon_hours = 4
facebook_hours = 10
--  print((6*google)+(10*facebook)+(4*amazon))
-- use dictionary for each company, with rate, hours)

# A student can be enrolled to a class only if the class is not full and the class schedule
#  does not conflict with her current schedule.

-- student_name:
-- class_1: 
-- class_2:
-- class_3:
-- class_4:

current_enroll: current number of students enrolled 
max_enroll: maximum allowable enrollment


# A product offer can be applied only if people buys more than 2 items, and the offer has not
#  expired. Premium members do not need to buy a specific amount of products.

total_items: total items purchased
is_expired: bool
is_premium: bool