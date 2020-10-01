# Palindromes
n = int(input("palindromic n: "))


# Solution 1: Treat numerically
def isPalindrome_n(n):
    base = 10
    x = n
    p = 0
    while n>0:
        p=p*base + n%base
        n = (n - n%base)/base
    return x == p

# Solution 2: Treat as string
def isPalindrome_str(n):
    s = str(n)
    p = ""
    for a in s:
        p = a + p
    return p == str(n)

print(n,"palindrome?", isPalindrome_n(n))
print(n,"palindrome?", isPalindrome_str(n))
