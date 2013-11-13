# Computing for mathematics handout 7 - The class test, srange, tangents and more applications of functions or classes to data.

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

- How to plot in Sage (domain of plot and 'addition' of plots);
- How to obtain limits in Sage;
- How to differentiate in Sage;
- How to integrate in Sage;
- How to to upload data to Sage.

## Obtaining the values from a solution of an equation

Let's consider the following equation:

$$x^2-x-1$$

To find the roots of the equation we can simply use the `solve` function:

~~~{.python}
sols = solve(x ^ 2 - x - 1 == 0, x)
~~~

Before viewing the solutions of our equation what type of object is `sols`?

~~~{.python}
type(sols)
~~~

`sols` is a 'generic sequence' (a type of list).

~~~{.python}
sols
~~~

We see that our solutions are given in the form of a list of relationships. The solutions to exercise 3 show a way of extracting the solutions. Here is another:

~~~{.python}
sols = solve(x ^ 2 - x - 1 == 0, x, solution_dict=True)
~~~

Sols is now a list of dictionaries. Let us try and extract the positive solution to our equation:

~~~{.python}
phi = [k[x] for k in sols if k[x] >= 0][0]
~~~

If you're not familiar with what $\phi$ is try the following:

~~~{.python}
for n in range(1):
    print expand((phi ^ n - (1 - phi) ^ n) / sqrt(5))
~~~

## Question 9

Question 9 was a tricky task. The solution gives a function that takes a function and a point and outputs a plot. If the solution is not clear: come and speak to me.

## Importing data

Let's carry out the following exercise:

1. Use Python to obtain a list of the Fibonacci numbers;
2. Write those numbers to file;
3. Import that data file in to Sage;
4. Plot the ratio of the differences between two consecutive Fibonacci numbers.

1. Here't the python script:

~~~{.python}
import csv

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

file = open('fibonaccinumber.csv', 'w')
csvwrtr = csv.writer(file)  # You have seen how to do this before
for n in range(201):
    csvwrtr.writerow([fib(n)])

csvwrtr.close()
~~~

Now let us import that file in to Sage and use the following code to obtain the ratios of two successive numbers:

~~~{.python}
import csv

file = open(DATA + 'fibs', 'r')
csvrdr = csv.reader(file)

data = [int(row[0]) for row in data]

ratios = []
for k in range(len(data) - 1):
    ratios = [[k, data[k + 1] / data[k]]]

list_plot(k)
~~~

**We could do all of the above using Sage but this is just an example of using data written to file.**

## What you should do next:

- **Start the next sheet**: make sure you spend time working on the sheet **BEFORE** the labs.
- Contribute to the wiki.
- To make the best use of the lab sessions turn up having finished your sheets;
- If anything is still unclear **please** come and see me during office hours.
