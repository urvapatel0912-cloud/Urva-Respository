user_bio = input("Please enter your gender: ")
user_hem = float(input("Please enter your hemoglobin level: "))

if user_bio == "Male":
    if user_hem < 117:
        print("Your hemoglobin level is low")
    elif user_hem <= 155:
        print("Your hemoglobin level is normal")
    else:
        print("Your hemoglobin level is high")

elif user_bio == "Female":
    if user_hem < 134:
        print("Your hemoglobin level is low")
    elif user_hem <= 167:
        print("Your hemoglobin level is normal")
    else:
        print("Your hemoglobin level is high")

else:
    print("Invalid Input")