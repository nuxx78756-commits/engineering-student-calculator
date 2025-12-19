def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def watts_to_horsepower(watts):
    return watts / 745.7

def pascal_to_kilopascal(pascals):
    return pascals / 1000

def ohms_law(voltage, resistance):
    return voltage / resistance

def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2


while True:
    print("\nEngineering Student Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Watts to Horsepower")
    print("6. Pascal to Kilopascal")
    print("7. Ohm's Law (Current)")
    print("8. Kinetic Energy")
    print("9. Exit")

    choice = input("Choose an option: ")

    if choice == "9":
        print("Exiting program.")
        break

    try:
        if choice in ["1", "2", "3", "4"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(a, b))
            elif choice == "2":
                print("Result:", subtract(a, b))
            elif choice == "3":
                print("Result:", multiply(a, b))
            elif choice == "4":
                print("Result:", divide(a, b))

        elif choice == "5":
            watts = float(input("Enter power in watts: "))
            print("Horsepower:", watts_to_horsepower(watts))

        elif choice == "6":
            pascals = float(input("Enter pressure in pascals: "))
            print("Kilopascals:", pascal_to_kilopascal(pascals))

        elif choice == "7":
            voltage = float(input("Enter voltage (V): "))
            resistance = float(input("Enter resistance (Ohms): "))
            print("Current (A):", ohms_law(voltage, resistance))

        elif choice == "8":
            mass = float(input("Enter mass (kg): "))
            velocity = float(input("Enter velocity (m/s): "))
            print("Kinetic Energy (J):", kinetic_energy(mass, velocity))

        else:
            print("Invalid option. Try again.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")
