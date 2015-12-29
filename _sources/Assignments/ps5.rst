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


3. Write code **that will keep printing what the user inputs over and over until the user enters the string "quit".**

.. activecode:: ps_5_3

   # Write code here

   ====
   print "\n---\n\n"
   print "There are no tests for this problem"



4. Given the string in the code below, write code to figure out what the most common word in the string is and assign that to the variable ``abc``. (Do not hard-code the right answer.) Hint: dictionaries will be useful here.

.. activecode:: ps_5_4

   s = "Will there really be such a thing as morning in the morning"
   # Write your code here...
    
   ====
    
   print "\n---\n\n"
   import test
   print "testing whether abc is set correctly"
   try:
     test.testEqual(abc, 'morning')
   except:
     print "The variable abc has not been defined"


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

6. 


8. An exercising on defining and calling a function. See comments for instructions.

.. activecode:: ps_5_8

      # Define a function is_prefix that takes two strings and returns
      # True if the first one is a prefix of the second one, but returns
      # False otherwise.



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
        print "Looks like the function is_prefix has not been defined or has an error"


9. Define a python function ``grep`` that works just like the unix command. It takes two inputs, a string and a filename. It should return a list of all and only the lines in the file that contain the string.

.. activecode:: ps_5_9
   :available_files: timely_file.txt

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



