# Given integer returns all positive integer divisors

i = int(input("Integer: "))

if(i%2==0):
    for n in range(2, i+1, 2):
        if(i%n==0):
            print(n)
else:
    for n in range(1,i+1):
        if(i%n==0):
            print(n)