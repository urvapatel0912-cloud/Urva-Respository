def gallon(user):
    lr = float(user) * 3.785
    return lr

while True:
    user = float(input("Enter the volume in gallons: "))
    if user < 0:
        print("You can't enter a negative number")
        break
    print(f"{user} gallons into liters: {gallon(user)}\n")

