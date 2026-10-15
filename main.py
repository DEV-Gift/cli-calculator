def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    return a / b


def show_menu():
    print("\n===== CLI CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")


def main():
    while True:
        show_menu()

        choice = input("Choose an operation: ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")
            continue

        try:
            first = float(input("Enter the first number: "))
            second = float(input("Enter the second number: "))

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if choice == "1":
            result = add_numbers(first, second)

        elif choice == "2":
            result = subtract_numbers(first, second)

        elif choice == "3":
            result = multiply_numbers(first, second)

        elif choice == "4":
            if second == 0:
                print("Error: Cannot divide by zero.")
                continue

            result = divide_numbers(first, second)

        print("Result:", result)


main()