####################################################################################
# Conditionals
####################################################################################
# if statement

x = -1  # we can change this value of x

# absolute value
if x < 0:
    print("Negating x")
    x = -x
print(f"x is: {x}")

####################################################################################
# if-else statement

x = 5  # we can change this value of x

# checking if x is even/odd
if x % 2 == 0:
    print("x is even!")
else:
    print("x is odd!")

####################################################################################
# if-elif-else statement

x = 1
y = 3

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


####################################################################################
# Sequences
####################################################################################

# indexing/slicing

my_list = [1, 2, 'a', 'zebra', -3.14]
my_string = "hello everyone"

# indexing starts from 0:
my_list[0]  # answer is 1
my_string[0]  # answer is "h"

my_list[1]  # answer is 2
my_string[1]  # answer is "e"

my_list[3]  # answer is zebra
my_string[6]  # answer is "e"

# we can also index reverse using negative values
my_list[-1]  # answer is -3.14
my_string[-1]  # answer is "e"

my_list[-4]  # answer is 2
my_string[-4]  # answer is "y"

# we can use indices to take a slice of a string (or any sequence)
# if we have some sequence and we index it: sequence[a:b]
# this is inclusive on left, exclusive on the right: [a, b)
my_list[1:3]  # [2, 'a']
my_string[5:10]  # ' ever'

# if we want to only slice off the beginning of a sequence,
# we can leave off the second index
my_list[1:]  # [2, 'a', 'zebra', -3.14]
my_string[-8:]  # 'everyone'

# likewise, if we want to only slice off the end of a sequence,
# we can leave off the first index
my_list[:3]  # [1, 2, 'a']
my_string[:5]  # 'hello'

####################################################################################
# more string operations

# splitting a string by whitespace (space(s), tab(s), linebreak(s))
another_string = "i really like pi"
split_string = another_string.split()
print(split_string)  # ["i", "really", "like", "pi"]

# we can stitch these strings back together
frankenstein_string = " ".join(split_string)
print(frankenstein_string)  # "i really like pi"
print("!!!".join(["here", "is", "another", "example"]))  # here!!!is!!!another!!!example

# capitalize/lowercase
'a'.upper()  # 'A'
'abc123'.upper()  # 'ABC123'
'HELLO'.lower()  # 'hello'

####################################################################################
# Compound Types
####################################################################################

# Tuples

# tuples are sequences that can contain arbitrary objects
# (integers, floats, Booleans, None, or even other tuples!)

# tuples use parentheses:
coordinate1 = (10, 5)
coordinate2 = (-3, 3)

card1 = (3, "spades")
card2 = (7, "diamonds")

###################################################################################

# Lists

# lists are similar to tuples, but we can change them directly

# lists use square brackets

cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [42, 123]
another_list = [7, 12, 10]
empty = []  # we can also make a list that contains no elements!

my_list = [1, 2, 3]

# modifying an element
my_list[0] = 5
print(my_list)  # [5, 2, 3]

# appending elements
my_list.append(4)
print(my_list)  # [5, 2, 3, 4]

# we can append other things too
my_list.append("sky")  # [5, 2, 3, 4, "sky"]
my_list.append((1, 2, 3))  # [5, 2, 3, 4, "sky", (1, 2, 3)]

# pop removes, extend adds another list to the end
my_list.pop()  # [5, 2, 3, 4, "sky"]
my_list.extend([1, 2, 3])  # [5, 2, 3, 4, "sky", 1, 2, 3]

###################################################################################

# Dictionaries

# provides mapping between keys and values (key-value pairs)
# curly brackets {} with ':' between keys and values, and ',' to
# separate key-value pairs

eng_to_fr = {}  # this is an empty dictionary
eng_to_fr["hello"] = "bonjour"  # this inserts a new key-value pair into the dictionary
print(eng_to_fr["hello"])  # "bonjour"

# note that we can also create a new dictionary like this:
eng_to_fr = {"hello": "bonjour", "goodbye": "au revoir"}

# note that it only works if we look up the keys
# if we look up the value, we get an error! (unless the value is equal to another key)
print(eng_to_fr["goodbye"])  # "au revoir"
print(eng_to_fr["bonjour"])  # error

# keys can be overridden
print(eng_to_fr)  # {"hello": "bonjour", "goodbye": "au revoir"}
eng_to_fr["hello"] = "salut"
print(eng_to_fr["hello"])  # salut

# dictionaries need to have IMMUTABLE OBJECTS as keys

###################################################################################

# Sets

# sets are like lists, BUT:
# 1) they do not have any ordering
# 2) they do not contain any repeated values

my_set = {1, 2, "a"}
my_set.add(3)
print(my_set)  # {1, 2, "a", 3}

my_set.add(1)
my_set.add(1)
my_set.add(1)
my_set.add(2)
my_set.add(2)
my_set.add(2)
print(my_set)  # {1, 2, "a", 3}
