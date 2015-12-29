:orphan:

..  Copyright (C) Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. highlight:: python
    :linenothreshold: 500

Activities through 2/14
=======================

You have the following graded activities:





.. _problem_set_5:

Problem Set
-----------

.. datafile:: timely_file.txt
	:hide:

	Autumn is interchangeably known as fall in the US and Canada, and is one of the four temperate seasons. Autumn marks the transition from summer into winter.
	Some cultures regard the autumn equinox as mid autumn while others, with a longer temperature lag, treat it as the start of autumn then. 
	In North America, autumn starts with the September equinox, while it ends with the winter solstice. 
	(Wikipedia)

1. Define a function called add_three, which takes one integer as input and returns that integer + 3.

.. activecode:: ps_4_4

    # Write your code here.
    # (The tests for this problem are going to try to CALL the function that you write!)

    ====

    import test
    try:
      print "testing if add_three(2) equals 5"
      test.testEqual(add_three(2),5)
      print "testing if add_three(33) equals 36"
      test.testEqual(add_three(33),36)
    except:
      print "The function add_three has not been defined yet, OR it hasn't been defined properly"

2. Take a look at the code below. The function subtract_five is supposed to take one integer as input and return that integer - 5. You'll get an error if you run it as is. Change the function so it works and passes the test!

.. activecode:: ps_5_2

   def subtract_five(inp)
   	print inp - 5
	return None

   y = subtract_five(9) - 6

   ====

   print "\n---\n\n"
   import test
   try:
    print "testing if y is -2"
    test.testEqual(y, -2)
   except:
    print "The variable y was deleted or is not defined"

3. Write code **that will keep printing what the user inputs over and over until the user enters the string "quit".**

.. activecode:: ps_5_3

   # Write code here

   ====
   print "\n---\n\n"
   print "There are no tests for this problem"


4. Define a function called change_amounts that takes one integer as input. If the input is larger than 10, it should return the input + 5. If the input is smaller than or equal to 10, it should return the input + 2.

.. activecode:: ps_5_4

    # We've started you off with the first line...
    def change_amounts(num_here):
       pass # delete this line and put in your own code for the body of the function.

    ====

    print "\n---\n\n"
    import test
    try:
      print "testing if change_amounts(9) equals 11"
      test.testEqual(change_amounts(9),11)
      print "testing if change_amounts(12) equals 17"
      test.testEqual(change_amounts(12),17)
    except:
      print "The function change_amounts has not been defined properly"


5. We've given you another data file in this problem. It's called ``timely_file.txt``. Write code to figure out which is the most common word in the file. Save the string that is most common word in the file in the variable ``abc``. (Hint: there was a problem on last week's problem set that is very similar to this one.)

.. activecode:: ps_5_5

   # Write code here!
    
   ====
    
   print "\n---\n\n"
   import test
   try:
     print "testing whether abc is set correctly"
     test.testEqual(abc, 'the')
   except:
     print "The variable abc has not been defined"


6. Here's another bit of code that generates an error. Think about what's going on with the code below that causes a problem. Write a comment explaining why an error occurs. Then fix the 4th line of code so that it does not generate an error.

.. activecode:: ps_5_6

    def change_amounts(yp):
	   n = yp - 4
	   return n * 7

    print yp

    ====

    print "\n---\n\n"
    print "There are no tests for this problem"

7. Here will be a question about returning in the middle of a function -- maybe a two-part question? This pset is getting real important.

8. Define a function ``is_prefix`` that takes two strings as inputs and returns the boolean value ``True`` if the first string is a prefix of the second string, but returns ``False`` otherwise.

.. activecode:: ps_5_8

      # Define your function here.


      # Here's a couple example function calls, printing the return value
      # to show you what it is.
      print is_prefix("He","Hello") # should print True
      print is_prefix("Hi","Hello") # should print False
      print is_prefix("lo","Hello") # should print False
      print is_prefix("Hel","Hello") # should print True

      ====

      import test
      try:
        print 'testing whether "Big" is a prefix of "Bigger"'
        test.testEqual(is_prefix("Big", "Bigger"), True)
        print 'testing whether "Bigger" is a prefix of "Big"'
        test.testEqual(is_prefix("Bigger", "Big"), False)
        print 'testing whether "ge" is a prefix of "Bigger"'
        test.testEqual(is_prefix("ge","Bigger"), False)
        print 'testing whether "Bigge" is a prefix of "Bigger"'
        test.testEqual(is_prefix("Bigge","Bigger"),True)
      except:
        print "Looks like the function is_prefix has not been defined or has another error"


9. Define a python function ``grep`` that works just like the unix command ``grep``. Your function should take two inputs, a string and a filename. It should return a list of all the lines in the file that contain the string, and only the lines in the file that contain the string.

.. activecode:: ps_5_9

   # Write code here!

   ====

   print "\n---\n\n"
   import test
   def solgrep(a, b):
     lines = open(b, 'r').readlines()
     acc = []
     for l in lines:
       if a in l:
         acc.append(l)
     return acc
   try:
     print "testing whether grep('autumn', 'timely_file.txt') returns the right two lines"
     test.testEqual(grep('autumn', 'timely_file.txt'), solgrep('autumn', 'timely_file.txt'))
     print "testing whether grep('fool', 'timely_file.txt') correctly returns an empty list"
     test.testEqual(grep('fool', 'timely_file.txt'), solgrep('fool', 'timely_file.txt'))
   except:
     print "The function grep has not been defined yet"


10. Write code that repeatedly asks the user to input numbers. Keep going until the sum of the numbers is 21 or more. Print out the total.

.. activecode:: ps_5_10

    # Write your code here!



