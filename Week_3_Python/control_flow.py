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
