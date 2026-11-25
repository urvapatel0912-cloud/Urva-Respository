airports = {}

while True:
    print("1. Enter a new airport")
    print("2. Fetch information of an existing airport")
    print("3. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        icao = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[icao] = name
        print("Airport saved!")

    elif choice == "2":
        icao = input(f"Enter ICAO code: ")
        if icao in airports:
            print(f"AIRPORT: {airports[icao]}")
        else:
            print("Airport not found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2 or 3.")