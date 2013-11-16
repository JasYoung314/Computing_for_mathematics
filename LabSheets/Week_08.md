# Week 8 - Linear Algebra

A YouTube playlist with all the videos for this lab sheet can be found [here](http://www.youtube.com/playlist?list=PLnC5h3PY-znzwLePTdmDWDCKJse3omJe5).

1. Use Sage to solve the following system of equations:

    $$\begin{cases}
    10x+2y=0\\
    2x-y=154
    \end{cases}$$

2. **TICKABLE** Note that the above system of equations is equivalent to the following systems of equations:

    $$\begin{cases}
    10a+2b=0\\
    2a-b=154
    \end{cases}$$

    $$\begin{cases}
    10m+2n=0\\
    2m-n=154
    \end{cases}$$

    In essense the only thing that defines the system of equations is the cofficients:

    $$\begin{pmatrix}
    10,2,0\\
    2,-1,154
    \end{pmatrix}$$

    We can of course seperate the right hand side of our equation and perhaps include those elements in a vector. Our system can now be represented as:

    $$\begin{pmatrix}10,2\\2,-1\end{pmatrix}\begin{pmatrix}0\\154\end{pmatrix}$$

    Let us attempt to represent the above system in Sage.

    The following defines `b` as a vector:

    ~~~{.python}
    b = vector(0,154)
    ~~~

    The representation of coefficients is a well defined mathematical object called a `matrix`. The following code defines `A` as a matrix:

    ~~~{.python}
    A = matrix([[10, 2], [2, -1]])
    ~~~

    If we define a vector `X` as a vector of the symbolic variables:

    ~~~{.python}
    X = vector([x, y])
    ~~~

    We can **multiply** `A` by `X`:

    ~~~{.python}
    A * X
    ~~~

    Verify that $X = (x_0, y_0)$ where $(x_0, y_0)$ is the solution to our system of equations (obtained in (1)).

    [Video hint](http://youtu.be/zuxPlbRK79w)

3. **TICKABLE** In linear algebra (you will study this next semester) a matrix equation is an equation of the form:

    $$AX=b$$

    or

    $$XA=b$$

    If we define `A` and `b` as in question 2 we can solve this equation quite simply using the `solve_right` or `solve_left` methods. The following obtains a solution to the equation $AX=b$:

    ~~~{.python}
    A.solve_right(b)
    ~~~

    Note that `A\b` is shorthand for `A.solve_right`

    Use the above to solve the following system of equations using matrix notation:

    $$\begin{cases}
    4x - 2y + 3z = 10\\
    -x - 5y - 8z = 9\\
    x + y + z = 1
    \end{cases}$$

    [Video hint](http://youtu.be/-Qxv5XMer60)

4. For reasons that will become clear, the following definition of matrix multiplication is required:

    $$(AB)_{ij}=\sum_{j'}\sum_{i'}A_{ij'}B_{i'j}$$

    For $2\times 2$ matrices this is equivalent to:

    $$AB=\begin{pmatrix}a_{11}& a_{12}\\a_{21}& a_{22}\end{pmatrix}\begin{pmatrix}b_{11}& b_{12}\\b_{21}& b_{22}\end{pmatrix}=\begin{pmatrix}a_{11}b_{11}+a_{12}b_{21}&a_{11}b_{12}+a_{12}b_{22}\\a_{21}b_{11}+a_{22}b_{21}&a_{21}b_{12}+a_{22}b_{22}\end{pmatrix}$$

    As an example create the following two matrices in Sage:

    ~~~{.python}
    A = matrix([[1,2],[3,4]])
    B = matrix([[7,8],[9,10]])
    ~~~

    Attempt to multiply these matrices by hand and carry out their multiplication in Sage:

    ~~~{.python}
    A * B
    ~~~

    Repeat the exercise by multiplying the following pairs of matrices:

    1. $A=\begin{pmatrix}-1&1\\-1&-1\end{pmatrix}$, $B=\begin{pmatrix}-1&4\\1&1\end{pmatrix}$
    2. $A=\begin{pmatrix}0&144\\-2&1\end{pmatrix}$, $B=\begin{pmatrix}1&0\\0&1\end{pmatrix}$
    3. $A=\begin{pmatrix}1&0\\0&1\end{pmatrix}$, $B=\begin{pmatrix}-2&0\\-1&-17\end{pmatrix}$
    4. $A=\begin{pmatrix}0&-1\\3&1\end{pmatrix}$, $B=\begin{pmatrix}1/3&1/3\\-1&0\end{pmatrix}$

    [Video hint](http://youtu.be/NOpEMl_yzMM)

5. **TICKABLE** The previous exercise shows that when considering matrix multiplication there exists a matrix which does not have a multiplicative affect: "the identity matrix".

    The identity matrix of size $n\times n$ is denoted by $\mathbb{I}_n$. The following Sage code gives $\mathbb{I}_n$:

    ~~~{.python}
    identity_matrix(4)
    ~~~

    Note also, that the previous exercise showed that we can sometimes find a matrix $B$ such that $AB=\mathbb{I}_n$. Finding such a matrix is refered to as 'invering' $A$ and if certain properties hold (you will see this in further details next semester) this matrix is denoted $A^{-1}$.

    If we recall the matrix equation $AX=b$ and if we assume that $A^{-1}$exists then multiplying both sides by $A^{-1}$ gives:

    $$A^{-1}AX=A^{-1}b\Rightarrow \mathbb{I}_nX=A^{-1}b\Rightarrow X=A^{-1}b$$

    In Sage we can obtain $A^{-1}$ (if it exists) with the following code:

    ~~~{.python}
    A.inverse()
    ~~~

    Thus another approach to solving $AX=b$ is:

    ~~~{.python}
    A.inverse() * b
    ~~~

    Use this approach to solve the systems of equations we have considered so far.

    [Video hint](http://youtu.be/NOpEMl_yzMM)

6. **TICKABLE** Recalling your basic python knowledge. Lists can be used to hold any sort of object. Obtain a list of the inverses of the following matrices (when the inverse exists, you might need to look up information on `try` and `except`):

    $$\left(\begin{array}{rrrrr}
    \frac{1}{2} & 0 & 0 & -1 & 1 \\
    -1 & -1 & 1 & -\frac{1}{2} & 2 \\
    0 & -1 & 0 & -2 & 0 \\
    0 & 0 & \frac{1}{2} & -1 & 0 \\
    -1 & 0 & -2 & 2 & 0
    \end{array}\right)
    $$
    $$\left(\begin{array}{rrrrr}
    -1 & -1 & 0 & 0 & -1 \\
    2 & 1 & 0 & 1 & 1 \\
    -2 & 0 & 1 & 2 & 2 \\
    -\frac{1}{2} & 0 & -\frac{1}{2} & 0 & \frac{1}{2} \\
    0 & 0 & 0 & \frac{1}{2} & -1
    \end{array}\right)
    $$
    $$\left(\begin{array}{rr}
    -\frac{1}{2} & -\frac{1}{2} \\
    -2 & -1
    \end{array}\right)
    $$
    $$\left(\begin{array}{rrr}
    2 & -2 & 1 \\
    6 & -1 & 1 \\
    12 & -2 & 2
    \end{array}\right)
    $$
    $$\left(\begin{array}{rr}
    1 & 2 \\
    2 & 0
    \end{array}\right)$$

    For every matrix in this list and the original list obtain the result of the `det` method. This gives the **determinant** of the matrices. It is a very important quantity that will be explained next semester.

    [Video hint](http://youtu.be/rUvbWGg0QO0)

7. **TICKABLE** The `random_matrix` command can be used to obtain a random matrix:

    ~~~{.python}
    random_matrix(ZZ, 5) # Gives a random square matrix of size 5 in Z
    random_matrix(QQ, 5) # Gives a random square matrix of size 5 in Q
    ~~~

    Using this attempt to conjecture a connection between the determinant of a matrix and it's inverse (and the determinant of it's inverse).

    [Video hint](http://youtu.be/3qdlespAi9o)

8. **TICKABLE** The file [W08_D01.csv](./Data/W08_D01.csv) contains 4 columns of data:

        a, b, c, d, f, g

    For each row of data, obtain the solution to the system of equations:

    $$\begin{cases}
    ax+by=c\\
    dx+fy=g
    \end{cases}$$

    Write to file a new data set containing the following columns:

        A, B, C, D

    Where $A$ is the number of the original data set, $B$ and $C$ are the solutions to the system of equation in question: $B=x, C=y$. $D$ is the 'norm of the solution vector': $D=\sqrt{C^2+B^2}$.

    If there is no solution to the system of equations set `B=C=D=False`. The data set is a randomly sampled set of problems, how often does a solution exist?

8. The file [W08_D02.csv](./Data/W08_D02.csv) contains a large number of columns and rows. Investigate the `dimensions` and `plot` methods on this matrix.
