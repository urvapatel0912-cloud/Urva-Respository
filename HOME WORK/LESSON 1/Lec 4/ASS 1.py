#Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers.
# Use a for loop.

import random

User = int(input("How many dice do you want to roll? : "))
total = 0

for count in range(User):
    roll = random.randint(1, 6)
    print(f"Die {count + 1}: {roll}")
    total = total + roll

print(f"Sum of all dice:{total}")
