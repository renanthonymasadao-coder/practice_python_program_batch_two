# Ask the user to input the first number
result = float(input("Enter number: "))

# Ask the user for the remaining 9 numbers
for i in range(9):
    num = float(input("Enter another number: "))

    # Subtract each number from the result
    result -= num

# Display the final result
print("The result is:", result)