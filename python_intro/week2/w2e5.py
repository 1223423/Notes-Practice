# Uses sieve of Eratosthenes algorithm to generate primes and check if n is one of them

n = int(input("n: "))

def sieve(limit):
    # Start with 2 in the list so we only iterate odd numbers
    nonprime = set()
    primes = [2]

    # Loop through each odd number
    for i in range(3, limit+1, 2):
        # If we already sieved i out, go to next loop iteration
        if i in nonprime:
            continue

        # For each number sieve all multiples of i
        for z in range(i*i, limit+1, i):
            nonprime.add(z)

        primes.append(i)
    return primes

print(sieve(n))
print(n in sieve(n))
