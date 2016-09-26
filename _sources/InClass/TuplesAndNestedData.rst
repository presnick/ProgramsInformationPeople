..  Copyright (C)  Paul Resnick, Jaclyn Cohen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


Tuples and Nested Data 
=======================

.. activecode:: session13_free
    
    # This is provided for your convenience. You can write any code here.


Tuples
------

.. activecode:: session13_0
    
    # iterating over lists of tuples 
    for z in [(3, 4), (5, 6)]:  # list of tuples
        print z[0], z[1] # each thing z is one tuple

    for (x, y) in [(3, 4), (5, 6)]:
        print x, y 

    list_of_tups = [("birds",2,"small"), ("cats",4,"medium"),("lions",3,"big")]
    for tup in list_of_tups:
        print tup[0], "are", tup[2]


.. activecode:: session13_1

    # swapping variable values
    # powerful!

    x = 5
    y = 4

    z = 3
    b = 2

    # reference diagram
    # swap z and b
    temp = z
    z = b
    b = temp
    print "z is", z
    print "b is", b

    print "before swap"
    print "x is", x
    print "y is", y
    # easier way to swap values - swap x and y
    x,y = y,x

    print
    print "after swap"
    print "x is", x
    print "y is", y


.. activecode:: session13_2
    
    # Borrowed from the exercise from textbook chapter
    julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
    claude = ("Claude", "Shannon", 1916, "A Mathematical Theory of Communication", 1948, "Mathematician", "Petoskey, Michigan")
    alan = ("Alan", "Turing", 1912, "Computing machinery and intelligence", 1950, "Mathematician", "London, England")

    people = [julia, claude, alan]

    # using tuple packing
    # print out only the years people were born
    years = julia[2],claude[2],alan[2]
    print years 

    print "-----"

    # want to just print each year on its own
    for p in people:
        print p[2] # indexing into the tuple -- same mechanics as lists!

    # unpacking -- save a bunch of values into different variables on one line
    julia_year, claude_year, alan_year = years

    # then can do stuff with one at a time really easily
    print "Claude Shannon was born in", claude_year


.. activecode:: session13_2a

    # Very neat for function parameter passing
    def rectangle_area(length, width):
        return length * width

    rectangle_dimensions = [(3,4), (9,5), (11,2)]
    for dim in rectangle_dimensions:
        print rectangle_area(*dim)

.. activecode:: session13_3

    # Also for return values
    # Remember functions only return 1 value -- 
    # With tuples, 1 value can hold multiple pieces of data

    # Here's most of a function that takes a dictionary as input with
    # key-value pairs that are names as keys 
    # and integers as values. 
    # The values represent the score that person got in a game.
    # For example, {"Nick":12,"Ayo":15,"Lauren":21}

    # The function should return a tuple: 
    # the name of the person who got the highest score, and their score

    def highest_scoring(score_diction):
        keys = score_diction.keys() # could also use .items(), but that would lead to different code
        max_key_so_far = keys[0]
        for k in keys:
            if score_diction[k] > score_diction[max_key_so_far]:
                max_key_so_far = k
        # FILL IN THE RETURN STATEMENT

    # example invocation code

    sd = {"Nick":12,"Ayo":15,"Lauren":21}
    sd2 = {"Natalie":62,"Jackie":35,"Jaime":44}

    print highest_scoring(sd) # should print: Lauren 21
    print highest_scoring(sd2) # should print: Natalie 62
    # Like strings, tuples print a little different than they're represented in code


.. activecode:: session13_4
    
    # Here's a somewhat complex example.
    # What does this code do?

    def user_type_numbers(limit_number):
        tot = 0
        list_of_nums = []
        while tot < limit_number:
            num = int(raw_input("Enter a number:"))
            tot = tot + num
            list_of_nums.append(num)
        return limit_number, tot, len(list_of_nums)

    # example invocations
    returned_info = user_type_numbers(11)

    print returned_info

    # You can use that one tuple, stored in a variable, to print something like this
    # Got here with just one function invocation!

    print "We asked the user to input numbers until the sum of the numbers was more than", returned_info[0], "and they entered", returned_info[2], "numbers, and got a sum of", returned_info[1]


Nested Data
-----------

.. activecode:: session13_5

    x = [[1, 2, 3], [4, 5], [6, 7]]

    #With nested data, each level of nesting requires one level of extraction

    # With indexing

    y = x[1] #[4, 5]
    z = y[0] 
    print z # 4

    # Same thing in one line
    w = x[1][0]
    print w # 4

    # or just
    print x[1][0]

    #OR printing pieces of nested data with iteration

    #for lst in x:
    #    print lst[0]

    #for lst in x:
    #    for item in lst:
    #        print item

    #print x 
    #print x[1]
    #print type(x[1])

    #for item in x[1]:
    #    print item



.. activecode:: session13_7

    nd = {"hello":{"inner key":[1,2,3,4],"another key":[10,20,30,40]},"favorite word":"enigmatic","list of words":["green","pink","blue"]}

    print type(nd)
    #print nd.keys()
    #print nd["hello"]
    #print type(nd["hello"])
    #print nd["hello"].keys()
    #print nd["hello"]["another key"]

    #for n in nd["hello"]["another key"]:
    #   print n

    #print nd["favorite word"]

    #print nd["list of words"]

    #for w in nd["list of words"]:
    #   print w


**Exercise:** Write a function that takes as input a list of lists, like x in earlier example, and returns a count of the total number of leaf items (seven in x above).

.. activecode:: session13_8

    # Write code here

    # Here's an example list of lists to look at and make your plan
    x = [[1, 2, 3], [4, 5], [6, 7]]

