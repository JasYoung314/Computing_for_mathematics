---
layout      : post
categories  : labsheets
title       : Week 2 - Conditional Statements and Flow Control
playlisturl : http://www.youtube.com/playlist?list=PLnC5h3PY-znwZCtyKG1UQASpZ9mRkEIJo
comments    : true
---

This lab sheet will serve as a basic introduction to programming. After this session you will know the basic Python syntax to carry out the following:

+ Set up basic variables;
+ Write if statements (so called: 'Conditional statements');
+ Write while and for loops (so call: 'flow control');
+ Define functions;
+ Write clear and consistent code.

A YouTube playlist with all the videos for this lab sheet can be found [here](http://www.youtube.com/playlist?list=PLnC5h3PY-znwZCtyKG1UQASpZ9mRkEIJo).

**Programming in Python**

---

Python is a programming language. There are various other programming languages:

+ Java
+ C
+ C++
+ Ruby
+ VBA

and many more.

A programming language allows you to write a **program** which is a **sequence of instructions that specifies how to perform a computation**.

When writing a program one makes use of an Integrated Development Environment: **IDE**. There are various (freely available) IDE's:

+ Eclipse
+ IDLE
+ Vim

and many more. We will be using the simplest Python IDE available: IDLE which comes bundled with Python (in your own time be sure to investigate others as it is a question of personal choice).

01. **TICKABLE**: Open up IDLE and in the **interpreter** type the following code and press `ENTER`:

        print "Hello world"

    ![]({{site.baseurl}}/assets/Screenshots/W02-S01.png)

    [Video hint](http://www.youtube.com/watch?v=9FdsVBAUqRs)

02. For short bits of code typing directly in to the interpreter is fine (and in fact sometimes very helpful). However, for longer pieces of code one needs to write a file containing all the commands. Open a script and type the same code as above:

        print "Hello world"

    ![]({{site.baseurl}}/assets/Screenshots/W02-S02.png)

    Send this code to the interpreter (you will be asked to save the file: choose a name and system that will be helpful to you and that you stick with for the rest of the course: `W02.py`).

    **Basic variables**

    ---

    A variable is one of the basic building blocks used by a program. Variables may be of various types.

03. **TICKABLE**: Experiment with the following code which creates variables (by assigning them a value) and checks what type they are using the `type` function.

        num1 = 23
        print type(num1)

        num2 = 23.5
        print type(num2)

        str1 = "Hello world!"
        print type(str1)

    [Video hint](http://www.youtube.com/watch?v=UFGJEG34qMk)

04. We can carry out basic arithmetic operations using Python. Take a look at the following:

        num = 2
        num = num +3
        print num

    this can however also be written:

        num = 2
        num += 3
        print num

    Simlarly, `-`, `*`, `/` and `**` can be used for:

    + subtraction;
    +  multiplication;
    +  division;
    +  exponentiation.

    [Video hint](http://www.youtube.com/watch?v=A_Pa6Ov60T8)

05. **TICKABLE**: Assign the variable `num` to a value of 5.2, what is the result of adding 7 to `num` then muliplying `num` by 300 then dividing `num` by 4 and finally raising `num` to the power of 3?

    [Video hint](http://www.youtube.com/watch?v=ihBpyMpDy-M)

06. **TICKABLE**: We can carry also manipulate strings. Try out the following:

        str1 = "This is a string that I will learn to manipulate"
        str2 = ", string manipulation is very useful."
        string = str1 + str2
        print string
        print len(string)
        print string[0]
        print string[-1]
        print string[3:7]

    We see that Python indexes a string, starting at 0, we can also use negative values to start from the end.

        index = str1.index("string")
        print index
        print str1[index:index + len("string")]

    There are various other things that can be done "on" strings, be sure to research these.

    [Video hint](http://www.youtube.com/watch?v=gHQtmCeCg1w&feature=youtu.be)

07. It is possible to go from one type of variable to another.

        f = 10.2
        print int(f)
        print float(int(f))

        s = str(f)
        print s
        print type(s)

    It is also possible to write strings using other variables.

        numberofcats = 2
        name = "Vince"
        height = 1.7
        notborn = "the UK"

    One way to do this would be:

        string = "My name is " + name +", I am " + str(height) + " metres tall, have " + str(numberofcats) + " cats and was not born in " + notborn

    Python (and most other languages) has a nicer way of doing this:

        string = "My name is %s, I am %.2f metres tall, have %i cats and was not born in %s" % (name, height, numberofcats, notborn)

    The `%` is used to denote that a value must be input in to the string. The symbols after the `%` say what type of value is to be included:

    - `s`: A String
    - `.`_x_`f`: A float rounded to _x_ decimal places
    - `i`: An integer

    There are other types that can be used as well.

    [Video hint](http://www.youtube.com/watch?v=LlQ7q-EaDnc)

    **If statements**

    ---

08. An `if` statement allows you to tell a program to carry out something based on the value of a `Boolean` variable.

        boolean = True
        if boolean:
            print "boolean is %s" % boolean

    Try typing the above code but change `boolean` to `False`. **Note: in Python, indentation is important! In all languages it is good practice, in Python it is a requirement**.

    It is easy to create boolean variables using the following:

    - `<` strictly less than
    - `>` strictly greater than
    - `<=` less than or equal
    - `>=` greater than or equal
    - `!=` not equal
    - `==` equals **Note: this is a test of equality as opposed to the basic `=` which is an assignment.**

    It is also possible to give alternatives to an `if statement`:

        num = 11
        print num % 2 == 0
        if num % 2 == 0:
            print "num is an even number"
        else:
            print "num is an odd number"

    (The `%` operator gives the remainder of one number when divided by another. Note that this is not the same use as discussed in question 7 within strings.)

    [Video hint](http://www.youtube.com/watch?v=ZODKm7YolkQ)

    **Spend some time understanding the `elif` statement.**

09. **TICKABLE**: Find some information on the `raw_input` statement and write some code that prompts a user to input a string. If the length of that string is more than 10 then print "that string has length strictly more than 10" otherwise "that string has length less than 9".

    [Video hint](http://www.youtube.com/watch?v=4nH-vtBrKXs)

    **Loops**

    ---

    An important type of programming instruction allows us to make a program repeat certain things. These are also referred to as loops. There are two basic types of loops "count controlled loops" and "event controlled loops".

10. The `range()` function in Python allows us to create a list of integers easily. **A list is a new type of variable that we will look at more closely next week**:

        print range(10)

    Note that this gives a list starting at 0 of size 10 (so it goes up to the integer 9). We can include 2 arguments in to this function:

        print range(3,10)

    We can also include 3 arguments:

        print range(0,10,2)

    Using `range()` we can use the basic `for` loop in Python (a type of count controlled loop):

        for i in range(10):
            print i

    The first line of the above defines the iterator `i` and tells it the values it will go through.

    ![]({{site.baseurl}}/assets/Images/W02-img01.png)

    We can in fact iterate over anything in a list:

        for e in ["dog", "cat", 3, "I love mathematics"]:
            print e

    This allows us to do various interesting things. Try the following:

        s = 0
        for i in range(1001):
            s += i
        print s

    [Video hint](http://www.youtube.com/watch?v=3ht1mNULJC0)

11. **TICKABLE**: Modify the above code so that it calculates the sum of the first integers less than 1000 that are not divisible by 3.

    [Video hint](http://www.youtube.com/watch?v=1PvEXo0l1NE)

12. Event based loops are implemented in Python using a `while` command that keep repeating a set of commands until a boolean variable is `False`.

        k = 0
        while k < 10:
            print k
            k += 1


    The second line of the above checks the boolean variable `k < 10` and as long as this is `True` loops through the rest of the commands:

    ![]({{site.baseurl}}/assets/Images/W02-img02.png)

    [Video hint](http://www.youtube.com/watch?v=Rog3YAETP-Q)

13. **TICKABLE**: Write some code to find \\(N\\) such that \\(\sum_{i=0}^Ni^2\\) is more than 20000.

    [Video hint](http://www.youtube.com/watch?v=tzc4uaJaYHU)

14. It can be shown (you are not required to check this) that the following sequence:

    $$x_{n+1} = \frac{x_n+K/x_n}{2}$$

    approaches \\(\sqrt{K}\\) as \\(n\\) increases. Write some code to verify this to any given level of precision.

    [Video hint](http://www.youtube.com/watch?v=bHv2vqPliL0)

15. Take a look at the `random` Python library (we will talk about libraries in detail later) and write some code that uses the `input` function to code a simple game:

    - The program chooses a random integer;
    - The user tries to guess the integer;
    - At every guess the program indicates if the guess is too high or too low.

    [Video hint](http://www.youtube.com/watch?v=TpQgPKEhrg0)

