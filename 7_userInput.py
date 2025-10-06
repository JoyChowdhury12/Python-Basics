# By default python take all input in string datatype form..
# so we have to typeCast if we need int,float or boolean value

name = input("Enter your name : ")
print(type(name))
print("Welcome!",name)


age = int(input("Enter your age : "))
print(type(age))
print("Your Age is : ", age)


weight = float(input("Enter your weight: "))
print(type(weight), "Your weight is :",weight,"kg")