#Write a program that prompts the user t enter numbers until they leave the input blank.
# nce the input steps, the program outputs the smallest and largest numbers entered.

smallest = None
largest = None

while True:
    user = input("Enter a number: ")

    if user == "":
        break

    number = float(user)

    if smallest is None or number < smallest:
        smallest = number

    if largest is None or number > largest:
        largest = number

if smallest is None:
    print("You did not enter any numbers.")
else:
    print("\nSmallest number:", smallest)
    print("Largest number:", largest)