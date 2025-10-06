# its override the data of characters and also we can read the data
f = open("demo.txt", "r+")#non truncate

f.write("abc")
print(f.read())
f.close()