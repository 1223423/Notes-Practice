# What in is a integral multiple? Integer multiple?

x = int(input("x: "))
y = int(input("y: "))

def integer_multiple(x, y):
        return isinstance(abs(y) / abs(x), int)


print(integer_multiple(x, y))