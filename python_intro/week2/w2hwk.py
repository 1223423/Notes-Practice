# Version 2: Dramatically improved time complexity by prevening unnecessary loops & calculation

price_orange = int(input("Orange cost: "))
price_grapefruit = int(input("Grapefruit cost: "))
price_melon = int(input("Melon cost: "))
budget = 10000
basket = 100

# Instead of looping through n of fruits we loop through through the budget and interate by costs
# This way we're checking far less combinations
for o in range(0, budget, price_orange):
    # Notice how we can use the previous orange costs to narrow this loop's range further
    for g in range(0,budget-o, price_grapefruit):
        # Check if remainder budget is divisible by melon price
        # If it is that means this is a potential correct solution where o g m are all integers
        m = budget - o - g
        if m%price_melon == 0:
            # Does this potential solution equal our budget?
            sum = o + g + m
            if sum == budget:
                # If it does, derive the number of fruits
                melons = m / price_melon
                oranges = o / price_orange
                grapefruits = g / price_grapefruit

                # Finally, do the n of fruits add up to the amount we want?
                if(oranges + melons + grapefruits == basket):
                    print('{} oranges {} grapefruits {} melons = {} fruits for a total of {} '.format(int(oranges), int(grapefruits), int(melons), sum, budget))
            # If sum already exceeds our budget, break out of the inner loop
            elif sum > budget:
                break