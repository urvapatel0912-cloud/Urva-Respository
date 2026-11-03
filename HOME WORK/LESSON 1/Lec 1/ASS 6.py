#Write a program that generates two random combinations of numbers for a combination lock:
#A 3-digit code where each number is between 0 and 9.
#A 4-digit code where each number is between 1 and 6.

import random

digit1 = random.randint(0, 9)
digit2 = random.randint(0, 9)
digit3 = random.randint(0, 9)

num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
num3 = random.randint(1, 6)
num4 = random.randint(1, 6)

print("3-digit code:", digit1, digit2, digit3)
print("4-digit code:", num1, num2, num3, num4)