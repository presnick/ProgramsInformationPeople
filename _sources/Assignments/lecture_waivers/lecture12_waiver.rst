
:orphan:

..  Copyright (C) Paul Resnick, Jackie Cohen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. highlight:: python
    :linenothreshold: 500

Lecture 12: Challenge Exercises
===============================

.. _lecture_12_waiver:

.. activecode:: ee_Opt_Params_04
   :tags: OptionalAndKeywordParameters/OptionalParameters.rst
   :autograde: unittest

   Write a function called ``math`` that takes in three parameters: an integer, a second integer, and an *optional* string with the default value "add". If the string value is "add", the function should add the two integers. If the string value is "subtract", subtract the second integer from the first integer. If the value is "multiply", multiply the integers and if the value is "divide", divide the first integer by the second integer. Return the result of whatever mathematical operation occurs.
   ~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(math(1,2), 3, "Testing that math(1,2) returns 3")
         self.assertEqual(math(12,2, "divide"), 6, "Testing that math(12,2, 'divide') returns 6")
         self.assertEqual(math(0, 2, "multiply"), 0, "Testing that math(0, 2, 'multiply') returns 0")
         self.assertEqual(math(0, 7, "subtract"), -7, "Testing that math(0, 7, 'subtract') returns -7")

   myTests().main()


.. activecode:: ee_optparams_041
   :tags: OptionalAndKeywordParameters/OptionalParameters.rst
   :autograde: unittest

   Define a function called ``connect`` that takes two inputs. The first, a required parameter, should be a list of strings. The second, an optional parameter named ``connector``, should have a default value of "_" but can take any string as input. The function should return one long string that contains all the original strings concatenated together, joined by the connector string.
   ~~~~
   def connect():

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(connect(["hi", "bye", "yo"]), "hi_bye_yo", "Testing the function connect on input ['hi', 'bye', 'yo'].")
         self.assertEqual(connect(["a", "b", "c"], connector = "--"), "a--b--c", "Testing the function connect on inputs ['a', 'b', 'c'], connector = '--'.")
         self.assertEqual(connect(["x", "y", "z"], connector = "1234"), "x1234y1234z", "Testing the function connect on inputs ['x', 'y', 'z'], connector = '1234'.")
         self.assertEqual(connect([]), '', "Testing the function connect on input [].")
         self.assertEqual(connect(["solo"]), "solo", "Testing the function connect on input ['solo'].")

   myTests().main() 


.. activecode:: ee_Opt_Params_05
   :tags: OptionalAndKeywordParameters/KeywordParameters.rst
   :autograde: unittest

   Provided below is a function, ``test``. Correctly call the function in the ways indicated by the comments below. 
   ~~~~
   def test(int1, dict1, boolean = True):
       if boolean == True:
           for x in dict1:
               if int1 in dict1:
                   return True
               else:
                   return False
       else:
           return "Bool is false"

   #Call the function with the correct parameters so that the function returns "Bool is false". Save the output to a variable called output.



   #Call the function with the correct parameters so that the function returns False. Save the output to a variable called output2. 


   #Now, call the function with parameters such that output will be True. Save the output to a variable called output3. 


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(output, "Bool is false", "Testing that output is assigned to correct value.")
      def testTwo(self):
         self.assertEqual(output2, False, "Testing that output is assigned to correct value.")
      def testThree(self):
         self.assertEqual(output3, True, "Testing that output is assigned to correct value.")

   myTests().main()


.. activecode:: ee_optparams_051
   :tags: OptionalAndKeywordParameters/KeywordParameters.rst
   :autograde: unittest

   We've provided the function ``nums`` below. You must pass the correct inputs into the function so that it returns the values listed in the ActiveCode window. **Note:** You should only pass positive integers into the function (i.e. If asked to produce a negative output, do so by using the ``switch`` argument!)
   ~~~~
   def nums(int1, mult_int=5, switch=False):
       if switch == False: 
           return int1 * mult_int
       if switch == True: 
           return (int1 * mult_int) * -1

   # Below, make the function return the value 10, and save it to the variable name output1


   # Below, make the function return the value -12, and save it to the variable name output2


   # Below, make the function return the value -25, and save it to the variable name output3


   # Below, make the function return the value -5, and save it to the variable name output4


   # Below, make the function return the value 56, and save it to the variable name output5


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(output1, 10, "Testing that output1 was assigned correctly.")
      def testTwo(self):
         self.assertEqual(output2, -12, "Testing that output2 was assigned correctly.")
      def testThree(self):
         self.assertEqual(output3, -25, "Testing that output3 was assigned correctly.")
      def testFour(self):
         self.assertEqual(output4, -5, "Testing that output4 was assigned correctly.")
      def testFive(self):
         self.assertEqual(output5, 56, "Testing that output5 was assigned correctly.")

   myTests().main()
