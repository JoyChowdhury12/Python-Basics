# it will refresh the data and we can add new data

f= open("demo.txt", "w+")#truncate 
print(f.read())
f.write("abc")
f.close()