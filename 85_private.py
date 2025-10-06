#private attributes and methods are meant to be used only within a class and are not accesible from outside the class 
# we simply do this with __


class Account :
    def __init__(self, acc_no , acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def resetPass(self):
        print(self.__acc_pass)

acc1 = Account("02134832", "abcde")

print(acc1.acc_no)
acc1.resetPass()

print(acc1.__acc_pass) # this will throw an error



        