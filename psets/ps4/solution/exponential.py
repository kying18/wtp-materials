# Get user input for base and exponent
base = input("What is the base?")
exponent = input("What is the exponent?")
# Make sure to cast to int so we can do operations!
base = int(base)
exponent = int(exponent)
# An exponent is the amount of times you multiply a base times itself
# ex: base = 2, exp= 4 is equal to 2*2*2*2
# As a result, we want to set up a loop that multiplies the base by
# itself for a given amount!
number = base
for i in range(0, exponent-1):
    number = base*number

print(number)
