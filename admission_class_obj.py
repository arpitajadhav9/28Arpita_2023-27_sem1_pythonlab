print("""------STUDENT ADMIT------""")

class Student:
    
    def __init__(self): #This is used 
        self.name = input("enter the name: ")
        self.age = int(input("enter the age: "))
        Student.count=+1
    
    def display(self):
        print("name : ",self.name,"Age :",self.age)
        print(Student.count)

obj1 = Student()
obj1.display()

Student.count