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


Activities through 2/15
=======================

You have the following graded activities:

1. Class prep. Don't forget: always access the textbook by clicking on the Textbook link from cTools, so that you'll be logged in and get credit for doing the prep.
   
   * Before Monday's class: 

   
   * Before Wednesday's class:
       * Read :ref:`While loops<while_chap>`, and do the exercises in that chapter
       * Read :ref:`Installing a Native Python Interpreter and Text Editor <next_steps>` and follow the instructions to set up for running python on your computer
       
 
#. Reading responses

   * By Tuesday midnight: 

#. Problem set **Due:** **Sunday, February 15 at 5 pm**

   * Do the :ref:`Native Python Interpreter and Text Editor part of Problem Set 5. <unix_pset5>`
      
   * Save answers to the exercises in Problem Set 5: :ref:`Problem Set 5 <problem_set_5>` 




.. _unix_pset5:

Native Python Interpreter and Text Editor
-----------------------------------------

Turn these in as screenshots via CTools in the Assignments tab!

#. Make a new file in your text editor, and save it as ``new_program.py``. (This is a Python program!)

#. In your ``new_program.py`` file, write the following code (copy it from here).

.. activecode:: example_code_ps6

   def cool_machine(x):
   	y = x**2 +7
   	print y

   z = 65.3
   print z + cool_machine(8)

Then, run the Python program in your native Python interpreter. You should get an error. Take a screenshot of this and upload it to CTools.

In a text editor, make edits to this code so it will work (the only output should be 136.3), saving it with a different name (``fixed_program.py``). Take a screenshot of the text editor with the correct coce, and upload it to CTools.


.. _problem_set_5:

Problem Set
-----------

.. datafile:: timely_file.txt
	:hide:

	Autumn is interchangeably known as fall in the US and Canada, and is one of the four temperate seasons. Autumn marks the transition from summer into winter.
	Some cultures regard the autumn equinox as mid autumn while others, with a longer temperature lag, treat it as the start of autumn then. 
	In North America, autumn starts with the September equinox, while it ends with the winter solstice. 
	(Wikipedia)




4. Write code **that will keep printing what the user inputs over and over until the user enters the string "quit".**

.. activecode:: ps_5_4

   # Write code here

   ====
   print "\n---\n\n"
   print "There are no tests for this problem"



8. Given the string in the code below, write code to figure out what the most common word in the string is and assign that to the variable ``abc``. (Do not hard-code the right answer.) Hint: dictionaries will be useful here.

.. activecode:: ps_5_8

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


9. We've given you another data file in this problem. It's called ``timely_file.txt``. Write code to figure out which is the most common word in the file. Again, save it in the variable ``abc``.

.. activecode:: ps_5_9
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
