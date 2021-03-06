# Simple power function 

b = int(input("Base: "))
e = int(input("Exponent: "))

# Turbo brainpower solution
print(b**e)

# Recursive solution
def power(b,e):
    if(e == 0):
        return 1
    else:
        return b * power(b,e - 1)

# Alternatively iterative solution
def power_i(b,e):
    r = 1
    while(e):
        r *= b
        e=e-1
    return r

print("Recursive: " + str(power(b,e)))
print("Iterative: " + str(power_i(b,e)))
