# Create a Python script file named data_types_and_variables.py. Inside it, write some 
# Python code, that is, variables and operators, to describe the following scenarios. 
# Do not worry about the real operations to get the values, the goal of these exercises 
# is to understand how real world conditions can be represented with code.


# You have rented some movies for your kids: The little mermaid (for 3 days), Brother 
# Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're 
# going to like it). If price for a movie per day is 3 dollars, how much will you have 
# to pay?

little_mermaid_days = 3  #Variables hold nouns
brother_bear_days = 5
hercules_days = 1
price_per_movie = 3


print(3 * (little_mermaid + brother_bear + hercules))

-- 27

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
amazon_subtotal = amazon_hours * amazon_rate
google_subtotal = google_hours * google_rate
facebook_subtotal = facebook_hours * facebook_rate
total = amazon_subtotal + facebook_subtotal + google_subtotal

f"${total} is the total of consulting with these companies"

-- '$7420 is the total of consulting with these companies'


# A student can be enrolled to a class only if the class is not full and the class schedule
#  does not conflict with her current schedule.

class_has_space = True
schedule_works = True
can_be_enrolled = class_has_space and schedule_works
can_be_enrolled 

--  True
# A product offer can be applied only if people buys more than 2 items, and the offer has not
#  expired. Premium members do not need to buy a specific amount of products.

has_not_expired = True
buys_two_or_more = True
is_premium_member = True
offer_available = has_not_expired and (buys_two_or_more or is_premium_member)
offer_available

-- True


# Use the following code to follow the instructions below:

# username = 'codeup'
# password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:

-- the password must be at least 5 characters
-- the username must be no more than 20 characters
-- the password must not be the same as the username
-- bonus neither the username or password can start or end with whitespace
#~~~~~~~~~~~~~~~~~~~~
if username[0] != ' ' and username[-1] != ' '
and password[0] != ' ' and password[0] != ' '
#~~~~~~~~~~~~~~~~~~~

pw_is_at_least_five_characters = len(password) >= 5
username_less_than_twenty  == len(username) <= 20
password_differs_from_username = username != password
password_no_begin_or_end_whitespace =  password == password.strip()
username_no_begin_or_end_whitespace =  username == username.strip()