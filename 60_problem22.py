n = int(input("Enter a number that you want factorial : "))
print("Now we are calculating factorial of :",n,"...")
fact = 1
for i in range(1,n+1):
    fact *= i

print("Total factorial = ",fact)