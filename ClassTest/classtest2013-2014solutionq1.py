"""
Solution to question 1 of class test

Marking for this exercise will be strict as the students were told multiple times during lectures that all they would need to do for question 1 of the class test is to copy a file from the solutions.
"""

def fib(n):
    """
    A function to give the nth fibonacci number using recursion

    Arguments: n, an integer

    Outputs: the nth fibonacci number
    """
    if n == 0 or n == 1:  # Check the base case
        return 1
    return fib(n - 1) + fib(n - 2)  # Use recursion and the formula for the fibonacci numbers

### 20 marks available for defining function

print "The first 10 fibonacci numbers:"

for i in range(11):  # Printing the first 10 numbers
    print "f(%s)=%s" % (i, fib(i))

### 10 marks available for correct loop and use of function (if incorrect range is used: lose 2 marks)
