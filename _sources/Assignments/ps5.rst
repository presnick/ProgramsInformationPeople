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

* Before Monday's class:
    * Read :ref:`Defining Functions<functions_chap>`, and do the exercises in that chapter


.. usageassignment:: prep_09
    :chapters: Functions
    :assignment_name: Prep 09
    :deadline: 2016-02-08 19:40:00
    :pct_required: 80
    :points: 50

* By Tuesday midnight:
    * Read *The Most Human Human*, Chapter 10, p.219-237.
    * Answer `Reading Response 6 <https://umich.instructure.com/courses/48961/assignments/57682>`_ on Canvas.

* Before Wednesday's class:
    * Read :ref:`While loops<while_chap>`, and do the exercises in that chapter
    * Read :ref:`Installing a text editor<text_editor_installation>` and the subsequent sections on installing and running python. Do the exercises and installations.


.. usageassignment:: prep_10
    :chapters: IndefiniteIteration
    :subchapters: Installation/TextEditor
    :assignment_name: Prep 10
    :deadline: 2016-02-10 19:40:00
    :pct_required: 80
    :points: 50

* By Sunday 2/14 evening:
   * Save answers to the exercises in Problem Set 5: :ref:`Problem Set 5 <problem_set_5>` by **5PM**
   * Upload your **Demonstrate Understanding** assignment to Canvas by **6PM**


.. _unix_pset5:

Unix Problems - Native Python Interpreter and Text Editor
---------------------------------------------------------

Turn these in as screenshots via Canvas > Assignments > Unix Problems 5. **These Unix problems are especially important for the rest of the semester. If this does not work for you or you have any questions, contact the instructional team/come to office hours.**

#. Make a new file in your text editor (Sublime Text), and save it as ``new_program.py``. (This is a Python program!)

#. In your ``new_program.py`` file, write the following code (copy it from here).

.. code:: python

   def cool_machine(x):
       y = x**2 +7
       print y

   z = 65.3
   print z + cool_machine(8)

Then, run the Python program in your native Python interpreter, by executing the unix command ``python new_program.py`` (Note: you will have to be connected to the right directory!). You should get an error. Take a screenshot of this and upload it to Canvas.

In a text editor (Sublime Text), make edits to this code so it will work (the only output should be 136.3), saving it with a different name (``fixed_program.py``). Try running it and see that it prints out a result, without an error. Take a screenshot that shows the text editor with the correct code and the successfully run program in your command prompt, and upload it to Canvas.

.. note::

    You may discover another way to run your python program directly from Sublime Text. We have found that this will not work for everything you need to do throughout the semester. Therefore, it's very important that you learn how to run your python programs from the unix command prompt, including figuring out how to connect to the right directory with the unix ``cd`` command. You will only get credit for these unix problems if your screenshots show that you ran the programs from the unix command prompt.

.. _problem_set_5:

Problem Set
-----------

.. datafile:: timely_file.txt
    :hide:

    Autumn is interchangeably known as fall in the US and Canada, and is one of the four temperate seasons. Autumn marks the transition from summer into winter.
    Some cultures regard the autumn equinox as mid autumn while others, with a longer temperature lag, treat it as the start of autumn then. 
    In North America, autumn starts with the September equinox, while it ends with the winter solstice. 
    (Wikipedia)

1. Take a look at the code below. The function subtract_five is supposed to take one integer as input and return that integer - 5. You'll get an error if you run it as is. Change the function so it works and passes the test!

.. activecode:: ps_5_1

   def subtract_five(inp):
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

2. Write code **that will keep printing what the user inputs over and over until the user enters the string "quit".**

.. activecode:: ps_5_2

   # Write code here

   ====

   print "\n---\n\n"
   print "There are no tests for this problem"


3. Define a function called change_amounts that takes one integer as input. If the input is larger than 10, it should return the input + 5. If the input is smaller than or equal to 10, it should return the input + 2.

.. activecode:: ps_5_3

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


4. We've given you another data file in this problem. It's called ``timely_file.txt``. Write code to figure out which is the most common word in the file. Save the string that is most common word in the file in the variable ``abc``. (Hint: there was a problem on last week's problem set that is very similar to this one.)

.. activecode:: ps_5_4
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


5. Here's another bit of code that generates an error. Think about what's going on with the code below that causes a problem. Write a comment explaining why an error occurs. Then fix line 5 so that it does not generate an error.

.. activecode:: ps_5_5

    def change_amounts(yp):
       n = yp - 4
       return n * 7

    print yp

    ====

    print "\n---\n\n"
    print "There are no tests for this problem"

7. See comments and code below for instructions.

.. activecode:: ps_5_7

    # Here is a function definition. DO NOT change it!
    def list_end_with_string(new_list):
        if type(new_list[-1]) == type("hello"):
            return new_list
        new_list.append("the last element is a string no matter what now!")
        return new_list

    # Play around with this function with the following function calls.
    l = [3,46,6]
    b = [4,"hi",10,"12",12,123,"whoa!"]
    print list_end_with_string([1,2])
    print list_end_with_string(l)
    print list_end_with_string(b)

    # Now write a couple invocations of this function yourself below this line.

    # Finally, write a few sentences in comments that explain what's happening in this function called list_end_with_string. You should explain what happens if a list like l gets input into this function AND what happens if a list like b gets input into it.

8. Define a function ``is_prefix`` that takes two strings as inputs and returns the boolean value ``True`` if the first string is a prefix of the second string, but returns ``False`` otherwise.

.. activecode:: ps_5_8

      # Define your function here.


      # Here's a couple example function calls, printing the return value
      # to show you what it is.
      print is_prefix("He","Hello") # should print True
      print is_prefix("Hello","He") # should print False
      print is_prefix("Hi","Hello") # should print False
      print is_prefix("lo","Hello") # should print False
      print is_prefix("Hel","Hello") # should print True
      # Remember, these won't work at all until you have defined a function called is_prefix

      ====

      print "\n---\n\n"
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


    ====
    
    print "\n---\n\n" 
    print "There are no tests for this problem."
