..  Copyright (C)  Paul Resnick, Jaclyn Cohen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Functions In Class Code Samples
===============================

This first code box is provided for your convenience: you can put any code in here and try things out.

.. activecode:: session9_free

    # You can put any code here.


For each of the following code samples, answer these questions:

* How many inputs (arguments) does this function take?
* What type of inputs (arguments) does this function expect?
* What does this function return?
* What will print out?

.. activecode:: session9_0


    def get_last_letter(s):
        return s[-1]

    # example invocations of get_last_letter function

    # here are some values stored in variables 
    # which you could use as input to the function
    original_str = "the quick brown rhino jumped over the extremely lazy fox"
    another_str = "by a route obscure and lonely, haunted by ill angels only"

    get_last_letter(original_str)
    # in a print statement
    print get_last_letter(original_str)
    # in an assignment statement
    lett = get_last_letter(another_str)
    print lett


.. activecode:: session9_1
    
    def show_key_val_pairs(diction):
        for key in diction:
            print key, diction[key]
        return None
    
    # example invocation of the show_key_val_pairs function
    animals = {'cows': 2, 'chickens': 8, 'pigs': 4, 'mice': 72, 'cats': 9,'dogs': 1}
    new_diction = {"autumn":"spring", "well":"spring", "4":"seasons","23":345} 

    # predict what will print out here before you try it!
    show_key_val_pairs(animals)
    print show_key_val_pairs(animals)

    show_key_val_pairs(new_diction)
    res = show_key_val_pairs(new_diction)
    print res


.. activecode:: session9_2

    def find_list_element(inp_lst, num):
        return inp_lst[num]

    # example invocations of find_list_element
    L = [2,"hello",4,7,False,9.6,5]
    new_L = ["106","206","330","334","110"]

    n = find_list_element(L,3)
    print n

    b = find_list_element(L,-2)
    print b

    print find_list_element(new_L,1)

    print "I am in the class with the number", find_list_element(new_L,0)


.. activecode:: session9_3

    def get_acronym(list_of_strs):
        accum_str = ""
        for s in list_of_strs:
            accum_str = accum_str + s[0]
        return accum_str

    # example invocations
    words = ["PRAY", "YOU", "TOOK", "HER", "ONLY", "NEEDLE"]
    print get_acronym(words)
 
    print get_acronym(["YO","IS","KRAZY-GLUE","EVEN","SURPRISING"])


.. activecode:: session9_4

    def get_list_of_even_nums(list_of_ints):
        accum_lst = []
        for num in list_of_ints:
            if num % 2 == 0:
                accum_lst.append(num)
        return accum_lst

    # example invocations
    li = [2,5,7,4,10,12,3]

    print get_list_of_even_nums(li)

    print get_list_of_even_nums([3,3,7])


Multiple function calls in the same expression!

.. activecode:: session9_5


    def prof_resnick_function(x):
        return x*x
    def jackie_function(y):
        return y +3  
    def student_function(z):
        return z * 2

    print prof_resnick_function(jackie_function(student_function(2)))


Local and global scope: BE CAREFUL.

.. activecode:: session9_6

    x = 4
    z = 17

    def prof_resnick_function(x):
        return x*x
    def jackie_function(x):
        return x + 3
    def student_function(x):
        return x * 2

    print prof_resnick_function(jackie_function(student_function(2)))



.. activecode:: session9_7

    # BAD - Don't do stuff like this with function definitions
    accum = 0

    def how_many_letter(letter,sentence):
        for ch in sentence:
            if ch == letter:
                accum += 1
        return accum

    # GOOD

    def better(letter,sentence):
        accum = 0
        for ch in sentence:
            if ch == letter:
                accum += 1
        return accum

    # try invoking this function

    # sample sentences to use
    s1 = "by a route obscure and lonely, haunted by ill angels only"
    s2 = "when you come to a fork in the road, take it"
    s3 = "small example"

    print how_many_letter('a', s1)
    print how_many_letter('x', s3)

    print better('a', s1)
    print better('x', s3)


``return`` ends the execution, even if there's more code

.. activecode:: session9_8

    def f(nums):
        accum = 0
        for num in nums:
            accum += num
            return accum
        print "all done"

    print f([2, 4, 6, 8])

Without a ``return`` statement, the function returns None, when it runs out of code to execute (at the bottom of the function).

.. activecode:: session9_9

    def f(nums):
        accum = 0
        for num in nums:
            accum += num
        print "all done"

    print f([2, 4, 6, 8])

You have to do something with returned values, else they get discarded

.. activecode:: session9_10

    def f(nums):
        accum = 0
        for num in nums:
            accum += num
        return accum

    f([2, 4, 6, 8])

Write a function definition that takes three numbers as inputs and returns the sum of all three

.. activecode:: session9_11

    # define your function here


    # invoke your function here and print out the results


