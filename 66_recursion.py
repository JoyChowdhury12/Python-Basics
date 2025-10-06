# when a function calls itself repeatedly

# prints n to 1 backwards
# recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)