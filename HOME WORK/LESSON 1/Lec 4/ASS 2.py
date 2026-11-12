number = []

while True:
    user = input("Enter the Number or quit by pressing Enter: ")
    if user == "":
        break
    number.append(float(user))
number.sort(reverse=True)

print("Five greatest numbers:")
for number in number[:5]:
    print(number)

