# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here

# Call the function
calculate_dog_years()

def calculate_dog_years():
    try:
        # Prompt user and convert to integer
        age = int(input("Input a dog's age: "))

        if age < 0:
            print("Age cannot be negative.")
        elif age <= 2:
            # First two years are 10 dog years each
            dog_years = age * 10
        else:
            # First two years (20) + 7 for each year after
            dog_years = 20 + (age - 2) * 7
        
        if age >= 0:
            print(f"The dog's age in dog years is {dog_years}.")
            
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Call the function
calculate_dog_years()
