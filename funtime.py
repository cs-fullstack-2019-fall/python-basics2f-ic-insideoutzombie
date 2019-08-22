# Problem 1:
# Write the code to create a random number from 1 - 100. Print the number generated.

import random
# randomNumber = random.randint(1, 100)
#
# print(randomNumber)

### Problem 2:
##### We will keep having this problem until EVERYONE gets it right without help
# Write some python code that has a loop that prompts the
# User for string input, and will only stop after the User enters ```q```.
# If the user doesn't enter ```q```, then prompt them to input another string.
# Continuing asking for input until they enter ```q```.
#
# *NOTE: Your code should handle both lower and uppercase ```q``` values.
# userInput = input("Enter somehting bruh ")
#
# while (userInput != 'q'):
#
#     userInput = input("Enter a name ")
#
#     print(userInput)

userInput = ""
while(userInput != 'q'):
    userInput = input("Enter a string. q to quit ")
    userInput = userName.upper()


# ### Problem 4:
# Write some Python code that creates a random number from 1 - 10 and stores it in a variable.
# Ask the user to guess the random number.
# Keep letting the user guess until they get it right, then quit.
# Print the message ```Sorry, incorrect``` for each wrong guess.
randomNumber = random.randint(1, 10)
userGuess = ''
while (userGuess != randomNumber):
    userGuess = int(input("Enter a number "))
    if(userGuess == randomNumber):
        print("success")
    else:
        userGuess = int(input("sorry incorrect "))


# nameList = ""
# while (userName != 'q'):
#     nameList = nameList + " - " + userName
#     userName = input("Enter a name ")
#
#     print(nameList)
