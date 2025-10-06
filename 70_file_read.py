# python can be used to perform operations on a file (read & write data)
# we have to open a file before reading or writing


f = open ("demo.txt", "r")

# data = f.read()

# print(data)
line1 = f.readline()
line2 = f.readline()

print(line1)
print(line2)
f.close()