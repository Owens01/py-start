try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print(f"The result of {a} divided by {b} is: {result}")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Execution completed.")
