# Question 2


# Task 1
# Write a script that asks for and checks the length of the user's first name and last name.
# Both should be at least 2 characters long. If not, print an error message.


# Ask for user's first name and last name
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

# Check the length of the names
if len(first_name) < 2:
    print("Error: Your first name should be at least 2 characters long.")
if len(last_name) < 2:
    print("Error: Your last name should be at least 2 characters long.")