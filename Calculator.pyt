#Program For Simple Calculator 


# Create a Function for Addition of Two Numbers
def add(num1, num2):
    return num1 + num2

# Create a Function for Subtraction of Two Numbers
def diff(num1, num2):
    return num1 - num2

# Create a Function for Multiplication of Two Numbers
def multi(num1, num2):
    return num1 * num2

# Create a Function for Division of Two Numbers
def div(num1, num2):
    return num1 / num2

# Take input from user for num1 and num2
num1 = float(input("Enter the value of Number1 : "))
num2 = float(input("Enter the value of Number2 : "))

#Prompt user choose the operation
print("Choose the operation (+, -, *, /):")
operation = input().strip()

#Check the type of operation and perform Calculations
if operation == "+":
    print("The Addition of num1 and num2 is", add(num1, num2))
    
elif operation == "-":
    print("The Subtraction of num1 and num2 is", diff(num1, num2))

elif operation == "*":
    print("The Multiplication of num1 and num2 is", multi(num1, num2))
    
elif operation == "/":
    print("The Division of num1 and num2 is", div(num1, num2))
    
else:
    print("Invalid Operation!")