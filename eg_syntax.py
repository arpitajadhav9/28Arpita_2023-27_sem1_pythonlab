class TestClass:
    def __init__(self): # constructor function using self
        self.name = None # Variable using self
        self.name = None # Variable using self 
        self.dept = None


# TestArray = [] #empty array

objs = list()
for i in range(10):
    objs.append(TestClass())

print(objs)


objs[0].name = "ABC"
objs[0].age = 18

# Testobject1 = TestClass() #this is an object
#Testobject2 = TestClas()  # this is another object


#Testobject1.name = "ABC" # asssigning value to object1
#Testobject1.age = 18  # assigning valut to object1