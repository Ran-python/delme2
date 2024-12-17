# app.py

# Entry Point: Start of the Program
print("Starting the program...")

import helper
import calcs

def main():
    # Greeting the user
    name = input("Enter your name: ")
    print(helper.greet(name))

    # User inputs for calculations
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform calculations using calcs module
    sum_result = calcs.add(num1, num2)
    diff_result = calcs.subtract(num1, num2)
    product_result = calcs.multiply(num1, num2)

    # Handle division separately to catch potential errors
    try:
        div_result = calcs.divide(num1, num2)
    except ValueError as e:
        div_result = str(e)

    # Display results
    print(f"The sum of {num1} and {num2} is {sum_result}")
    print(f"The difference between {num1} and {num2} is {diff_result}")
    print(f"The product of {num1} and {num2} is {product_result}")
    print(f"The division of {num1} by {num2} is {div_result}")

if __name__ == "__main__":
    main()

# Entry Point: End of the Program
print("Program execution completed.")
