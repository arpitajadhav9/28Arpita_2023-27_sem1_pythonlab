def fact(n):
    if n == 0:
        return 1
    else:
        recurse = n*fact(n-1)
        return recurse
    
print(fact(3))