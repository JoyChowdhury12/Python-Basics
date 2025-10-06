str = "iam studying python from apna college"

print(str.endswith("ege"))
print(str.startswith("iam"))

print()
# for temporary change the first alphabet into upper case 

print(str.capitalize())

print()
# for permanent change the first alphabet into upper case 

str = str.capitalize()
print(str)


print()
# to replace any word with another alphabet 

print(str.replace("python", "java"))


print()
# for search a word or alphabet for the first time occured in the line
print(str.find("apna"))
print(str.find("o"))


print()
# for counts the occurence of substring in the line

print(str.count("o"))