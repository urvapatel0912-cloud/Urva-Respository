#Design a program that continuously converts inches to centimeters,
# stopping only when the user enters a negative value.

while True:
    User = float(input("Enter your Inches: "))
    if User < 0:
            break
    Cm = User * 2.54
    print(f"Here is your {User} Inches into {Cm} Centimeters")
