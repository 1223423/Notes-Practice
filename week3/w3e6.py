# Triangle printer go brrr

c = str(input("char: "))
n = int(input("n: "))

# Recursive
def brrr(char, n):
    if n:
        print(char * n)
        brrr(char,n-1)

# Iterative
def brrri(char, n):
    while 0:
        print(char * n)
        n-=1

print(brrr(c,n))
print(brrri(c,n))