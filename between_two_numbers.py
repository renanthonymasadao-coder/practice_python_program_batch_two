# Ask the user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Determine the smaller and bigger number
start = min(num1, num2)
end = max(num1, num2)

# Print numbers between them
for i in range(start + 1, end):
    print(i)