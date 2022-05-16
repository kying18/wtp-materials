# Lecture 3: Compound Objects and Conditionals

# Sources

These notes were adapted or copied verbatim from from [Adam Hartz](https://hz.mit.edu/)'s MIT [6.145 readings](https://hz.mit.edu/catsoop/6.145/), as well as [Think Python 2e](https://greenteapress.com/wp/think-python-2e/) by [Allen Downey](http://www.allendowney.com/wp/).

# Conditional Statements

So far, all of our programs have continued in a relatively straightforward manner: Python executed all of the statements in a program in exactly the order they were specified.

However, when we program more complex functionality, we might need to check a certain condition and change behavior of the program according to the result of that condition. **Conditional statements** give us this ability.

Let's go back to our example of a robot doing our homework. Perhaps we only want the robot to do our math homework if it is due tomorrow. In thise case, we would need to ask our robot to check whether or not the math homework is due tomorrow, and if it is, do the math homework, otherwise, proceed with all the other homework. The flowchart would look something like this:

#### TODO flowchart

## `if` Statements

We can capture the above example using an `if` statement:

```
# check if math homework is due tomorrow
if math_due_tomorrow:
    print("Doing math homework")
print("Doing English homework")
print("Doing history homework")
print("Doing science homework")
print("Doing programming homework")
```

Here's a more functional example using absolute value:

```
# Absolute value
if x < 0:
    x = -x
```

The boolean expression after `if` is called the **condition**. If it is true (i.e., if it evaluates to `True`), the indented statement (the body) runs. If not, nothing happens.

We may have multiple statements in the body of the conditional statement. Any statements that have the indentation at the same level are part of the body, and all of them get executed if the conditional is true.

```
# This example also introduces a new concept: we can display a sequence of
# characters to the screen verbatim by surrounding them in quotes.

print("This will always print")
if x < 0:
    print("x is negative")
    print("so we'll print")
    print("a few extra things")
print("This will always print, too")
print("And so will this!")
```

In this case, if `x` is less than `0`, Python will execute all three indented lines; otherwise, it will skip all of them. Notice that only the execution of the indented lines is affected by the condition; the bottom two lines are not part of the conditional; they are always executed

There is no limit on the number of statements that can appear in the body, but there has to be at least one. Occasionally, it is useful to have a body with no statements (usually as a place keeper for code you haven't written yet). In that case, you can use the `pass` statement, which does nothing.

```
if x < 0:
    pass  # do nothing
```

## `if`-`else` Statements

A second form of the `if` statement makes Python run one of multiple possible alternative pieces of code. In this structure, there are two possibilities and the condition determines which one runs. The syntax looks like this:

```
if x % 2 == 0:
    print("x is even")

else:
    print("x is odd")
```

Basically, if the remainder of `x` divided `2` is `0`, then `x` is even, and we print the statement `"x is even"`. Otherwise, we know that `x` is odd, and we run the block under the `else:` branch, which prints the alternative statement `"x is odd"`.

The alternatives are called **branches**, because they are branches in the flow of execution.

## Chained Conditionals

Sometimes, it's not enough to simply have one statement and an alternative. Sometimes, we want to have multiple branches. Here, we can use a **chained conditional**:

```
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
```

`elif` is an abbreviation of "else if". Again, exactly one branch will run. There is no limit on the number of `elif` statements. If there is an `else` clause, it has to be at the end, but there doesn't have to be one.

Each condition is checked in order. If the first is false, the next is checked, and so on. If one of them is true, the corresponding branch runs and the statement ends. Even if more than one condition is true, only the first true branch runs.

## Nested Conditionals

The branches of a conditional can contain any valid Python code. This means that a conditional could contain another conditional! Previously, when we compared `x` and `y`, we could have written code like this:

```
if x == y:
    print("x and y are equal")
else:
    if x < y:
        print("x is less than y")
    else:
        print("x is greater than y")
```

Here, the outer conditional has two branches. The first branch is a simple statement, but the second branch contains another conditional that has two branches of its own. While it's possible to have nested conditionals, it's a good idea to avoid them when you can, because it's difficult to read sometimes!

Also, note that we can use logical operators that reduce to a boolean. For example:

```
if 0 < x:
    if x < 10:
        print("x is a positive single-digit number.")
```

can be simplified if we replace it with:

```
if 0 < x and x < 10:
    print("x is a positive single-digit number.")
```

## Concept question

1. Can you explain differences between the following examples?

```
if x < 0:
    print("x is negative")
elif x < 100:
    print("x is a small positive number")
elif x < 1000:
    print("x is a not-so-small positive number")
else:
    print("x is a large positive number")
```

```
if x < 0:
    print("x is negative")
if x < 100:
    print("x is a small positive number")
if x < 1000:
    print("x is a not-so-small positive number")
else:
    print("x is a large positive number")
```

```
if x < 0:
    print("x is negative")
else:
    if x < 100:
        print("x is a small positive number")
    else:
        if x < 1000:
            print("x is a not-so-small positive number")
        else:
            print("x is a large positive number")
```

# Sequences

Strings are actually sequences of characters. In Python, some may consider strings a primitive, and some may consider it of **compound** type (since it is comprised of characters). We can do many interesting operations in Python with sequences, but we'll start with strings, and then generalize.

# Sequences

Strings are actually sequences of characters. In Python, some may consider strings a primitive, and some may consider it of **compound** type (since it is comprised of characters). We can do many interesting operations in Python with sequences, but we'll start with strings, and then generalize.

## Indexing

In Python, we can extract a single character from a string (or more generally, a single value from a sequence) using square brackets. For example:

```
sequence = "this string"
character = sequence[1]
print(character)
```

Here, the `[1]` means we are selecting the character at position 1 from `sequence` and assigning it to the variable `character`. The `1` is called an **index**. The index must be an integer and it tells the program which value in the sequence we want.

In Python, we use `0-indexing`, which means that our sequences start at index `0`, rather than `1`. In the example above, we actually print out `h` and not `t`, which is what many people just starting to code might expect!

In our example above, any integer between 0 and 10 is a valid index. Any integer between -1 and -11 is also a valid index. This is how we can index from the end of a sequence! In the example above, `sequence[-1]` would give us `g`, `sequence[-2]` would give us `n`, and so on.

## Iteration

Sequences are also **iterable**, which means that we are allowed to iterate over them! In the context of strings, we would likely start the beginning, select each character turn after turn, do something with it, and then continue until the string ends. This is referred to as **looping**. In Python, we can have a `for` loop that, for example, can print each character in a string:

```
word = "cat"
for letter in word:
    print(letter)
print('done')
```

Basically, for each letter in the word, we print out that letter, and then after we iterate through the entire string, we print `done`.

We will come back to looping later. Let's cover more complex Python data types!

## Tuples

**Tuples** are sequences that can contain arbitrary objects (integers, floats, Booleans, None, or even other tuples!).

Tuples are specified as a comma-separated sequence of arbitrary objects, usually wrapped in parentheses. For example, the following is a tuple containing three different objects: `x = (7, -7.8, "blue")`.

We can perform many of the same operations on tuples that we could on strings. For example:

- we can index into a tuple (`x[1]` gives us `-7.8`)
- we can use + to concatenate two tuples (`x + (1, 2, 3)` gives us `(7, -7.8, "blue", 1, 2, 3)`)
- we can compare two tuples using `==`
- we can loop over the elements in a tuple

## Lists

**Lists** are one of the most useful Python types. It is also a sequence that can contain arbitrary objects (integers, floats, Booleans, None, lists/tuples), just like the tuple, but there is one big difference:

Lists are **mutable**!

This means that they can be changed _after_ they are created! However, strings and tuples cannot be. If we wanted to replace the 3rd item in a string or a tuple, we would need to create another tuple where the 3rd item is different. However, in a list, we can go in and edit the 3rd item without creating another one!

Tuples use round parentheses, while lists use square brackets. Here are some examples of lists:

```
cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [42, 123]
another_list = [7, 12, 10]
empty = []  # we can also make a list that contains no elements!
```
