# Finds combination value by brute force
# Note: Extremely inefficient

budget = int(input("Enter budget: "))
c_orange = int(input("Orange cost: "))
c_grapefruit = int(input("Grapefruit cost: "))
c_melon = int(input("Melon cost: "))
fruits_wanted = 100;

# Limits
l_orange = int(budget / c_orange)
l_grapefruit = int(budget / c_grapefruit)
l_melon = int(budget / c_melon)

for o in range(0, l_orange):
    for g in range(0, l_grapefruit):
        for m in range(0, l_melon):
            if(o * c_orange + g * c_grapefruit + m * c_melon == budget and o+g+m == fruits_wanted):
                print(str(o) + " oranges, " + str(g) + " grapefruits, " + str(m) + " melons")