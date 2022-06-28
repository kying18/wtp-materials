# Lecture 3: Expressions and Variables

# Sources

These notes were adapted or copied verbatim from from [Adam Hartz](https://hz.mit.edu/)'s MIT [6.145 readings](https://hz.mit.edu/catsoop/6.145/), as well as [Think Python 2e](https://greenteapress.com/wp/think-python-2e/) by [Allen Downey](http://www.allendowney.com/wp/).

# Algebraic Expressions

We can combine the basic types using **operators**. Previously, we've already seen the `+` operator. Let's explore some other mathematical operators we can use:

- `+` denotes addition
- `-` denotes subtraction
- `*` denotes multiplication
- `/` denotes division
- `i**j` denotes exponentiation

## Order of Operations

If you've learned about order of operations, PEMDAS, it still holds in programming. In case not, we'll briefly cover the ordering here:

- Parentheses have the highest precedence and are evaluated first
- Exponentiation is next
- Multiplication and Division follow exponentiation
- Addition and Subtraction come last

For example, an expression like `5+(2*(4-1)+4**3)` would folloow the following order:

1. We evaluate what is inside the parentheses first: `2*(4-1)+4**3`.
2. We must also apply PEMDAS here as well. Evaluating the parentheses, we get: `2*3+4**3`.
3. Now, evaluating the exponent, we get: `2*3+64`.
4. Evaluating the multiplication, we get: `6+64`.
5. Finally, we perform the addition here, and get `70` for the final value of the parentheses.
6. For the value of the whole expression, we get `5+70`, which gives us then `75`.

## Strings

We cannot perform mathematical operations on strings, even if they look like numbers. For example `"stringa"-"stringb"`, `"100"/"20"` and `"4"*"2"` are not valid expressions. However, there are two exceptions: `+` and `*`.

The `+` operator allows us to join strings together. This is known as **string concatenation**. For example, `"Hello " + "World"` would give us `"Hello World"` (note that there is a space at the end of the first string... if it were just `"Hello"+"World"`, we would get `"HelloWorld"`)

The `*` operator allows us to repeat a string "multiplied" by an integer. For example, `"example"*3` would produce `"exampleexampleexample"`. We can treat `"example"*3` as `"example"+"example"+"example"`, but with less to type out, which will be a recurring theme in computer science. Usually, the less to type, the less code there is to contain a mistake!

## Concept Questions

1. What would `7+8` produce?
2. What about `7.+8`? How is this result different from the one above?
3. What would happen if we tried `7+"8"`?
4. What about `"7"+"8"`?

# Converting Between Types

Just a note, we can convert between types of numbers and strings.

```
int(7.8)  # 7
float(6)  # 6.0
str(6.0)  # "6.0"
int("2")  # 2
float("7.8")  # 7.8
int("tomato")  # error
int("7.8")  # error
float("6")  # 6.0
```

# Boolean Expressions

A Boolean expression resolved to either true or false. In Python, this is an object of type `bool`, and the value is either `True` or `False`. For example. `5 == 5` returns `True`, but `5 == 6` returns `False`.

As we might guess, the `==` is an operator that determines whether or not two values are equal to one another, and results in a boolean value.

The `==` operator is a relational operator, which operates on arbitrary values and produce bool objects. Other relational operators include:

- `==` ("is equal to") compares two operands and produces `True` if they are equal, and `False` otherwise.
- `!=` ("is not equal to") compares two operands and produces `True` if they are not equal, and `False` otherwise.
- `>` ("is greater than") compares two operands and produces `True` if the first is greater than the second, and `False` otherwise.
- `<` ("is less than") compares two operands and produces `True` if the first is less than the second, and `False` otherwise.
- `>=` ("is greater than or equal to") compares two operands and produces `True` if the first is greater than or equal to the second, and `False` otherwise.
- `<=` ("is less than or equal to") compares two operands and produces `True` if the first is less than or equal to the second, and `False` otherwise.

There are also three operators that only operate on Boolean values:

- `and` produces `True` if both of its operands are `True`, and produces `False` otherwise (for example, `True and True` produces `True`; but `False and True` produces `False`).
- `or` produces `True` if at least one of its operands is `True`, and produces `False` otherwise (for example, `True or True` produces `True`; and `True or False` also produces `True`; but `False or False` produces `False`).
- `not` is a unary operator (it has only one operand) that produces `True` if its operand is `False`, and `False` if its operand is `True` (for example, `not False` produces `True`; and `not True` produces `False`.

Sounds pretty straightforward right? When will we ever need to know if `False or False` is `False`? That doesn't sound like it's very useful... However, in future chapters, we will see that there are more complex expressions that reduce to `True` and `False`, and the computer will rely on those expressions to decide how to proceed!

# Expression Practice

```
5 + 3 - 16      # -8
25 // 4         # 6
8+4*2           # 16
(8+4)*2         # 24
3 ** 5          # 243
3.0 ** 5        # 243.0
3/2             # 1.5
16.3 % 16       # 0.3

True or False       # True
True and False      # False
3 > 4 or 3 == 3     # True
not False           # True
not (4 > 3 and 100 > 6)     # False
4 == 2 + 2          # True
```

# Variables and Assignment

Up to now, we've only really looked at expressions. However, sometimes it's useful to **assign** a name to a value. We do this using **variables**.

Let's use an example:

```
x = 2 + 2
```

Here, we are assigning the result of `2+2` to the value `x`. So, if we ask the console what `x` is, we see that the result is `4`.

Let's try to explain this with some algebra. Ok so if we say `x = 2+2`, then we are basically setting the variable `x` as `4`. Now, if we type in `x+5`, we replace the name with the value, and this is the same as `4+5`, which returns `9`. We can even use another assignment operator with a different variable, `y = x+5`, and now, we have a variable `x` that equals `5` and a variable `y` that equals `9`.

Note, the `=` and `==` might seem similar, but the former is an operator that assigns a value to a variable, and the latter is an operator that checks whether two values are equal.

## Concept questions

1. What if we had set `x = x+5`? Do you think this is allowed? If so, what would `x` be equal to?

# Variable Names

In our example above, we could have replace `x` with some other name, such as `a` or `number` or `elephant`. Usually, we want to choose variable names that are somewhat descriptive, but short enough to type.

For example, can anyone tell me what this code is trying to do:

```
a = 6.28318
b = 2

c = a * b
d = 1 / 2 * a * b ** 2

e = 4 * d
f = 2 / 3 * a * b ** 3
```

In contrast, let's use some more descriptive variable names:

```
tau = 6.28318
radius = 2

circle_circumference = tau * radius
circle_area = 1 / 2 * tau * radius ** 2

sphere_surface_area = 4 * circle_area
sphere_volume = 2 / 3 * tau * radius ** 3
```

That makes the code a lot easier to understand right? It is possible to go a little too far, and then the variables are just annoying to type out:

```
the_ratio_between_the_circumference_and_the_radius_of_a_circle = 6.28318
the_radius_of_the_shapes_for_which_we_want_to_compute_values = 2
```

## Rules for variable names:

- Variable names must begin with an alphabetical character or the underscore character
- Variable names cannot begin with a number
- Variable names must be comprised of alphanumeric characters and underscores (`A-Z`, `a-z`, `0-9`, and `_`). This means no special characters such as `*`, `!`, and so on!
- Variable names are case-sensitive. This means that `wtp`, `WTP`, and `Wtp` are all different variables

## Examples of variable names:

```
# valid variable names
my_wtp_variable = "hello"
mywtpvariable = "hello"
myWtpVariable = "hello"
_my_wtp_variable = "hello"
WTPVAR = "hello"
wtpvar12345 = "hello"

# non-valid variable names
123var = "hello"
wtp-variable = "hello"
my wtp variable = "hello"
```

# Variables Example

```
a = 7
c = 9
a = 4
if a > 6:
    b = 9
else:
    b = 10

if a > 7:
   d = 3
if a > 3:
   d = 2
else:
    d = 1
```

What are the values of `a`, `b`, `c`, and `d`?

Answer:

```
a = 4
b = 10
c = 9
d = 2
```

# Comments

We can add comments to our code to help ourselves/others understand the code better. These do not do anything functional to our code, but they allow us to, well, add comments! In Python, comments are denoted by a `#` symbol. For example, we can write this:

```
x = 2 + 2  # sets x to 4
```

The comment is just for the reader to know that that line is setting `x` to `4`, but the actual function of the code does not change.

# Debugging

We're human. We usually make mistakes. When things don't go the way we want them to, we call these **bugs** in our code. The process of fixing these bugs is known as **debugging**. Sometimes, 10% of your time programming is actually coding and the other 90% is trying to hunt down mysterious bugs. :')

Debugging is usually not an easy task. However, there are a few tools to help you!

First, how do you know there's a bug? Usually, the most common way is that the script throws an error, or you do not get the output that you want! When you get an error, usually that is good, and we can use it to see where we made a mistake.

For example, let's say the fire alarm in your house is going off. This is the equivalent of your code showing an error message. Now, let's say you had a smart-house that told you, "There is smoke coming from the kitchen on the first floor." Naturally, you (or the firemen) would check the kitchen on the first floor, right?

When we have bugs in our code, usually we get an error message that tells us exactly what is going on. That will be the first place to start the debugging hunt.

Now, let's say we don't have any errors but we know our code is failing because we aren't getting the result that we want. Let's say we have a fire alarm going off, but no smart-house, so we aren't sure where it's coming from. We might check all the rooms in the house to see what's going on in there! Similarly, we might want to see if our code at various steps is returning the result that we want it to. We can take a look at what's going on by using a debugger (which is what you probably should officially use)... or... by using a bunch of `print` statements (which is what most Python programmers actually do).

We will grow to love/hate debugging as we start writing code!

There are three kinds of errors that occur in a program:

1. **Syntax error**: “Syntax” refers to the structure of a program and the rules about that structure. For example, parentheses have to come in matching pairs, so `(1 + 2)` is legal, but `8)` is a syntax error. If there is a syntax error anywhere in your program, Python displays an error message and quits, and you will not be able to run the program. During the first few weeks of your programming career, you might spend a lot of time tracking down syntax errors. As you gain experience, you will make fewer errors and find them faster.
2. **Runtime error**: The second type of error is a runtime error, so called because the error does not appear until after the program has started running. These errors are also called exceptions because they usually indicate that something exceptional (and bad) has happened. Runtime errors are rare in the simple programs you will see in the first few chapters, so it might be a while before you encounter one.
3. **Semantic error**: The third type of error is “semantic”, which means related to meaning. If there is a semantic error in your program, it will run without generating error messages, but it will not do the right thing. It will do something else. Specifically, it will do what you told it to do. Identifying semantic errors can be tricky because it requires you to work backward by looking at the output of the program and trying to figure out what it is doing.
