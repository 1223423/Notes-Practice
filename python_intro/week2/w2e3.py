# Returns log base b of n

b = int(input("b: "))
n = int(input("n: "))

# Recursive 
def log(b, n):
    if(b > n):
        return 0
    else:
        return 1 + log(b, n/b)

# Iterative
def log_i(b, n):
    r = 1
    while(n/b>=b):
        n/=b
        r+=1
    return r


print(log(b,n))
print(log_i(b,n))