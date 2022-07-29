# mystery.py
# Name: 
# Collaborators: 

# This is the mystery.py code, and the comments show how to walk through it.

# b(9)
def b(z):
    # z=9 for this
    # prod = a(9,9)
    prod = a(z,z) # prod = 90
    print(z, prod) # prints 9 90
    return prod # returns 90

# a(9,9)
def a(x, y):
    # x,y = 9,9
    x = x+1 #x = 10
    prod = x*y #prod = 90
    return prod # returns prod (90)

# c(1,5,3)
def c(x,y,z):
    sum = x+y+z # adds inputs, sum = 1+5+3 = 9
    # pow = b(9)^2 - what's b(9)? calculate it
    pow = b(sum) ** 2 # pow = 90^2 = 8100
    return pow # returns 8100

x = 1 #x=1
y = x + 1 #y=2
# res = c(1,5,3)
res = c(x, y+3, x+y)
# res = 8100
print(res)
# prints 8100

# what's printed to the console?
# 9 90
# 8100

