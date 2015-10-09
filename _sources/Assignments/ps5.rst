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


Activities through 10/18
========================

You have the following graded activities:

* Before Monday's class:
    * Read :ref:`While loops<while_chap>`, and do the exercises in that chapter
    * Read :ref:`Installing a Native Python Interpreter and Text Editor <next_steps>` and follow the instructions to set up for running python on your computer

* By Tuesday midnight:
    * Read `Tutorial on unix diff <http://www.computerhope.com/unix/udiff.htm>`_ (This will help you understand the section of "The Most Human Human" below).
    * Read *The Most Human Human*, Chapter 10, p.237-259.
    * Answer :ref:`Reading Response 7 <reading_response_7>`.

* By Sunday midnight 10/18:
   * Save answers to the exercises in Problem Set 5: :ref:`Problem Set 5 <problem_set_5>`


Reading Response
----------------

.. _reading_response_7:

1. Suppose you write and edit a long text file over the course of several days, saving a new version every 15 minutes or so (``myfile1.txt``, ``myfile2.txt``, ``myfile3.txt``,...). Eventually, you have 100 different versions of the file. Now consider the whole directory containing all 100 versions of the file. Would it have a lot of redundancy? As a compression technique, how might you take advantage of the unix diff command in order to reduce the total amount of space required to store all 100 versions of the file?

.. activecode:: rr_7_1

   # Fill in your response in between the triple quotes
   s = """

   """
   print s

2. Think about assigning entropy scores to people instead of documents. If you were to compute information entropy scores for all the students you've met since enrolling at the University of Michigan, which of them has the highest entropy and why?

.. activecode:: rr_7_2

   # Fill in your response in between the triple quotes
   s = """

   """
   print s



Unix Problems
-------------

.. _unix_pset5:

Turn these in as screenshots via CTools in the Assignments tab!

1. In the `tutorial on unix <, >, and |  <http://www.ee.surrey.ac.uk/Teaching/Unix/unix3.html>`_,  there are instructions for creating two files called  ``list1`` and ``list2``. Write a single unix command that displays all lines in either file that contain the letter ``p``.

2. Save a file in the ``106`` folder you created a couple weeks ago called ``fun_with_unix.txt``. Now use ``ls``, ``|`` (pipe), and ``grep`` to find all filenames in your folder containing the string ``unix``. (For fun, try this with other substrings and other folders)


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


5. We've given you another data file in this problem. It's called ``timely_file.txt``. Write code to figure out which is the most common word in the file. Again, save it in the variable ``abc``.

.. activecode:: ps_5_5
   :available_files: timely_file.txt

   # Write code here!
    
   ====
    
   print "\n---\n\n"
   import test
   try:
     print "testing whether abc is set correctly"
     test.testEqual(abc, 'the')
   except:
     print "The variable abc has not been defined"

6. Write three function calls to the function ``give_greeting``:

   * one that will return the string ``Hello, SI106!!!``
   * one that will return the string ``Hello, world!!!``
   * and one that will return the string ``Hey, everybody!``

You may print the return values of those function calls, but you do not have to.

You can see the function definition in the code below, but that's only so you can understand exactly what the code is doing so you can choose how to call this function. Feel free to make comments to help yourself understand, but otherwise DO NOT change the function definition code! HINT: calling the function in different ways and printing the results, to see what happens, may be helpful!

.. activecode:: ps_5_6

   def give_greeting(greet_word="Hello",name="SI106",num_exclam=3):
      final_string = greet_word + ", " + name + "!"*num_exclam
      return final_string

   #### DO NOT change the function definition above this line (OK to add comments)

   # Write your three function calls below


7. Define a function called mult_both whose input is two integers, whose default parameter values are the integers 3 and 4, and whose return value is the two input integers multiplied together.

.. activecode:: ps_5_7

   # Write your code here

   ====

   import test
   print "\n---\n\n"
   print "Testing whether your function works as expected (calling the function mult_both)"
   try:
      test.testEqual(mult_both(), 12)
      test.testEqual(mult_both(5,10), 50)
   except:
      print "mult_both not defined or yields an error when invoked"

8. Here's a warm up exercise on defining and calling a function:

.. activecode:: ps_5_8

      # Define a function is_prefix that takes two strings and returns
      # True if the first one is a prefix of the second one,
      # False otherwise.



      # Here's a couple example function calls, printing the return value
      # to show you what it is.
      print is_prefix("He","Hello") # should print True
      print is_prefix("Hi","Hello") # should print False
      print is_prefix("lo","Hello") # should print False

      ====

      import test
      try:
        print 'testing whether "Big" is a prefix of "Bigger"'
        test.testEqual(is_prefix("Big", "Bigger"), True)
        print 'testing whether "Bigger" is a prefix of "Big"'
        test.testEqual(is_prefix("Bigger", "Big"), False)
        print 'testing whether "ge" is a prefix of "Bigger"'
        test.testEqual(is_prefix("ge","Bigger"), False)
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

