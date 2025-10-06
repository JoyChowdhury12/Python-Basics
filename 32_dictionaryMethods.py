student = {
    "name" : "Joy Chowdhury" , 
    "subjects" : {
        "phy" : 65,
        "che" : 55,
        "math" : 88,
    
    }
}


print(student.keys())
print(student.values())


# also we can typecase dict to list

print(list(student.keys()))
print(list(student.values()))


# returns all key_values in the form of tuples

print(student.items())


# we can see our values via keys but if it is not exist 

# print(student["name2"]) # not exist and throws an error

print(student.get("name2")) # not exist but not throwing any error


student.update({"City" : "Chandpur"})
print(student)