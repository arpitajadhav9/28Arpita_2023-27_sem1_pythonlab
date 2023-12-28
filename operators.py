# Arithmetic operators
a = float(10)
b = float(5)

print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)
print("\n")

# Relational operators
x = 7
y = 12

print("Relational Operators:")
print("Equal to:", x == y)
print("Not equal to:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal to:", x >= y)
print("Less than or equal to:", x <= y)
print("\n")

# Assignment operators
z = 20

print("Assignment Operators:")
z += 5
print("+= :", z)

z -= 3
print("-= :", z)
print("\n")

# Logical operators
p = True
q = False

print("Logical Operators:")
print("AND:", p and q)
print("OR:", p or q)
print("NOT:", not p)
print("\n")

# Bitwise operators
m = 0b1010
n = 0b1100

print("Bitwise Operators:")
print("AND:", m & n)
print("OR:", m | n)
print("XOR:", m ^ n)
print("NOT:", ~m)
print("Left Shift:", m << 1)
print("Right Shift:", m >> 1)
print("\n")

# Membership operators
list_example = [1, 2, 3, 4, 5]

print("Membership Operators:")
print("In:", 3 in list_example)
print("Not in:", 6 not in list_example)
print("\n")

# Identity operators
obj1 = "Hello"
obj2 = "World"

print("Identity Operators:")
print("is:", obj1 is obj2)
print("is not:", obj1 is not obj2)
print("\n")

# Ternary operator
condition = True
result = "Yes" if condition else "No"
print("Ternary Operator:", result)
