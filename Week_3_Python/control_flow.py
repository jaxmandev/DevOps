# if, elif and else
# Using operators ==, >, etc..
# Check age restrictions before selling the ticket
# Over 18, 15, 12, PG, U
# else block should ensure to display message if other conditions

age = int(input("Please enter your age  "))

if age >= 18:
    print('You are eligable to watch any movie')
elif age >= 15:
    print("You are eligable to watch movies up to the 15 rating")
elif age >= 12:
    print("You are eligable to watch movies up to the 12A rating")
elif age >= 7:
    print("You are eligable to watch movies up to the PG rating while accompanied by an adult")
elif age >= 4:
    print("You, sir, can only watch movies that have the U rating")
else:
    print("There has been a problem, please retype your age or try again later")

Day 2 - Control Flow

if, elif and else statements as well as: for loops and while loops

if elif:

# Control Flow
# if statements
# Synatx: if then condition

user_age = 14

if user_age >= 15:
    print('Thank you for booking the ticket')
elif user_age < 15:
    print("Sorry, you are not of the right age to watch this movie")
else:
    print("Sorry something went wrong, try again later")


# Create a program using control flow with if, elif and else
# Using operators ==, >, etc..
# Check age restrictions before selling the ticket
# Over 18, 15, 12, PG, U
# else block should ensure to display message if other conditions

age = int(input("Please enter your age  "))

if age >= 18:
    print('You are eligable to watch any movie')
elif age >= 15:
    print("You are eligable to watch movies up to the 15 rating")
elif age >= 12:
    print("You are eligable to watch movies up to the 12A rating")
elif age >= 7:
    print("You are eligable to watch movies up to the PG rating while accompanied by an adult")
elif age >= 4:
    print("You, sir, can only watch movies that have the U rating")
else:
    print("There has been a problem, please retype your age or try again later")
for loops

# Loops for loop and while loop
# for loop is used to iterate through the data 1 by 1 for example
# Syntax for variable name in name_of_data collection_variable

shopping_list = ['eggs', 'milk', 'supermalt']
print(shopping_list)

for item in shopping_list:
    if item == 'milk':
        print(item)

sparta_user_details = {
    'first_name' : 'Charlie',
    'last_name' : 'Shelby',
    'dob' : '22/10/1997',
    'address' : '74 Privet Drive',
    'course' : 'DevOps',
    'grades' : ['A*', 'A', 'A'],
    'hobbies' : ['running', 'reading', 'hunting']
}
# To print keys and values use a for loop
for i, j in sparta_user_details.items():
        if isinstance(j, list):
            print(f"Key: {i}")
            for k in j:
                print(f"List Value: {k}")
        else:
            print(f"Key: {i}, Value: {j}")
while loops

while loops is not regularly used however you do see it used for monitoring
Key words like break and continue help control the flow of our loop
# While Loops!
# break and continue can be used to control the flow of the loop
# Syntax: while variable_name condition value:
number = 0

while number < 10:
    print(f"It's working -> {number}" )
    if number == 4:
        break
    number += 1

# Take user input and use while loop

user_prompt = True

while user_prompt:
    age = input("Please enter your age")
    # Note: this user input is within our while loop therefore it'll prompt the user
    # until we get desired input
    if age.isdigit() and int(age) < 117:
        # isdigit() checks if the input is all digits
        user_prompt = False
    else:
        print("Please provide age in digits")
print(f"Your age is {age} ")
# Can also use isinstance(variable, data_type) e.g. isinstance(age, int) does the same thing
