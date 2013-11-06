# Computing for mathematics handout 6 - Sage and the Class test

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

- How to carry out basic algebraic operations in Sage (solve equations, simplify expressions etc...)

## What is Sage?

- Sage is a mathematics package built on Python. This implies that you can use the Python code you learnt in the first weeks of this class in Sage.
- Sage can be used to check formulae. For example: what is the formula for $\sum_{i=a}^bx^{i}$?

    ~~~{.python}
    a = var('a')
    b = var('b')
    i = var('i')
    x = var('x')
    sum(x^i,i,a,b)
    ~~~

- Sage can also be used to plot functions (this could help when attempting to visualise a particular theorem):

    ~~~{.python}
    k = 20
    p = plot(x^0,color=rainbow(20)[0], legend_label="$x^0$")
    for i in range(1,20):
        p += plot(x^i,color=rainbow(20)[i],legend_label="$x^{%s}$" % i)
    p
    ~~~

    Here is something a bit more visually impressive (the code is slightly more compact as it uses some Sage tricks):

    ~~~{.python}
    k = 20
    rb = rainbow(k+1)
    sum(plot(sin(i*x)*i,color=rb[k-i], legend_label=r"${0}\sin({0}x)$".format(i)) for i in [0..k])
    ~~~

- Sage is a tool available to you to help you through your time at Cardiff.
- Sage allows you to share files with particular people (if you know their username) and also allows you to publish it.

## Sometimes our server is buggy

Our server has been a bit buggy for some of you. I apologise and sadly there's not much I can do about it a part from show you how to get around the bugs.

- **DO NOT USE INTERNET EXPLORER** Internet explorer (IE) does weird things sometimes and so if you've written your code in IE and then opened up your file in a modern browser you might **still need to re-write your code** (not copy and paste) to make it work. **Alternative to IE are available on the networked machines**.
- If sometimes your code seems to work but does not evaluate try the following trick:

    ~~~{.python}
    sol = solve(x^2==-1,x)
    ~~~

    Then in another cell simple show `sol`:

    ~~~{.python}
    sol
    ~~~

- If all else fails close down your browser and open it up again. If there are very buggy things happening please let me know.

## Class test

- The class test will be 3 questions with 30 marks for each question and 10 marks for correct conventions, commenting and documentation.
- You will submit your work using a folder on the Shared drive: *you won't have read or write rights to that folder* so you will only be able to submit once!
- The class test is at 1400 for some of you (it will start at 1410) and 1500 for others (it will start at 1510). I have spoken to your Calculus lecturer and told him that some of you might be late. He has been very understanding but has asked you to please not waste any time after the class test.

## What you should do next:

- **Finish revising for the class test**: be sure to be confident with the lab sheets 1 - 5 (Sage is not on the class test).
- **Start the next sheet**: this is a longer one looking at how to differentiate, integrate and plot in Sage.
- Contribute to the wiki.
- To make the best use of the lab sessions turn up having finished your sheets;
- If anything is still unclear **please** come and see me during office hours.
