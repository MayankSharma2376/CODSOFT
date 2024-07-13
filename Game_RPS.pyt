import random

"""
'r' for Rock, 's' for Scissors, 'p' for Paper
Rock beats Scissors, Scissors beats Paper, Paper beats Rock
"""

# Define a function to play the game
def func_play():

# Take input from user
    input1 = input("Enter your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors")
    user_input = input1.lower()

# Create variable for computer_input
    computer_input = random.choice(['r', 'p', 's'])
    
#Check the condition
    if (user_input == computer_input):
        print("It\'s a tie'")
    if func_is_win(user_input, computer_input):
        return "You Won!"
    return "You Lost"
  

# Define a function to Players      
def func_is_win(var_player, var_opponent):
    if(var_player == 'r' and var_opponent == 's') or (var_player == 's' and var_opponent == 'p') or (var_player == 'p' and var_opponent == 'r'):
        return True
# Call function
result = func_play()
print(result)

# Ask user to play again
print("Choose the option to play again (yes,no)")
another_round = input().strip()
if another_round == "yes":
    print(result)
else:
    print("Thanks for playing")