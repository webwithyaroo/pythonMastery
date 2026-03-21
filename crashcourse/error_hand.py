
    
try:
    # 1. Risky code
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    # 2. Runs if you divide by zero
    print("Error: You cannot divide by zero!")
    
except ValueError:
    # 2. Runs if you enter text instead of a number
    print("Error: Please enter a valid integer.")
else:
    # 3. Runs only if everything went perfectly
    print(f"Success! The result is {result}")
finally:
    # 4. Runs no matter what happens
    print("Cleaning up resources...")
    
    
def set_age(age):
    if age < 0:
        # We manually trigger a ValueError
        raise ValueError(f"Invalid age: {age}. Age cannot be negative!")
    print(f"Age set to {age}")

try:
    set_age(-5)
except ValueError as e:
    print(f"Caught an error: {e}")

