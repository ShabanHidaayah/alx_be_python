# Get user input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop for columns
    for col in range(size):
        print("*", end="")
    # Move to next line after each row
    print()
    # Increment row counter
    row += 1