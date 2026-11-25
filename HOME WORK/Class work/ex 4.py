
a= int(input("Enter the first integer: "))
b= int(input("Enter the second integer: "))

for number in range(1, 1001):
        if number % a == 0 and number % b == 0:
            print("First number divisible by both:", number)
            break