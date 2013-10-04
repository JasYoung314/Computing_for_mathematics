# Week 9 - Differential Equations

Sage can be used to solve differential equations. Often complex systems can be modelled simply in terms of differential equations however solving these differential equations is not always straightforward (you will be studying differential equations a lot closer in the Spring semester). At the end of this week you will be able to:

- Solve differential equations using Sage;
- Solve differential equations numerically using Sage;
- Plot the results of the above.

A YouTube playlist with all the videos for this lab sheet can be found [here](http://www.youtube.com/playlist?list=PLnC5h3PY-znzOZOAOVo6k_b-zDxjBr-x4).

1. **TICKABLE** The general syntax for solving a differential equation of the form $f(x, y)== g(x, y)$ is shown below:

    ~~~{.python}
    desolve(f(x, y) == g(x, y), y)
    ~~~

    Try out the following code which solves the differential equation: $\frac{dy}{dx}=y$.

    ~~~{.python}
    y = function('y', x)
    desolve(diff(y, x) == y, y)
    ~~~

    Note that that there is no need to specify the independent variable ($x$). The following code solves the general form of the above equation: $\frac{dy}{dx}=ky$ for some $k\in\mathbb{R}$.

    ~~~{.python}
    k = var('k')
    desolve(diff(y, x) == k * y, y, ivar=x)
    ~~~

    [Video hint](http://youtu.be/fpyxAE_-UsI)

2. Once we have the solution to a differential equation it is very straightforward to plot it:

    ~~~{.python}
    y = function('y', x)
    soln(x) = desolve(diff(y, x) == y, y)
    plot(soln(x).subs(c=2), x, -10, 10)
    ~~~

    Note that we are here seeing the `subs` method which allows us to substitue a given value in an expression. It is very easy to get a whole family of plots:

    ~~~{.python}
    p = plot(soln(x).subs(c=0), x, -10, 10, color=rainbow(11)[0], legend_label="c=0")
    for C in range(1, 11):
        p += plot(soln(x).subs(c=C), x, -10, 10, color=rainbow(11)[C], legend_label="c=%s" % C)
    p.show()
    ~~~

    We are here making use of the Sage `rainbow` function which gives a list of colors that can be used in the plot `color` option. We are also making use of the `legend_label` option.

    Obtain a similar plot for the solution to the differential equation: $\frac{dy}{dx} = xy$.

    [Video hint](http://youtu.be/XUcn_zTa2FM)

3. There is nothing restricting us to only solving first order differential equations. The following differential equation can be used to model the position of a mass on a spring:

    $$m\frac{d^2x}{dt^2}+c\frac{dx}{dt}+kx=0$$

    Solve this equation.

    [Video hint](http://youtu.be/DZ5ofuAgDIY)

4. **TICKABLE** Solve the following differential equations and plot their solution (for the given particular value):

    1. $\frac{dy}{dx}+4y=5e^x$, ($y(0)=3$)
    2. $\frac{dy}{dx}+\frac{x(2y-3)}{x^2+1}=\sin(x)$, ($y(0)=4$)
    3. $\frac{d^2y}{dx^2}-y=\sin(5x)$, ($y(3)=1, y'(3)=0$)
    4. $\frac{d^2y}{dx^2}+2\frac{dy}{dx}+2y=\cosh(x)$, ($y(1)=2, y'(1)=72$)

5. Systems of differential equations often arise and can also be solved using Sage. Take a look at the `desolve_system` function and solve the following system of differential equations:

    $$\begin{cases}
    \frac{dx}{dt} = 1 - y\\
    \frac{dy}{dt} = 1 - x
    \end{cases}$$

    [Video hint](http://youtu.be/2Q52rmftdjQ)

6. A battle between two armies can be modelled with the following set of differential equations:

    $$\begin{cases}
    \frac{dx}{dt} = - y\\
    \frac{dy}{dt} = -5x
    \end{cases}$$

    Obtain the solution to this system of equations. Assuming that $x(0)=100$ and that $y(0)=700$ plot the two solutions of the equations, which army wins this battle? When does the battle end?

7. **TICKABLE** The love story between Romero and Juliet can be modelled with the following system of differential equations:

    $$\begin{cases}
    \frac{dx}{dt} = -y\\
    \frac{dy}{dt} = .7x
    \end{cases}$$

    Where $x(t)$ represents the affection of Juliet towards Romeo and $y(t)$ the affection of Romeo towards Juliet (negative affection represents 'hatred').

    Solve this system of equation and assuming that Romeo is initially attracted to Juliet ($x(0)=1$) but that Juliet is initially indifferent to Romeo ($y(0)=0$) at time $t=0$ are indifferent to each other describe the long term relationship between the two characters.

    Describe the behaviour of the system if Romeo and Juliet are initially indifferent to each other.

8. **TICKABLE** Certain differential equations are much harder to solve than others. Attempt to solve the following differential equation using Sage:

    $$\frac{dy}{dx} + y(y-1)==|(x-2)|$$

    In these situations certain numerical algorithms exist that can still describe the evolution of the system. Investigate the `desolve_rk4` function and obtain a solution for the above equation given that $y(0)=1$ for $x<100$. Obtain a plot of the numerical solution

    [Video hint](http://youtu.be/LhIyZ14LKKE)
