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


Activities through 9/30
=======================

You have the following graded activities:

* **Before Monday's class, 9/26:**

  * Read :ref:`Defining Functions<functions_chap>`, and do the exercises in that chapter

.. usageassignment::
    :subchapters: Functions/FunctionDefinitions,Functions/FunctionInvocation,Functions/FunctionParameters,Functions/Returningavaluefromafunction,Functions/Afunctionthataccumulates,Functions/DecodingaFunction,Functions/MethodInvocations,Functions/Variablesandparametersarelocal,Functions/GlobalVariables,Functions/Functionscancallotherfunctions,Functions/FlowofExecutionSummary,Functions/Printvs.return,Functions/PassingMutableObjects,Functions/SideEffects
    :assignment_name: Prep 06
    :deadline: 2016-09-30 04:00
    :pct_required: 80
    :points: 50

* **Before Tuesday 9/27 at 11:59 pm:**

  * Read Chapter 3 of The Most Human Human and answer `Reading Response 4 <https://umich.instructure.com/courses/108426/assignments/139265>`_ on Canvas.

* **Before Wednesday's class, 9/28:**
  
  * Read :ref:`While loops<while_chap>`, and do the exercises in that chapter


.. usageassignment::
    :subchapters: IndefiniteIteration/intro-indefiniteiteration, IndefiniteIteration/ThewhileStatement, IndefiniteIteration/listenerLoop
    :assignment_name: Prep 07
    :deadline: 2016-09-30 04:00
    :pct_required: 80
    :points: 50


* **Before Friday 9/30 at 6:30 PM:**

  * Save answers to each of the exercises in :ref:`Problem Set 3 <problem_set_3>` and submit your **Demonstrate Your Understanding** assignment to Canvas (linked in the problem set).

  * You have a grace period for the problem set and DYU submission until Sunday 10/2 at 11:59 pm.

This Week's Reading Responses
-----------------------------

.. _reading_response_4:

.. external:: rr_4

  `Reading Response 4 <https://umich.instructure.com/courses/108426/assignments/139265>`_ on Canvas.


Problem Set
-----------
**This problem set is in draft. You may look at it and run code. The problems/instructions may change slightly while this disclaimer remains here.**

.. _problem_set_3:

.. datafile:: timely_file.txt
   :hide:

   Autumn is interchangeably known as fall in the US and Canada, and is one of the four temperate seasons. Autumn marks the transition from summer into winter.
   Some cultures regard the autumn equinox as mid autumn while others, with a longer temperature lag, treat it as the start of autumn then. 
   In North America, autumn starts with the September equinox, while it ends with the winter solstice. 
   (Wikipedia)


.. activecode:: ps_3_1
   :language: python
   :hidecode:

   **1.** Write code **that will keep printing what the user inputs over and over until the user enters the string "quit".**

   ~~~~
   # Write code here

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testCode(self):
         self.assertIn("print", self.getEditorText(), "Testing code. (Don't worry about actual and expected values)")
         self.assertIn("while", self.getEditorText(), "Testing code. (Don't worry about actual and expected values)")
         self.assertIn("raw_input", self.getEditorText(), "Testing code. (Don't worry about actual and expected values)")

   myTests().main()

.. activecode:: ps_3_2
   :available_files: timely_file.txt
   :language: python
   :autograde: unittest
   :hidecode:

   **2.** We've given you another data file in this problem. It's called ``timely_file.txt``. Write code to figure out which is the most common word in the file. Save the string that is most common word in the file in the variable ``abc``. 

   ~~~~
   # Write code here!
        
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testCode(self):
         self.assertNotIn("= 'the'", self.getEditorText(), "Testing code input (Don't worry about actual and expected values)")
         self.assertIn("open",self.getEditorText(),"Testing that you have probably opened the file (Don't worry about actual and expected values)")

      def testOne(self):
         self.assertEqual(abc, 'the', "testing whether abc is set correctly.")

   myTests().main()

.. activecode:: ps_3_3
   :language: python
   :hidecode:

   **3.** Below is a function definition. **DO NOT** change it! 

   We have also provided some invocations of that function. Run those and see what they do.

   Below the comment provided in the code window, write a few calls to this function yourself, with whatever appropriate input you want.

   Finally, write a few sentences in comments in the code window that explain what's happening in this function called list_end_with_string. You should explain what happens if a list like ``l`` gets input into this function AND what happens if a list like ``b`` gets input into it. 

   Don't forget to run it and save!

   ~~~~
   # Function definition
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

.. activecode:: ps_3_4
   :language: python
   :hidecode:

   **4.** Take a look at the code below. The function ``subtract_five`` is supposed to take one integer as input and return that integer minus 5. You'll get an error if you run it as is. Change the function so it works and passes the test!
   ~~~~
   def subtract_five(inp):
       print inp - 5
       return None

   y = subtract_five(9) - 6

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(y, -2, "Testing if y is -2")

   myTests().main()


.. activecode:: ps_3_5
   :language: python
   :hidecode:
   :autograde: unittest

   **5.** Define a function called ``change_amounts`` that takes one integer as input. If the input is larger than 10, it should return the input + 5. If the input is smaller than or equal to 10, it should return the input + 2.
   ~~~~ 
   # We've started you off with the first line...
   def change_amounts(num_here):
       pass # delete this line and put in your own code for the body of the function.

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(change_amounts(9), 11, "Testing if change_amounts(9) equals 11")
         self.assertEqual(change_amounts(12), 17, "Testing if change_amounts(12) equals 17")

   myTests().main()


.. activecode:: ps_3_6
   :language: python
   :autograde: unittest
   :hidecode:

   **6.** Define a function ``is_prefix`` that takes two strings as inputs and returns the boolean value ``True`` if the first string is a prefix of the second string, but returns the boolean value ``False`` otherwise.

   ~~~~   
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

.. activecode:: ps_3_7
   :language: python
   :hidecode:

   **7.** Write code that repeatedly asks the user to input numbers. Keep going until the sum of the numbers is 21 or more. Print out the total.
   ~~~~
   # Write your code here!


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testCode(self):
         self.assertIn("print", self.getEditorText(), "Testing code. (Don't worry about actual and expected values)")
         self.assertIn("while", self.getEditorText(), "Testing code. (Don't worry about actual and expected values)")
         self.assertIn("+", self.getEditorText(), "Testing code. (Don't worry about actual and expected values)")
         self.assertIn("raw_input", self.getEditorText(), "Testing code. (Don't worry about actual and expected values)")

   myTests().main()


.. external:: ps3_dyu

   Submit your `Demonstrate Your Understanding <https://umich.instructure.com/courses/105657/assignments/131286>`_ for this week on Canvas.