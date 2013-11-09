"""
Solution to question 3 of the classtest

Marking for this question will again be lenient with marks given for methodology and 'almost working' answers.
"""

import random

class Point():
    """
    A class for a point falling in a random location on a square

    Attributes:
        x: the x coordinate of the point
        y: the y coordinate of the point
        incircle: a boolean indicating whether or not the point is under the graph
    """
    def __init__(self, r=1):
        self.x = random.random()
        self.y = random.random()
        self.undergraph = 1 - (self.x) ** 2 >= self.y  # This returns the boolean checking whether or not the point is under the graph

### 20 marks for creating class as above. Also, 20 marks if include method for 'undergraph' instead of attribute. If however, undergraph check is not class based: students lose 5 marks.

def approxint(N=1000):
    """
    Function to return an approximation for the integral using montecarlo simulation

    Arguments: N (default=1000) which is the number of points

    Outputs: An approximation of the integral
    """
    numberofpointsundergraph = 0
    for i in range(N):  # A loop to drop sufficient points
        point = Point()  # Generate a new drop
        if point.undergraph:  # Check if drop is in circle
            numberofpointsundergraph += 1
    return numberofpointsundergraph / float(N)


### 10 remaining marks for obtaining 'correct answer' (whether or not a function is used as above or if list comprehensions are used etc...

print "For N=200, integral approximated as %s" % approxint(200)
print "For N=1000, integral approximated as %s" % approxint()
print "For N=10000, integral approximated as %s" % approxint(10000)
print "For N=20000, integral approximated as %s" % approxint(20000)
