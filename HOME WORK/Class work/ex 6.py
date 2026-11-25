employees = [
(101, "Alice", 50000),
(102, "Bob", 65000),
(103, "Charlie", 45000)
]

search_id= int(input("Enter Employee ID: "))

found = False
for emp in employees:
    employee_id = emp[0]
    if employee_id == search_id:
            print("Employee found!")
            print("Employee ID:", emp[0])
            print("Employee Name:", emp[1])
            print("Salary:", emp[2])
            found = True
            break

if found == False:
    print("Employee not found.")