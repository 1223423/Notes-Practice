# Tests whether n is a perfect square

n = int(input("n: "))
tolerance = 1/1000000 # Error tolerance of one millionth 

# Solution 1: Calculate inverse square and see if integer conversion of that square is
# within tolerance level of the float
def perfSq(n, tolerance):
    sq = (n ** 0.5)
    return abs(sq - int(sq) < tolerance)

# Solution 2: No python operators. Use Newton's method to approximate square root
# and check if integer of that square is within tolerance level of the float
# Uncomment print below to see how the approximation evolves
def perfSq2(n, tolerance):
    x = n
    c = 0
    while(1):
        root = 0.5 * (x + (n / x))
        c+=1
        #print("Iteration: % 2d Approximation: %5.6f Error: % 5.6f" % (c,root,abs((root-x)-tolerance)))
        if(abs(root - x) < tolerance):
            break
        x = root
    return (root - int(root)) < tolerance


print("Newton ", perfSq(n, 0.0001))
print("Python ", perfSq2(n, 0.0001))