# Computing for mathematics handout 2 - Conditional Statements, flow control and functions

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

- Variables, variables types etc...
- What we can do to numeric variables;
- What we can do to strings;
- If statements;
- Loops (`for` and `while`);
- Functions;
- Comments.

## Saving files

When you save a python script make sure to include the `.py` extension. This ensures that IDLE will be able to open it.

## Indentation

Indentation is important in Python.

~~~{.python}
if BOOLEAN:  # Check if BOOLEAN is true or false
    then do everything in this indented block
    ...
    ...
    ...
    up until the last indent!
else:  # If BOOLEAN is false
    then do everything in THIS indented block
    ...
    ...
    ...
~~~

## Assignment

In question 21 you used a very clever aspect of Python called 'simultaneous assignment'. This ensured that `a` and `b` changed value at the same time.

To do this without simultaneous assignment we would need a `temporary variable`:

    temp = a
    a = b
    b = temp + b

## Documentation

**Commenting is extremely important**. You need to stick to the conventions described in questions 22, 23 and 24 of the first lab sheet.

Remember to describe functions like this:

~~~{.python}
def somefunction():
    """
    Describe in a sentence or two what your function does

    Arguments: Describe what variables must be passed to the function

    Outputs: Describe what outputs will be returned by the function
    """
    Then start the code... # Include in line comments along the way.
~~~

## What you should do next:

- **Get started on the second sheet!**
- To make the best use of the lab sessions turn up having finished your sheets;
- If anything is still unclear please come and see me during office hours.
