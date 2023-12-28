# WRITE A PYTHON FUNCTION TO SUM ALL THE NUMBERS IN A LIST.

#function for sum of a list
def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
addition = [1, 2, 3, 4, 5]
result = sum(addition)
print(result)  