# recurrence relation 
# n! = (n-1)! * n


def fact(n):
    if(n==1 or n==0):
        return 1
    return (n * fact(n-1))

f= fact(5)
print(f)