rows = 5

# Outer loop for rows
for i in range(1, rows + 1):
    # Inner loop for spaces before asterisks
    for j in range(rows - i):
        print(" ", end=" ")
    
    # Inner loop for printing asterisks
    for j in range(2 * i - 1):
        print("*", end=" ")
    
    # Move to the next line after printing the row
    print()
