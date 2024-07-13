import random # import random module

# Define a variable name numbers with values
numbers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*"

# Define length of the password
length_password = int(input("Enter the length of the Password : "))

# Declare a variable with join function
m = "".join(random.sample(numbers, length_password))

# Print the password
print(f"Your Password is {m}")