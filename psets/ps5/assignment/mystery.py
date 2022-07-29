# mystery.py
# Name:
# Collaborators:


def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod


def a(x, y):
    x = x+1
    prod = x*y
    return prod


def c(x, y, z):
    sum = x+y+z
    pow = b(sum) ** 2
    return pow


x = 1
y = x + 1
res = c(x, y+3, x+y)
print(res)

# what's printed to the console?
