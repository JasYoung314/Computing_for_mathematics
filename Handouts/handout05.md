# Computing for mathematics handout 5 - Object Orientated Programming

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

- How to create a class and an instance of a class;
- How to give a class attributes;
- How to give a class methods;
- How to create new classes from old through inheritance.

## Question 7

Many people found question 7 quite a challenge. Here is a similar question.

> _The list `fields` contains two columns of data: each representing the width and lengths of fields. For a field to be profitable they must have an area of at least 50 square metres, how many fields in our data set are profitable?_

~~~{.python}

fields = [[4,5],
          [6,2],
          [1,7],
          [8,2],
          [4,1],
          [7,2],
          [8,2],
          [9,1],
          [10,56],
          [83,15],
          [4,1],
          [53,2]]

class Field():
    """
    A class for our field
    """
    def __init__(self, x, y):
        self.width = x
        self.height = y
    def profitable(self):
        return self.width * self.height >= 50

fields = [Field(f[0], f[1]) for f in fields]
print len([f for f in fields if f.profitable()])
~~~

## What you should do next:

- **Start the next sheet**: this is a short one and the aim is for you to be familiar with Sage.
- Continue to revise for the class test: work through all your lab sheets. If you can do exercises in the lab sheets (not just 'understand them' but actually 'do them') you will be fine.
- To make the best use of the lab sessions turn up having finished your sheets;
- If anything is still unclear **please** come and see me during office hours.
