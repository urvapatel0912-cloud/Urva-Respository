# Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
# - For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
# - On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

user = int(input("Enter a number: "))

if user < 2:
    print(f"{user} is not a prime number")
else:
    is_prime = True

    for divisor in range(2, user):
        if user % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{user} is a prime number")
    else:
        print(f"{user} is not a prime number")
