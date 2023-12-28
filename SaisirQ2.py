#SUM OF FIRST 2000 PRIME NUMBER.
n = 2000
sum = 0
for x in range(2, n + 1):
    i = 2
    for i in range(2, x):
        if (int(x % i) == 0):
            i = x
            break;
    if i is not x:
        sum = sum + x
print("\nThe sum of prime numbers from 1 to ", n, " is :", sum)