# All classes have a function called __init__(), which is always executed when the object is being initiated
# the self parameter is a reference to the current instance of the class and is used to access variables that belongs to the class... 
class Student:
    versity = "Daffodil International University" # class attributes
    def __init__(self, name, marks):
        self.name = name # object attributes
        self.marks = marks # object attributes
        print("Adding new student in the database...")

s1 = Student("Joy Chowdhury", "55")
print(s1.name,s1.marks)
print(Student.versity)  #class attributes 
print()

s2 = Student("Rohit", "12")
print(s2.name)
print(s2.marks)
print(s2.versity) #instance attributes 

