class Car :
    @staticmethod
    def start() :
        print("Car Started..")

    @staticmethod
    def stop() :
        print("Car stopped..")


class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type


car1 = Fortuner("Diesel")

car1.start()