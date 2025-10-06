#the string of with 1st index to last index but the end index will not included

str = "Joy Chowdhury"

s = str[1:4]
print(s)

#but if we want it at last index we can use two type of things 

s = str[0:len(str)]
print(s)

print(str[0:])


# python also work with negative value
# the count will be -5,-4,-3,-2,-1

st = "apple"
st1 = st[-5:-2] # so the answer will be -5,-4,-3
print(st1)