months = ("jan", "feb", "mar", "apr", "may", "jun",
          "jul", "aug", "sep", "oct", "nov", "dec")

user = int(input("Enter the month number (1-12): "))

if user < 1 or user > 12:
    print("Invalid month number.")
else:
    month_name = months[user - 1]

    if user in (12, 1, 2):
        season = "winter"
    elif user in (3, 4, 5):
        season = "spring"
    elif user in (6, 7, 8):
        season = "summer"
    else:
        season = "autumn"

    print(f"Month number {user} is {month_name}.")
    print(f"The season is {season}.")