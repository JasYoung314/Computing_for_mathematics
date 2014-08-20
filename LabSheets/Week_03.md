---
layout      : post
categories  : labsheets
title       : Week 3 - Functions and Data Structures
playlisturl : http://www.youtube.com/playlist?list=PLnC5h3PY-znxclcsx-JIwgFqGTXMdItOH
comments    : true
---

This lab sheet will introduce various data structures and also an important concept called 'recurrence'. After this session you will know how to:

+ Create and manipulate lists;
+ Create and manipulate dictionaries (hash tables);
+ Write data to a file using the `write` and `read` functions;
+ Use the csv python module to read and write csv files;
+ Program some basic algorithms using recurrence.

A YouTube playlist with all the videos for this lab sheet can be found [here](http://www.youtube.com/playlist?list=PLnC5h3PY-znxclcsx-JIwgFqGTXMdItOH).

**Functions**

---

To be able to make progress from the basic on this sheet we need a way to write "recycle" code: functions. Much like mathematical functions, functions in programming can take multiple arguments and carry out tasks with those arguments.

![]({{site.baseurl}}/assets/Images/W02-img03.png)

01. The following code defines a very simple function (with no arguments):

        def printhello():
            print "Hello"

    The name of the function is `PrintHello` and `def` is the Python syntax used to define it. When we run the above two lines of code, nothing is output. To call the function we simply write:

        printhello()

    We can modify our function to take an argument:

        def printhello(name):
            print "Hello, " + name

    [Video hint](http://www.youtube.com/watch?v=I_DXaP-mrRA)

02. The following function makes use of the `return` call to actually return a result of the function:

        def mydiv(a, b):
            return a/b

    [Video hint](http://www.youtube.com/watch?v=0cA2VNcc54A)

03. **TICKABLE**: Include a check in the `MyDiv` function to ensure that no division by 0 is attempted.

    [Video hint](http://www.youtube.com/watch?v=KxdJVw-06KE)

04. **TICKABLE**: Create a function that returns the sum of the first $K$ integers not divisiable by $B$. Investigate "using optional arguments" and set $K$ and $B$ to have default values 10000 and 3 respectively.

    [Video hint](http://www.youtube.com/watch?v=hjv8sAlYPDw&feature=youtu.be)

05. Create a function that return the square root of a number using the algorithm suggested in question 14. Write some code that compares the output of this algorithm to the actual square root for the first 10000 digits.

06. **TICKABLE**: Write a function `Fibonacci` that uses loops to calculate the \\(n\\)th number of the Fibonacci sequence:

    $$X_n=\begin{cases}1,& n=0,1\\
    X_{n-1}+X_{n-2}\end{cases}$$

    [Video hint](http://www.youtube.com/watch?v=4ZxBLkLRPXQ)


    **Writing clear code**

    ---

    When writing code it is **very important** to include comments throughout. How well commented code is will be evaluated throughout this module. Comments should be thought of as messages explaining what instructions are being given by the code. This is useful to the writer of the code but more importantly to anyone who might want to add/modify the code.

    There are two ways of writing comments in Python:

    - Use the `#` to indicate to the interpreter that everything that is about to follow on a given line is to be ignored.
    - Use `"""` to indicate the beginning and end of multi line comments (note that this can also be used to write multi line strings).

07. The following is an example of a single line comment in the middle of some code:

        num = 2
        num += 3  # Add 3 to num
        print num

08. The following is an example of a multilined comment in the definition of a function:

        def myfunc(a,b):
            """
            This function calculates the ratio of two numbers raised to the sum of the two numbers.

            Arguments:
                a: the first number
                b: the second number

            Output: (a / b) ** (a + b)
            """
            return (a / float(b)) ** (a + b)

09. **TICKABLE**: One final aspect that is very important when writing code is **convention**. When working on a project with multiple people for example being able to use the same convention can be very beneficial. The most commonly known convention for Python is [PEP8](http://www.Python.org/dev/peps/pep-0008/). You are advised to use the following general summary of PEP8 for this course:

    - Variable and function names

          Use a descriptive `lowercase` (all lowercase characters) for variable and function names.

      Yes:

              myvariable
              sqrtvar
              var
              myfunction

      No:

              my_variable
              SqrtVAR
              MyFunction
              MYFUNCTION


      On some occasions it might be appropriate to make some exceptions (for example using a single letter for a very simple variable).

    - White spaces

      Include a whitespace between operators (`+`, `-`, etc) and a whitespace after a comma `,`.

      Yes:

            print 2 + 2
            myfunc(3, 4)

      No:

            print 2+2
            myfunc(3,4)

      Include 2 whitespaces before an inline comment `#` at the end of a line of code.

      Yes:

            # Just leave a space after the comment symbol if on a single line
            print 2 + 2  # but if you comment at the end of a line leave 2 whitespaces.

      No:

            print 2 + 2 # So this is not enough space.

      Also include two blank lines before the definition of a function.

      Yes:

            print 2 + 2


            def myfunc():
                print 2 + 2

      No:

            print 2 + 2

            def myfunc():
                print 2 + 2

    - Comments

      Comment well and comment often. In particular use the following convention for functions:

            afunc():
                """
                Always start a function with a multiline comment to describe what it does.

                Arguments: List the arguments and what format they should be in.

                Output: List the expected output of the function.
                """

      As and when we see new topics on this course we will also discuss the corresponding conventions.

    Go back through your previously written code and ensure that you have used the above convention.

    **Lists**

    ---

    Lists are a particular object in Python that hold ordered collection of other objects. In other languages they are sometimes called 'arrays'. You can think of these as baskets that allow you to hold objects. You can put anything in lists:

    + Numeric variables;
    + Character variables;
    + Other lists;
    + and various other 'things'.

10. **TICKABLE**: The following code creates a list with the numbers from 1, to 10.

        alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    We can manipulate lists in a similar way to strings. Try the following:

        blist = [30, 40, 50, 60]
        clist = alist + blist
        print clist
        print len(clist)
        print clist[0]
        print clist[-1]
        print clist[3:12]

    We see that python indexes lists just like strings: starting at 0. We can also use the `index` function as for strings. Try:

        index = clist.index(40)
        print index
        print clist[index:index + 2]

    [Video hint](http://www.youtube.com/watch?v=7FbYcOOB64c)

11. We have seen how to combine two lists using `+` but there is a very useful method on lists called the `append` method. With this we can easily add elements to lists:

        mylist = []
        for i in range(11):
            if i % 2 == 0:
                mylist.append(i)
        print mylist

    This makes use of the range function that we see in the previous lab sheet.

    [Video hint](http://www.youtube.com/watch?v=DWiHBdf5mQI)

12. **TICKABLE** Create a list with the first 1300 integers divisible by 3. What is the largest such number?

    [Video hint](http://www.youtube.com/watch?v=7KxOxWC3h78)

13. There is another way of creating/manipulating lists in python called list _comprehensions_. The following code give the squares of the first 10 integers:

        squares = [e ** 2 for e in range(1, 11)]
        print squares

    We can include logical statements to only give the squares of odd numbers:

        squares = [e ** 2 for e in range(1, 11) if e % 2 == 1]
        print squares

    [Video hint](http://www.youtube.com/watch?v=8WXIY18RJiY)

14. **TICKABLE** By creating a function and using list comprehensions, create a list of \\(f(n)\\) for all integers \\(n\leq 100\\) where \\(f(n)\\) is given below:

    $$f(n) = \begin{cases}
       n ^ 3,& \text{ if $n$ odd}\\
       n ^ 2 + 1,& \text{ if $n$ is divisible by }4\\
       n - 1,& \text{otherwise}
    \end{cases}$$

    [Video hint](http://www.youtube.com/watch?v=cr_QV3fF-Ls)

15. There are various other things that we can do to a list. Including getting the highest, lowest values as well as the length of the list:

        alist = [1,74,2,100,-123]
        print max(alist)
        print min(alist)
        print len(alist)

    [Video hint](http://www.youtube.com/watch?v=JslPoHRe3kk)

    **Dictionaries in Python**

    ---

16. **TICKABLE** In computer science 'hash tables' are used as an efficient way to find particular data that is used often. In python 'hash tables' are called dictionaries. To understand this consider the following list of lists:

        badphonebook = [["Vince", 3],
                        ["Zoe", 2],
                        ["Julien", 6],
                        ["Thomas", 10],
                        ["Mike", 1],
                        ["Matt", 4]]

    (Note that you can write lists over multiple lines)

    To find a particular phone number in this phone book we would need to go through every element of the phone book to check if it was the right one:

    ![]({{site.baseurl}}/assets/Images/W03-img01.png)

        def searchpb(target):
            for e in badphonebook:
                print "Checking %s" % e
                if e[0] == target:
                    return e[1]
            return "%s not in phonebook" % target

    Code this function and use it to find all the phone numbers in the above phone book. Try to find some strings that are not in the phone book.

    **In reality this is not how a phone book is designed.** Names are in a given order (alphabetical) and so it is easier to know _where a name is supposed to be_. This is implemented in python using 'dictionaries' which are an **unordered set of _key:value_ pairs**.

    ![]({{site.baseurl}}/assets/Images/W03-img02.png)

    This code creates the above phone book as a dictionary with the names as _keys_ and the numbers as their _values_:

        goodphonebook = {"Vince": 3,
                            "Zoe": 2,
                            "Julien": 6,
                            "Thomas": 10,
                            "Mike": 1,
                            "Matt": 4}

    (Note that you can write dictionaries over multiple lines)

    To query a dictionary we can use the `get` method:

        goodphonebook.get("Thomas")
        goodphonebook.get("Brayden")
        goodphonebook.get("Brayden", 'Not in book')
        goodphonebook.get("Thomas", 'Not in book')

    We can also modify an element of a dictionary as follows:

        print goodphonebook['Vince']
        goodphonebook['Vince'] = 8
        print goodphonebook['Vince']

    We must just be careful as if we use square brackets for a value that is not in a dictionary we will obtain an error:

        print goodphonebook['Brayden']
        goodphonebook['Brayden'] = 12
        print goodphonebook['Brayden']

    **Note: A key must be a string or a numerical variable. The associated value of a key can be anything.**

    [Video hint](http://www.youtube.com/watch?v=CuyHg-1Let0)

17. Iterate over the list `badphonebook` to initiate the `pb` as the equivalent dictionary:

        pb = {}
        for e in badphonebook:
            ...

    [Video hint](http://www.youtube.com/watch?v=ZZv2sB57BgA)

18. Note that it is also possible to iterate over keys in a dictionary:

        for e in goodphonebook:
            print goodphonebook[e]

    [Video hint](http://www.youtube.com/watch?v=cZWwJgvRbBE)


