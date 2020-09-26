# The euclidean algorithm for greatest common divisor of a and b

a = int(input("a: "))
b = int(input("b: "))

# Recursive
def gcd(a,b):
    # Handle edge case where a or b = 0
    if(a == 0 or b == 0):
        return b if a == 0 else a

    # Logic
    r = a%b
    if not r:
        return b
    else:
        return gcd(b, r)

# Iterative
def gcd_i(a,b):
    # Handle edge case where a or b = 0
    if(a == 0 or b == 0):
        return b if a == 0 else a

    # Logic
    while 1:
        r = a%b
        if not r:
            break
        a=b
        b=r
    return b


print("gcd: " + str(gcd(a,b)))
print("gcd: " + str(gcd_i(a,b)))
    

