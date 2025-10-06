class Student :
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

    def printAverage(self):
        print("Hi!",self.name,"Your average marks is :",sum(self.marks)/3)


s1 = Student("Joy Chowdhury", [99,98,97])

s1.printAverage()