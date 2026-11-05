user=input("Enter your class: ").upper()
if user == "lux":
    print("You have upper-deck cabin with a balcony.")

elif user == "A":
    print("You have cabin above the car deck with a window.")

elif user == "B":
    print("You have windowless cabin above the car deck.")

elif user == "C":
    print("You have windowless cabin below the car deck.")

else :
    print("Invalid cabin class")