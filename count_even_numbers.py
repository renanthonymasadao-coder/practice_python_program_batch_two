# Set counter for even numbers
count = 0

# Ask the user to input 10 numbers
for i in range(10):
    num = int(input("Enter a number: "))

    # Check if the number is even
    if num % 2 == 0:
        count += 1

# Display total even numbers
print("Total even numbers:", count)