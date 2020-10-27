spending = {
    "j" : int(input("John: ")),
    "p" : int(input("Peter: ")),
    "w" : int(input("William: "))
}

debt = {
    "j" : 0,
    "p" : 0,
    "w" : 0
}
def splitcosts(spend, debt):
    for spender in spending:
        for debtor in debt:

            split = spending[spender]/len(debt)

            if(spender == debtor):
                debt[spender]-= split
            else:
                debt[debtor]+= split
    print(debt)

splitcosts(spending, debt)
