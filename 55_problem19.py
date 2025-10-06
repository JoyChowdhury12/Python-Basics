# list = [1,4,9,16,25,36,49,64,81,100]

# for i in list :
#     print(i)


nums = (1,4,9,16,25,36,49,64,81,100,36)
found = 36
idx=0
for i in nums :
    if(i == found):
        print("Target found at index ", idx)
    idx +=1
        
