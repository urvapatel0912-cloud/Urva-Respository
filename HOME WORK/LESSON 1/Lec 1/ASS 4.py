#Write a program that asks the user for three integer numbers.
#The program prints out the sum, product, and average of the numbers
num1 = int(input("Enter integer 1: "))
num2 = int(input("Enter integer 2: "))
num3 = int(input("Enter integer 3: "))

sum = int(num1 + num2 + num3)
product =int(num1 * num2 * num3)
avg = sum / 3

print("The sum is: ", sum)
print("The product is: ", product)
print("The product is: ", avg)
