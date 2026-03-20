# Loop numbers from 0 to 100
for i in range(0, 101):

    # Check if number does not end in 0 or 5
    if i % 10 != 0 and i % 10 != 5:
        print(i)