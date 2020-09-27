# Uses sieve of Eratosthenes algorithm to generate primes and check if n is one of them

n = int(input("n: "))

# The sieve of Eratosthenes works by 'marking' or 'sieving' all multiples of 2, then 3,
#   then 5 and so on, until we reach the number we want. When we reach this limit
#   all the remaining numbers must be prime. This is how it looks visually:
#   https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif
#   
#   We will use the sieve to generate a list of primes and see if our number is inside that list.

def sieve(limit):
    # I'm using a set here to store non-prime numbers
    #   It's slightly faster than a list
    nonprime = set()

    # Optimization 1: I add 2 to the list of primes before we begin.
    #   All prime numbers above 2 are odd. By doing this
    #   we can start at 3 and iterate by 2 which always lands us on an odd number.
    #   Because of this our loop only needs to check half the numbers it would otherwise
    primes = [2]

    # The first loop is handling which multiples we're currently sieving out
    # We start marking multiples of 3 and iterate up by 2 until we reach limit+1
    for i in range(3, limit+1, 2):
        if i in nonprime:
            # If this number is already labeled as non-prime, stop
            #   the code here and go to the next iteration
            #   This means the code below will not be executed and
            #   we go to straight to checking the next i.
            continue

        # This loop marks all multiples of i as non-prime.
        # Optimization 2: We only need to begin looping from the square
        # of the number we're checking.
        for z in range(i*i, limit+1, i):
            # Mark all multiples of i as non prime
            nonprime.add(z)

        # Every i that we didn't skip with the 'continue' statement above
        # Must be a prime, so let's add it to the list here
        primes.append(i)

    # Now we have a list of primes up to limit+1
    return primes

print(sieve(n))
print(n in sieve(n))
