#Develop a game where the computer picks a random number between 1 and 10, and the user attempts to guess it.
# After each guess, the program provides feedback:Too high,Too low, orCorrect.
# The number remains the same throughout the game until the user guesses correctly.
import random

Number = random.randint(1, 10)

while True:
    user = int(input("Enter your gusse level:"))
    if user > Number:
        print(f"Your guess is too high")

    elif user < Number:
        print(f"Your guess is too Low")
    else:
        print("Your guess is correct")
        break



