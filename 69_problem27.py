def printList(list, i=0):
    if(i == len(list)):
        return
    print(list[i])
    printList(list, i +1)

fruits = ["Mango", "Banana", "Litchi", "Orange"]


printList(fruits)