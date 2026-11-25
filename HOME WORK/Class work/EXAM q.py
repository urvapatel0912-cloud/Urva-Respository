count = int(input("How many values do you want to store? "))

numbers = []

for i in range(count):
    value = float(input(f"Enter number {i + 1}: "))
    numbers.append(value)

if count > 0:
    total = sum(numbers)
    average = total / count

    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
else:
    print("No numbers were entered.")