collection = set()

collection.add(1)
collection.add(2)
collection.add(2) # set doesn't take duplicate values so this will be ignore
collection.add("Joy")
collection.add((1,2,3))
# collection.add([1,23,3]) # this will throw error bcoz sets are immutable and lists are mutable
print(collection)


collection.remove(2)
print(collection)


# collection.clear()
# print(collection)


# to remove a reandom value we use pop

n = {"Hello", "World", "Bangladesh", "Spain"}
n.pop()
print(n)
