
# Payment history
payments = {
    'John': float(input("John paid: ")),
    'Peter' : float(input("Peter paid: ")),
    'William' : float(input("William paid: "))
}

# Debt accounts
debts = {
    'John' : {'owes': 0, 'isowed' : 0},
    'Peter' : {'owes': 0, 'isowed': 0},
    'William' : {'owes': 0, 'isowed': 0}
}

# Settles debts with equal split for all payments
def settle(payments, debts):
    for person in payments:
        for account in debts:
            transaction = round(payments[person]/len(debts),2)
            if person != account:
                debts[account]['owes'] += transaction
            else:
                debts[account]['isowed'] += transaction

# Prints a summary of current debts
def summarise(debts):
    for account in sorted(debts, reverse = True, key = lambda x: (debts[x]['owes'])):
        print(account, "Owes: ", debts[account]['owes'], "Receives: ", debts[account]['isowed'])

settle(payments, debts)
summarise(debts)
