# # CONSTRUCTOR 

# class Student:
#     def __init__(self,name , age): #(DEFAULT CONSTRUCTOR)
#         self.name=name # INSTANCE VARIABLE
#         self.age=age # INSTANCE VARIABLE
#     def display (self): #(STATEMENT TO CALL THE CONSTRUCTOR)
#         print("name: ",self.name, "Age: ",self.age) 

# obj = Student("ABC" , 18)
# obj.display()
# obj= Student("XYZ",30)
# obj.display()


# HERE WE HAVE ADDED HA COUNT VARIBLE WHICH WILL INCREASE BY A NUMBER WHENEVER A NEW OBJECT IS CREATED .

class Student:
    count = 0 # CLASS VARIABLE
    def __init__(self,name , age): #(DEFAULT CONSTRUCTOR)
        self.name=name # INSTANCE VARIABLE
        self.age=age # INSTANCE VARIABLE

        Student.count += 1
   
    def display (self): #(STATEMENT TO CALL THE CONSTRUCTOR)
        print("name: ",self.name, "Age: ",self.age) 

obj = Student("ABC" , 18)
obj.display()
obj= Student("XYZ",30)
obj.display()

print(Student.count) #OUTPUT = 2 , THIS DISPLAYS THE COUNT OF TOTAL NUMBER OF OBEJCTS CREATED TILL NOW.



# WE CAN ACCESS A CLASS VARIABLE ONLY WHEN WE MENTION CLASS NAME WHILE CALLING THE CLASS VARIABLE.

