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

    # If any two sides > than the remaining side
    if((a + b > c) and (a + c > b) and (b + c > a)):
        # Then this is a valid triangle!
        return True
    else:
        return False

# This function determines the kind of triangle, given that it is valid
def triangle_determine(a,b,c):
    sum_sides = a**2 + b**2
    c2 = c**2
    return "right" if (sum_sides == c2) else ("acute" if (sum_sides > c2) else "obtuse")


# Main program logic
if triangle_isvalid(a,b,c):
    print(triangle_determine(a,b,c))
else:
    print("This is not a valid triangle.")