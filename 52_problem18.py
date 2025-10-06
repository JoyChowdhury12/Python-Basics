# # problem 1

# i =1

# while i <= 100 :
#     print(i)
#     i+=1




## problem 2

# i = 100
# while i>=1:
#     print(i)
#     i-=1


#problem 3
# i=1
# n = int(input("Enter a number : "))
# while i <= 10 :
#     print(n*i)
#     i+=1


#problem 4

# list = [1,4,9,16,25,36,49,64,81,100]
# heroes = ["ironman", "Thor", "Superman", "batman"]
# i = 0
# while i < len(heroes):
#     print(heroes[i])
#     i+=1


# idx = 0
# while idx < len(list):
#     print(list[idx])
#     idx +=1



## problem 5

nums = (1,4,9,16,25,36,49,64,81,100)
i = 0
found = 36
while i<len(nums):
    if(nums[i] == found):
        print("Item found at index", i)
    i +=1