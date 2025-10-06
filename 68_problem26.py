def calc_sum(n):
    if(n==0):
        return 0 
    return calc_sum(n-1) +n

s= calc_sum(5)
print(s)