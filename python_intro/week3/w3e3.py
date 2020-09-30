# ???
# If I eat myself do I get twice as big or disappear completely?

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

def twoBools(a,b,c):
    return (a and (b or c)) or (b and c)

print(twoBools(a,b,c))