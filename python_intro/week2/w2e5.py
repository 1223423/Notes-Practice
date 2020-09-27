# Uses sieve of Eratosthenes algorithm to generate primes and check if n is one of them

n = int(input("n: "))

def sieve(limit):
    nonprime = set()
    primes = [2]

    for i in range(3, limit+1, 2):
        if i in nonprime:
            continue

        for z in range(i*i, limit+1, i):
            nonprime.add(z)

        primes.append(i)

    return primes

print(sieve(n))
print(n in sieve(n))
