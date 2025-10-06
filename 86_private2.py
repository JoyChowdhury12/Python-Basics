class Person :
    __name = "anonymous"

    def __hello(self):
        print("Hello person!",self.__name)
    
    def welcome(self) :
        self.__hello()


p1 = Person()
p1.welcome()