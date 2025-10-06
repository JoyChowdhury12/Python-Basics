with open("demo.txt","r") as f:
    data = f.read()
print(data)

# we dont need to close the file because in "with" its always close the file after execution 