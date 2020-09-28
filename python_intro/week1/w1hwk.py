a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:"))

# This function returns a, b, and c in ascending order
def sortValues(a,b,c):

    sides = [a,b,c]
    sides.sort()
    return sides[0], sides[1], sides[2]

# This function determines if lengths a,b,c form a valid triangle
def triangle_isvalid(a,b,c):

    a, b, c = sortValues(a, b, c)

    # Check if triangle is valid (any two sides > than the remaining side)
    if((a + b > c) and (a + c > b) and (b + c > a)):
        # Determine kind of triangle
        return triangle_determine(a,b,c)
    else:
        return "Triangle not valid" 

# This function determines the kind of triangle, given that it is valid
def triangle_determine(a,b,c):
    sum_sides = a**2 + b**2
    c2 = c**2
    return "right" if (sum_sides == c2) else ("acute" if (sum_sides > c2) else "obtuse")

print(triangle_isvalid(a,b,c))