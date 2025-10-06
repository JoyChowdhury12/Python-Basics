# when one class (child/derived) derives the properties & methods of another class (parent/class)

class Car :
    @staticmethod
    def start():
        print("Car started..")
    
    @staticmethod
    def stop():
        print("Car stopped!")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
        
car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

car1.start()