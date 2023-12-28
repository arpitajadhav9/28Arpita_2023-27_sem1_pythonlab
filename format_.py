class Student:
    
    
    def getdata(self,name,age): # we have to write this the def __ init__ is constructor which we can write to or nott but getdata() is need to written
        self.name = name
        self.age = age

    def display(self):
        print("Name is: ", self.name, "Age is: ", self.age)

    def add(self, x,y):
        self.x = x
        self.y = y
        return self.x + self.y

stud = Student()
stud.getdata("Shikha",18)
stud.display()
print(stud.add(4,7))