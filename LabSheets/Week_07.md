# Week 7 - Symbolic Calculus

Using Sage we can carry out various operations from Calculus. This week we will investigate how to:

- Carry out limits in Sage;
- Carry out differentiation in Sage;
- Carry out integration in Sage.

A YouTube playlist with all the videos for this lab sheet can be found [here](http://www.youtube.com/playlist?list=PLnC5h3PY-znz1cih4_2b7QvVZaqPnE7m4).

1. Last week we saw how to define a function in Sage:

    ~~~{.python}
    f(x) = x ^ 3 + 3 * x + sin(x)
    ~~~

    To obtain the variables of a function we can use the `variables` method:

    ~~~{.python}
    print f.variables()
    ~~~

    Try this with a function of more than one variable:

    ~~~{.python}
    f(x, y) = x * y + x ^ 2 + y ^ 2
    ~~~

2. In calculus the following definition of a limit is well know:

    >  $\lim_{x\to a}f(x)=L$ iff $\forall\; \epsilon>0$ $\exists$ $\delta$ such that $\forall\; x$: $|x-a|<\delta$ $\Rightarrow$ $|f(x)-L|\leq \epsilon$.

    Let us calculate the limit of $f(x) = \frac{3x^2}{x^3+x-1}$ as $x\to 1$.

    First of all let us plot $f(x)$:

    ~~~{.python}
    plot(f(x), x, 1, 10)
    ~~~

    The following code obtains $\lim_{x\to 1}f$:

    ~~~{.python}
    limit(f,x=1)
    ~~~

    The following code obtains $\lim_{x\to \infty}f$:

    ~~~{.python}
    limit(f,x=oo)
    ~~~

    We can also obtain the same result using the `limit` method:

    ~~~{.python}
    f.limit(x=1)
    f.limit(x=oo)
    ~~~

    Note that $f(1)=\lim_{x\to 1}f(x)$:

    ~~~{.python}
    f(1)
    ~~~

    This implies that $f$ is continuous at 1.

    [Video hint](http://youtu.be/-br9qoY9QbM)

3. **TICKABLE** Plot $f(x)=\frac{3x^2}{x^3+x-1}$ using the default options:

    ~~~{.python}
    plot(f)
    ~~~

    We see that Sage is plotting extremely high values at the discontinuity due to a root of the denominator which seems to be around $x=.7$. We can plot our function either side of that point and combine them. We do this by creating plot objects:

    ~~~{.python}
    p = plot(f, x, 0.8, 10)
    type(p)
    p += plot(f, x, -10, .6)
    type(p)
    p.show()
    ~~~

    Identify (use the `solve` function or the `roots` method, and maybe the `denominator` method on $f$) $\alpha$: the root of the denominator of $f$. Obtain $\lim_{x\to\alpha +}f(x)$ and $\lim_{x\to\alpha -}f(x)$. Directions of limits can be obtained using the following code:

    ~~~{.python}
    limit(f, x=??, dir="plus")
    limit(f, x=??, dir="minus")
    ~~~

    Note that in this case a non directional limit returns `infinity` this implies that a single limit does not exist.

4. There are various algebraic relationships on limits:

    1. $\lim_{x\to a}[f(x)+g(x)]=\lim_{x\to a}f(x) + \lim_{x\to a}g(x)$
    2. $\lim_{x\to a}[f(x)\times g(x)]=\lim_{x\to a}f(x) \times \lim_{x\to a}g(x)$
    3. $\lim_{x\to a}[f(x)/g(x)]=\lim_{x\to a}f(x) / \lim_{x\to a}g(x)$ (if $\lim_{x\to a}g(a)\ne 0$)


    We can verify the first identity with the following Sage code for a particular example:

    ~~~{.python}
    f(x) = exp(x)
    g(x) = sin(x)
    var('a')
    L1 = limit(f(x) + g(x), x = a)
    L2 = limit(f(x), x = a) + limit(g(x), x = a)
    bool(L1 == L2)
    ~~~

    Note that we use the `bool` class to convert the symbolic equation `L1==L2` to a boolean variable. Verify with some example functions the other two relationships above.

5. **TICKABLE** The point of this question is to investigate $\lim_{x\to 0}\frac{\sin(x)}{x}$. Using Sage:

    1. Obtain the values of $|\sin(x)-x|$ for 1000 values of $x<.05$ (you might find the sage `srange` function helpful).
    2. Plot the above points, what does this indicate as to the value of the limit (investigate the `list_plot` sage function)?
    3. Compute the limit in question using Sage.

6. The point of this question is to investigate $\lim_{x\to 0}(1+x)^{1/x}$. Using Sage:

    1. Compute the numerical value of $e$.
    2. Obtain the values of $(1+x)^{1/x}$ for 1000 values of $x<.05$.
    3. Plot the above points, what does this indicate as to the value of the limit?
    4. Compute the limit in question using Sage.

7. Sage can be used to carry out symbolic differentiation. Experiment with the syntax below for other functions:

    ~~~{.python}
    n = var('n')
    f(x) = x ^ n
    diff(f,x)
    ~~~

    Note that here everything is a symbolic variable!

    [Video hint](http://youtu.be/FbxioEG9kzM)

8. The point of this question is to investigate the definition of a derivative:

    $$\frac{df}{dx}=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$$

    1. Consider $f(x) = x^3 + 3x - 20$;
    2. Compute $\frac{f(x+h)-f(x)}{h}$;
    3. Compute the above limit as $h\to 0$ and verify that this is the derivative of $f$.

9. **TICKABLE** By definition, the derivative $f'(a)$ gives the rate of change of the tangent line at the point $(a,f(a))$. Write a function that takes as arguments a function and a coordinate $x=a$ and returns the plot of the function as well as the tangent line at $x=a$. The plot \text{in Figure \ref{W07-img01}} shows a plot of $f(x)=\sin(x)+3x+1/x$ as well as the tangent line at $x=2$.

    ![\text{Tangent at $x=2$.}\label{W07-img01}](./Images/W07-img01.png)

10. There are various rules for the calculation of limits:

    1. $\frac{d}{dx}(u+v)=\frac{du}{dx}+\frac{dv}{dx}$
    2. $\frac{d}{dx}uv=v\frac{du}{dx}+u\frac{dv}{dx}$
    3. $\frac{d}{dx}\frac{u}{v}=\frac{v\frac{du}{dx}-u\frac{dv}{dx}}{v^2}$


    We can verify the first identity with the following Sage code for a particular example:

    ~~~{.python}
    f(x) = exp(x)
    g(x) = sin(x)
    D1 = diff(f(x) + g(x), x)
    D2 = diff(f(x), x) + diff(g(x), x)
    bool(D1 == D2)
    ~~~

    Note that we use the `bool` class to convert the symbolic equation `L1==L2` to a boolean variable. Verify with some example functions the other two relationships above.

11. Sage can be used to carry out integration. Indefinite integrals can be computed as follows:

    ~~~{.python}
    f(x) = x ^ 4
    integrate(f, x)
    ~~~

    the `integrate` method can also be used:

    ~~~{.python}
    f.integrate(x)
    ~~~

    To compute the definite integral, we simply include the start and end points as arguments:

    ~~~{.python}
    integrate(f, x, 5, 12)
    ~~~

    [Video hint](http://youtu.be/wQEk0h5kg50)

12. **TICKABLE** As before we can integrate fully symbolic expressions:

    ~~~{.python}
    a = var('a')
    f(x) = sin(a * x)
    f.integrate(x)
    ~~~

    Note that in some cases we might need to include certain assumptions. Try the following code and understand why things have not worked:

    ~~~{.python}
    n = var('n')
    f(x) = x ^ n
    f.integrate(x)
    ~~~

   Investigate the `assume()` command as well as the `forget()` command and work out the previous integral.

13. A graphical interpretation of integration is that $\int_a^bf(x)dx$ gives the area under the curve of $f(c)$. Using a technique called Riemmann integration we can approximate this area by taking a certain number of rectangles of given width and height given by $f(x)$. Do some work on Riemmann integration and use sage to see how the approximation converges to the actual value of the integral as the number of rectangles taken increases.

15. **TICKABLE** The data file [W07_D01.txt](./Data/W07_D01.txt) contains 5 columns of data:

    $$a,b,c,A,B$$

    For every row of data compute $\int_{A}^{B}ax^2+bx+c$ and obtain:

    1. The mean value of the integral
    2. The mean value of all integrals that are positive
    3. The mean value of all integrals that are negative

    To carry this out you will need to load a data file as before (see Python lab sheets) but to do so in the notebook you need to 'attach' a data file.

    [Video hint](http://www.youtube.com/watch?v=lhmXmIBBQOI) (Only the first part of this video is relevant to this question)
