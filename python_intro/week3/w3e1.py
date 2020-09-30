# Returns n factorial

n = int(input("n: "))

# Recursive solution
def nfac_recursive(n):
    if(n == 0):
        return 1
    return n * nfac_recursive(n-1)

# Iterative solution
def nfac_iterative(n):
    result = n
    while(n>1):
        n-=1
        result*=n
    return result

print(nfac_recursive(n))
print(nfac_iterative(n))
