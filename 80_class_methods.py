# methods are functions that belong to objects
class Student :
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome (self):
        print("Welcome!", self.name)

    def getMarks(self):
        return self.marks


s1 = Student("Joy Chowdhury",55)
s1.welcome()
print(s1.getMarks())