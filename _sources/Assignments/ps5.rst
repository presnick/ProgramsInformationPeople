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

Activities through 10/14
========================

You have the following graded activities:

* **Before Monday's class 10/10:
    
  * Read :ref:`While loops<while_chap>`, and do the exercises in that chapter
  * *If you use a Windows computer,* read and do the installation in the (:ref:`instructions for installing git bash <install_git_bash>`). 
  * Read :ref:`Installing a text editor<text_editor_installation>` and the subsequent sections on installing and running python. Try to do the exercises and installations. You will address any installation problems you have (hopefully none!) in section this week. 

.. usageassignment

* **By Tuesday 10/11 11:59 pm:**
    * Read *The Most Human Human*, Chapter 10, p.219-237.
    * Answer `Reading Response 6 <https://umich.instructure.com/courses/105657/assignments/131317>`_ on Canvas.

* **Before Wednesday's class 10/12:**
    
  * Read :ref:`Unix and the Command Line<unix_chapter>`, and try out the commands you learn in Terminal, if you use a mac, or Git Bash, if you use Windows.
  * Read `this tutorial <>`_ on Unix pipes and the Unix command **grep**.

.. usageassignment

* By Friday 10/14 at 6:30 PM:
   * Complete the :ref:`Unix Exercises for Problem Set 5 <problem_set_5_unix>`. (Half the problem set)
   * Save answers to the exercises in Problem Set 5: :ref:`Problem Set 5 <problem_set_5>` (the other half of the problem set)
   * Submit your **Demonstrate Understanding** assignment on Canvas


.. _problem_set_5:

Problem Set
-----------

.. datafile:: timely_file.txt
    :hide:

    Autumn is interchangeably known as fall in the US and Canada, and is one of the four temperate seasons. Autumn marks the transition from summer into winter.
    Some cultures regard the autumn equinox as mid autumn while others, with a longer temperature lag, treat it as the start of autumn then. 
    In North America, autumn starts with the September equinox, while it ends with the winter solstice. 
    (Wikipedia)



.. question:: problem_set_5_1
    :number: 1

    Write code **that will keep printing what the user inputs over and over until the user enters the string "quit".**

    .. activecode:: ps_5_1

        # Write code here

        ====

        print "\n---\n\n"
        print "There are no tests for this problem"



.. question:: problem_set_5_2

    We've given you another data file in this problem. It's called ``timely_file.txt``. Write code to figure out which is the most common word in the file. Save the string that is most common word in the file in the variable ``abc``. (Hint: there was a problem on last week's problem set that is very similar to this one.)

    .. activecode:: ps_5_2
       :available_files: timely_file.txt

       # Write code here!
        
       =====

       from unittest.gui import TestCaseGui

       class myTests(TestCaseGui):

          def testOne(self):
             self.assertEqual(abc, 'the', "testing whether abc is set correctly.")

       myTests().main()


.. question:: problem_set_5_3

    Below is a function definition. **DO NOT** change it! 

    We have also provided some invocations of that function. Run those and see what they do.

    Below the comment provided in the code window, write a few calls to this function yourself, with whatever appropriate input you want.

    Finally, write a few sentences in comments in the code window that explain what's happening in this function called list_end_with_string. You should explain what happens if a list like l gets input into this function AND what happens if a list like b gets input into it. 

    Don't forget to run it and save!

    .. activecode:: ps_5_7

       # Functiond efinition
       def list_end_with_string(new_list):
           if type(new_list[-1]) == type("hello"):
               return new_list
           new_list.append("the last element is a string no matter what now!")
           return new_list

       # Some function calls and lines that print out the results
       l = [3,46,6]
       b = [4,"hi",10,"12",12,123,"whoa!"]
       print list_end_with_string([1,2])
       print list_end_with_string(l)
       print list_end_with_string(b)

       # Now write a couple invocations of this function yourself below this line.


       # Write your comments here.

.. question:: problem_set_5_4

    Define a function ``is_prefix`` that takes two strings as inputs and returns the boolean value ``True`` if the first string is a prefix of the second string, but returns ``False`` otherwise.

    .. activecode:: ps_5_4

          # Define your function here.


          # Here's a couple example function calls, printing the return value
          # to show you what it is.
          print is_prefix("He","Hello") # should print True
          print is_prefix("Hello","He") # should print False
          print is_prefix("Hi","Hello") # should print False
          print is_prefix("lo","Hello") # should print False
          print is_prefix("Hel","Hello") # should print True
          # Remember, these won't work at all until you have defined a function called is_prefix

          =====

          from unittest.gui import TestCaseGui

          class myTests(TestCaseGui):

             def testOne(self):
                self.assertEqual(is_prefix("Big", "Bigger"), True, "Testing whether 'Big' is a prefix of 'Bigger'")
                self.assertEqual(is_prefix("Bigger", "Big"), False, "Testing whether 'Bigger' is a prefix of 'Big'")
                self.assertEqual(is_prefix('ge', 'Bigger'), False, "Testing whether 'ge' is a prefix of 'Bigger'")
                self.assertEqual(is_prefix('Bigge', "Bigger"), True, "Testing whether 'Bigge' is a prefix of 'Bigger'")

          myTests().main()

.. question:: problem_set_5_5

    Define a python function ``grep`` that works just like the unix command ``grep``. Your function should take two inputs, a string and a filename. It should return a list of all the lines in the file that contain the string, and only the lines in the file that contain the string.

    .. activecode:: ps_5_9
       :available_files: timely_file.txt

       # Write code here!

       =====

       from unittest.gui import TestCaseGui

       class myTests(TestCaseGui):

          def testOne(self):
             def solgrep(a, b):
                lines = open(b, 'r').readlines()
                acc = []
                for l in lines:
                   if a in l:
                      acc.append(l)
                return acc
             self.assertEqual(grep('autumn', 'timely_file.txt'), solgrep('autumn', 'timely_file.txt'), "testing whether grep('autumn', 'timely_file.txt') returns the right two lines.")
             self.assertEqual(grep('fool', 'timely_file.txt'), solgrep('fool', 'timely_file.txt'), "Testing whether grep('fool', 'timely_file.txt') correctly returns an empty list.")
             
       myTests().main()

.. question:: problem_set_5_6

    Write code that repeatedly asks the user to input numbers. Keep going until the sum of the numbers is 21 or more. Print out the total.

    .. activecode:: ps_5_6

        # Write your code here!


        ====
        
        print "\n---\n\n" 
        print "There are no tests for this problem."
