class Person :
    name = "Anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()

p1.changeName("Joy Chowdhury")
print(p1.name)

print(Person.name)