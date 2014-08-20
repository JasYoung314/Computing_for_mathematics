---
layout      : post
categories  : labsheets
title       : Week 4 - Writing and Reading Files, Recursion and Algorithms
playlisturl : http://www.youtube.com/playlist?list=PLnC5h3PY-znyEYYOnDbQHq1PUuNgbhdD3
comments    : true
---

This lab sheet will introduce two algorithms from computer science. After this session you will be able to sort and search lists using the two following algorithms:

+ Insertion and Bubble sort algorithm;
+ Binary search.

A YouTube playlist with all the videos for this lab sheet can be found [here](http://www.youtube.com/playlist?list=PLnC5h3PY-znyEYYOnDbQHq1PUuNgbhdD3).

**Writing data to files**

---

01. **TICKABLE** All of the data we handle with variables, lists and dictionaries lives in the 'memory' of a computer when our python code is running. When the program stops running the data is lost. There will be occasions when we want to write our data to a file on the hard drive of a computer (so that it is always available even when we turn the computer off).

    To do this we need Python to open a file (usually a basic text file), write strings to the text file and then close the file. The following code opens (or creates a) text file in 'write mode' (that's what the `w` is for) and writes the numbers 1 to 10 to it:

        textfile = open('mytextfile.txt', 'w')
        for i in range(1, 11):
            textfile.write("%s\n" % i)
        textfile.close()

    Note that the string we are writing at each step of the loop ends with a `\n`. This is a special character that tells the writer to write a new line. There are other special characters such as `\t` which tells the writer to include a tabulated space.

    [Video hint](http://www.youtube.com/watch?v=HSz1A8ZHWWg)

02. To read data from a file, we need to open the file in 'read mode':

        textfile = open('mytextfile.txt', 'r')
        string = textfile.read()
        print string

    This string is not particularly helpful. To transform the string to a list we can use the `split` method which seperates a string on a given character:

        data = string.split('\n')
        print data

    All the variables in this list are still character variables. To convert them to numeric variables we can use a list comprehension:

        data = [int(e) for e in data[:-1]]

    [Video hint](http://www.youtube.com/watch?v=3ljPll8cG3A&feature=youtu.be)

03. **TICKABLE** The following function checks if a number is prime or not. Read through the function and ensure that you understand it.

        def isprime(n):
            return min([n % e for e in range(2, n)]) != 0

    The file [W03_D01.txt]({{site.baseurl}}/assets/Data/W03_D01.txt) contains a list of integers. Read in these integers and print to screen how many of them are prime. (If you would like a bit of a challenge, print to to screen the number of unique primes as the file contains various repetitions of numbers).

    [Video hint](http://www.youtube.com/watch?v=Tbv0s_GEJ1I)

04. There is a common data format called 'csv' short for 'comma separated value'. There is a python library that allows for the easy use of this format when writing a lot of data to files. Watch the following video and experiment with this library.

    [Video hint](http://www.youtube.com/watch?v=jQ9aDyBWCXI)

    **Recursion**

    ---

05. **TICKABLE** Recursion is an important technique in programming. It often allows you to write code in a much more succinct way and is intimately linked to mathematics where sequences can be defined recursively. For example, consider:

    $$X_n=\begin{cases}
    1,& n=1\\
    2X_{n-1},& n>1
    \end{cases}$$

    To calculate \\(X_3\\), we apply the formula and get:

    $$X_3=2X_2$$

    at this point we must calculate \\(X_2\\):

    $$X_2=2X_1$$

    and we now apply the formula to calculate \\(X_1\\):

    $$X_1=1$$

    so by substituting all this in to our previous equation we get

    $$X_3=4$$

    Here is an iterative approach to programming this:

        def iterX(n):
            r = 1
            for i in range(n - 1):
                r *= 2
            return r

    Experiment and understand this function to verify that it is giving the correct results.

    The following code is a **recursive** approach to programming this:

        def recX(n):
            if n == 1:
                return 1
            return 2 * recX(n - 1)

    Note that this approach is much more closely related to the actual definition of what we are trying to compute. In general we will always either be considering a _base_ case or a case than can be reduced.

    ![]({{site.baseurl}}/assets/Images/W03-img03.png)

    [Video hint](http://www.youtube.com/watch?v=EYPT4Ykx5IU)

06. **TICKABLE** Program two functions that return \\(n!\\) in both an iterative approach and a recursive approach.

07. Write a recursive program for the Fibonacci sequence.

    **Sorting Algorithms**

    ---

08. **TICKABLE** The following code creates a list of digits from 1 to 31.

        l = range(1, 31)
        print l

    If we import the random library we can pick a random sample of the list and `shuffle` this it (do not worry too much about this):

        import random
        jumbledlist = random.sample(range(1, 31), 20)
        print jumbledlist

    Using pen and paper, sort the above list, attempting to understand a general approach to doing this. Write a function `jumbledlist` that takes as arguments: `maximumnumber` and `sizeoflist` which returns a jumbled list of integers as above.

    [Video hint](http://www.youtube.com/watch?v=18LLHQ7JR1s)

09. **TICKABLE** Python has a built in method on lists to sort them: `sort()`:

        l = jumbledlist(30, 20) # Use the function you created above.
        print l
        l.sort()
        print l

    In this question we will take a look at one type of algorithm that can be used to sort a list: "Selection sort".

    The main idea behind this algorithm is to create a new (empty at first) list and go through the old list and slowly pick out the 'next' element to go in the new list.

    ![]({{site.baseurl}}/assets/Images/W04-img01.png)

    Here is some **pseudo code** that describes this:

        INITIATE NEWLIST
        WHILE MORE ELEMENTS IN NEWLIST THAN IN OLDLIST:
            FIND SMALLEST ELEMENT IN OLDLIST
            MOVE THAT ELEMENT TO NEWLIST

    It should be straightforward to see that at every step of this algorithm the sum of the sizes of NEWLIST and OLDLIST stay the same. As such we can simply put the NEWLIST at the beginning of the OLDLIST so that at each step of our algorithm we are basically moving elements from the unsorted part of the list to the sorted part of the list.

    ![]({{site.baseurl}}/assets/Images/W04-img02.png)

    Here is some **pseudo code** that describes the 'insertion sort' algorithm:

        SET FIRSTUNSORTED TO 0
        WHILE NOT SORTED:
            FIND SMALLEST UNSORTED ITEM
            SWAP FIRST UNSORTED ITEM WITH EARLIEST UNSORTED ITEM
            SET FIRSTUNSORTED TO FIRSTUNSORTED + 1

    Here is some python code that carries out the above algorithm, experiment with it and include comments:

        def insertionsort(data):
            firstUnsorted = 0
            while firstUnsorted < len(data) - 1:
                indexOfSmallest = firstUnsorted
                index = firstUnsorted + 1
                while index <= len(data) - 1:
                    if data[index] < data[indexOfSmallest]:
                        indexOfSmallest = index
                    index += 1
                data[firstUnsorted], data[indexOfSmallest] = data[indexOfSmallest], data[firstUnsorted]
                firstUnsorted += 1

    [Video hint](http://www.youtube.com/watch?v=O1HBxikerUQ)

10. There are various other algorithms that can be used to sort lists. The following pseudo code is for an algorithm called 'bubble sort'. Attempt to write out the corresponding python code:

        SET FIRSTUNSORTED TO 0
        SET SWAP TO TRUE
        WHILE FIRSTUNSORTED < LENGTH - 1 AND SWAP:
            SET SWAP TO FALSE
            "BUBBLE UP" THE SMALLEST ITEM IN AN UNSORTED LIST
            SET FIRSTUNSORTED TO FIRSTUNSORTED + 1

    Here's the pseudo code for the "BUBBLE UP" part of the above code:

        SET INDEX TO LENGTH - 1
        WHILE INDEX > FIRSTUNSORTED:
            IF DATA[INDEX] < DATA[INDEX - 1]
                SWAP DATA[INDEX] AND DATA[INDEX - 1]
                SET SWAP TO TRUE
            SET INDEX TO INDEX - 1

    [Video hint](http://www.youtube.com/watch?v=SXDWTZpj--M)

11. The 'time' module allows you to get the current system time on your machine:

        import time
        print time.time()

    Using this we can write a function that will evaluate how long it takes to run a particular function:

        def timing(string):
            starttime = time.time()
            eval(string)
            return time.time() - starttime

    This uses the `eval` function which runs any string of code. We can define the following test function:

        def testfunction():
            k = 0
            while k < 10 ** 6:
                k += 1

    We see how long a single run of this testfunction takes using our timing function:

        print timing("testfunction")

    Modify the timing function so that it returns the average time taken over 10 evaluations of the passed code. Furthermore use this function to evaluate the performance of the bubble sort and insertion sort algorithms.

    [Video hint](http://www.youtube.com/watch?v=4MC3wPCKpyg)

    (Note that python also has a timeit library which offers timing functionality.)

    **Searching algorithms**

    ---

12. **TICKABLE** Consider the data in [W04_D01.txt]({{site.baseurl}}/assets/Data/W04_D01.txt). Search this file for the index of 4558. Do this by hand and then check your answer using the `index` method. How could you do this if it was to be done in pairs (2 students searching the list)?

    [Video hint](http://www.youtube.com/watch?v=D7-3Oh_oZA4)

13. One searching algorithm we will look at is called "sequential search". This algorithm starts by sorting a list, and then going through it until it either reaches the element in question or gets to a point in the list that the item in question **should** be at.

        SORT THE LIST
        SET INDEX TO 0
        SET FOUND TO FALSE
        WHILE INDEX < LENGTH and NOT FOUND:
            IF DATA[INDEX] = ITEM:
                FOUND = TRUE
            ELSE IF DATA[INDEX] > ITEM:
                INDEX = LENGTH
            ELSE:
                INDEX = INDEX + 1
        IF FOUND:
            RETURN INDEX
        ELSE:
            RETURN "ITEM NOT IN LIST"

    Write some python code for this and use it to find the index of following numbers:

        targets = [19,
                   592,
                   9507,
                   4221]

    in the file [W04_D01.txt]({{site.baseurl}}/assets/Data/W04_D01.txt).

    [Video hint](http://www.youtube.com/watch?v=CsBlbFaZD_I)

14. **TICKABLE** Another searching algorithm is called 'binary search'. In this algorithm, a **sorted** list is split in two recursively and by considering the first and last element of each list we immediately know which sublist to search.

    ![]({{site.baseurl}}/assets/Images/W04-img03.png)

    Here is some pseudo code that describes this:

        SORT THE LIST
        SET INDEX TO 0
        SET LAST TO LENGTH - 1
        SET FOUND TO FALSE
        WHILE FIRST <= LAST AND NOT FOUND:
            SET MIDDLE TO (FIRST + LAST) / 2
            IF DATA[MIDDLE] = ITEM:
                SET FOUND TO TRUE
            ELSE:
                IF DATA[MIDDLE] > ITEM:
                    SET LAST TO MIDDLE - 1
                ELSE:
                    SET FIRST TO MIDDLE + 1
        RETURN MIDDLE

    Here is some python code that carries out the above algorithm, experiment with it and include comments:

        def binarysearch(data, item):
            data.sort()
            first = 0
            last = len(data) - 1
            found = False
            while first <= last and not found:
                middle = int((first + last) / 2)
                if item == data[middle]:
                    found = True
                elif item < data[middle]:
                    last = middle - 1
                else:
                    first = middle + 1
            if data[middle] == item:
                return middle
            return False

    [Video hint](http://www.youtube.com/watch?v=UyIhxhURX-M)

15. Use the timing function of question 4 to compare the performance of the binary search and sequential search algorithms.

16. The binary search algorithm is a very nice algorithm to write in a recursive way, attempt to do this.
