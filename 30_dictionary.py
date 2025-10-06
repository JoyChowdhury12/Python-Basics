info = {
    "key" : "value",
    "name" : "Joy Chowdhury",
    "id": 453,
    "subject" : ["Python", "Java", "C",],
    "Topics" : ("dict", "Set"),
    
}
print(info["name"])
print(info["subject"])

# as this is mutable so we can change value 

info["name"] = "Joy"
print(info)


# also we can add more key - values in dict

info["surname"] = "Chouhan" 

print(info)


# also we can create null dict and add key_value later

null_dict = {}

null_dict["name"] = "Chowdhury"

print(null_dict)