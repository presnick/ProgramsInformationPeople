..  Copyright (C)  Paul Resnick, Jaclyn Cohen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


Optional/Keyword Parameters Examples
====================================

.. activecode:: optional_key_free

    # This is provided for your convenience. You can write any code here.


The is_prefix function
----------------------


.. activecode:: is_prefix_0

    def is_prefix(s1, s2):
        return s1 == s2[0:len(s1)] 

    print is_prefix("he", "hello")

.. activecode:: is_prefix_1

    def is_prefix(s1,s2):
        if s2.find(s1) == 0: #searches for s1 in s2, where s1 starts at index 0
            return True
        else:
            return False

    print is_prefix("hel","hello")
 
.. activecode:: is_prefix_2

    def is_prefix(s1, s2):
        return s1 == s2[0:len(s1)] 
    
    print is_prefix("he", "hello") 


.. activecode:: is_prefix_ex

    def is_prefix(s1,s2):
        return s2.find(s1) == 0

    #x = 5
    x = -2

    # To illustrate what we're doing with the boolean statement
    if x > 0:
        print True
    else:
        print False
    
    #That code does exactly the same thing as the following line of code    
    print x > 0


.. activecode:: is_prefix_3

    def is_prefix(s1, s2):# not quite right; why not?
        return s1 in s2  
 
    print is_prefix("ell", "hello") 
    # will get True if the function just uses the in operator, and that's not a prefix

    # Rephrase this problem in English
    # and then translate to code (look stuff up!) 

.. activecode:: is_prefix_4

    # Example using the flag pattern you learned last week
    # Can be used in any kind of iteration, not just indefinite iteration

    def is_prefix(s1, s2):
        is_it_good = True  # This is called a Boolean "flag"
        for i in range(len(s1)):  # [0, 1]
            if s1[i] != s2[i]:
                is_it_good = False
        return is_it_good
     
    print is_prefix("hel", "hello")

Optional/Keyword Parameters Examples
------------------------------------

.. activecode:: optional_key_inclass_01

    # what should the parameter list for f be?
    def f(): # Fill in the parameter list
        print z, x, y
        
    f(1)  # should print 30 1 20    
    f(2, 3) # should print 30 2 3    
    f(3, 4, 5) # should print 5 3 4

    # Next,

    f(2, 6) # what will it print? prints 30 2 6
    f(2, z=6) # what will it print?
    f(2, x=6) # what will it print?

    # Also consider: what does the function f return?


Here's a function count_vowels that takes a string and counts how many vowels are in it.

.. activecode:: optional_key_inclass_02

    # here is a function count_vowels
    def count_vowels(s):
        vowels = ['a', 'e', 'i', 'o', 'u'] 
        ct=0 
        for ch in s:
            if ch in vowels:
                ct = ct + 1
        return ct

    # Example invocation and print statement
    print count_vowels("supercalifragilisticexpialidocious")


Now using that as a basis, you should generalise the count_vowels function, to count the occurrences of any subset of letters, not just vowels, but treat vowels as the default if not otherwise specified. Fill in the parameter list and the code.

.. activecode:: optional_key_inclass_03

    # fill in the parameter list and function body

    def count_lets():
        # fill this in


    # example invocations with print statements
    print count_lets("Once upon a midnight dreary", ['a', 'e', 'i', 'o', 'u']) 
    print count_lets("Once upon a midnight dreary", ['l', 'm', 'm', 'o'])
