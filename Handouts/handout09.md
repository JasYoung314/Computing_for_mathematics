# Computing for mathematics handout 8 - Extracting solutions from outputs of solvers
Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

Some basic Sage code to solve differential equations:

    - ODEs;
    - Systems of ODEs;
    - Numerical solutions of ODEs (for when they can't be solved exactly).

## Extracting parts of an equation

In [handout 7](http://drvinceknight.github.io/Computing_for_mathematics/Handouts/handout07.html) we saw how to extract solutions to equations from the list output:

    sols = solve(x ^ 2 - x - 1 == 0, x, solution_dict=True)
    [d[x] for d in sols]

Another way to do this is to use `.rhs()`:

    sols = solve(x ^ 2 - x - 1 == 0, x)
    [eq.rhs() for eq in sols]  # We are getting the right hand side of the solutions which are given in the form of equations: `x = ...`.

**This extends to the solutions of differential equations**.

    t = var('t')
    y = function('y', t)
    x = function('x', t)
    sols = desolve_system([diff(x, t) == 1 - y, diff(y, t) == 1 - x], [y,x])

If we take a look at sols, the output of `desolve_system` is a list containing `x(t) = ...`  and `y(t) = ...`.

To extract the solutions we use the `rhs()` method:

    x(t) = sols[0].rhs()
    y(t) = sols[1].rhs()

Now plotting these is straightforward:

    p = plot(x, t, 0, 10, legend_label="$x(t)$")
    p += plot(y, t, 0, 10, color='red', legend_label="$y(t)$")
    p

**NOTE THAT THE ABOVE FAILS TO PLOT!** We need to include initial conditions so that `x(t)` does not contain `x(0)`.

## Numerical analysis

Certain equations and differential equations can't be solved or are very difficult to solve. In this case numerical solutions can still be found. This is what `desolve_rk4` is for.

This is all part of a subject called [Numerical Analysis](http://en.wikipedia.org/wiki/Numerical_analysis).

Some applications of this include the solution of equations that describe how many people would be in a queue throughout a day across different hours of the day.

## LaTeX

LaTeX is a language for typesetting (writing) documents.

- Go through the videos on the corresponding [lab sheet](http://drvinceknight.github.io/Computing_for_mathematics/LabSheets/Week_10.html).
- Take a look at my [coursework template](http://goo.gl/huzjyq).
- There are various other templates available at [https://www.writelatex.com/templates](https://www.writelatex.com/templates).

## What you should do next:

- Work through LaTeX lab sheets.
- **Finish the coursework**
- Contribute to the wiki.
- If anything is still unclear **please** come and see me during office hours.
