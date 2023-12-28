x = [1,2,3]
y=x
z=x.append(12)
print(z)


print(y)

print(x)

# z == none ....append is predefind  function which has return type void so therefore it show 'NONE' in terminal as its initial return value is always void

print(y) # OUTPUT OF THIS LINE IS [1,2,3,12]

x=x+[9,10]
print(x) #output of this line is [1,2,3,12,9,10]   # THIS IS SUBLIST OF x.This is concatenation only with x .

print(y) # output of this line is [1,2,3,12]


#HERE THE LIST IS WRITTEN IN SQUARE BRACKET "[ ]"