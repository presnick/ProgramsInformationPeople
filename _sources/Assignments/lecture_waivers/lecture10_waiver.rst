
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

Lecture 10: Waiver Challenge Exercises
======================================

.. _lecture_10_waiver:


.. activecode:: ee_ch07_052
   :tags: IndefiniteIteration/ThewhileStatement.rst
   :autograde: unittest

   Here is a for loop that works. Underneath, rewrite the problem so that it is done using a while loop, but save the accumulated total to the variable ``total``.
   ~~~~
   L = [3,9,29,8,48,5,3,8,6,1,2]
   accum = 0
   for elem in L:
       accum += elem

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(total, 122 , "Testing that total has the correct value")

   myTests().main()

.. activecode:: ee_ch07_06
   :tags: IndefiniteIteration/listenerLoop.rst
   :autograde: unittest

   Create a function called ``first_five`` that takes in a list of numbers. In this function, create a sublist of the inputted list by using a while loop that stops when it reaches the number 0. The function should only return a list of the first five numbers of the sublist, regardless of where the while loop stops. i.e. invoking the function with input ``[1, 1, 2, 3, 4, 3, 2]`` should return ``[1, 1, 2, 3, 4]``. But invoking the function with the input ``[1,5,0,2,3,4,6]`` should return ``[1,5]``. (For a challenge, do this without using slicing. You may use slicing to solve this problem, though.)
   ~~~~
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testSix(self):
         self.assertEqual(first_five([1, 2, 0]), [1,2], "Testing that first_five([1, 2, 0]) returns [1,2]")
         self.assertEqual(first_five([1, 2, 3, 4, 3, 2, 5, 0, 3, 4]), [1, 2, 3, 4, 3], "Testing that first_five([1, 2, 3, 4, 3, 2, 5, 0, 3, 4]) returns [1, 2, 3, 4, 3]")
         self.assertEqual(first_five([0]), [], "Testing that first_five([0]) returns []")

   myTests().main()


.. activecode:: ee_ch07_042
   :tags: IndefiniteIteration/listenerLoop.rst
   :autograde: unittest

   Write a function called ``check_letts`` that takes a list as its parameter, and contains a while loop that only stops once it reaches an element of the list that is the string ``'no'``. It should return a list of all of the strings up until it reaches 'no'.
   ~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(check_letts(['hey', 'now', 'you', 'are', 'a', 'rockstar', 'no', 'get', 'your', 'game', 'on']), ['hey', 'now', 'you', 'are', 'a', 'rockstar'], "Testing that check_letts stops on the correct position with input ['hey', 'now', 'you', 'are', 'a', 'rockstar', 'no', 'get', 'your', 'game', 'on']")
         self.assertEqual(check_letts(['never gonna give you up no', 'never', 'gonna', 'let', 'you', 'no']), ['never gonna give you up no', 'never', 'gonna', 'let', 'you'], "Testing that check_letts stops on the correct position with input ['never gonna give you up no', 'never', 'gonna', 'let', 'you', 'no']")
         self.assertEqual(check_letts(['no', 'aowef', 'wawfefj', 'awofjno', 'a23raf', '23rfad']), [], "Testing that check_letts stops on the correct position with input ['no', 'aowef', 'wawfefj', 'awofjno', 'a23raf', '23rfad']")

   myTests().main()


.. activecode:: ee_ch7_062
   :tags: IndefiniteIteration/listenerLoop.rst
   :autograde: unittest

   Write a function called ``too_big`` that takes a list of numbers as input and produces a new list of numbers as output. Using a while loop, the function should output a list of all of the numbers in the list *up until* the total is 30 or more. So, if the input to this function is ``[10,20,4,6,7,9]``, it should return the list ``[10,20]``. If the input is ``[10,3,5,6,7,9]``, it should return ``[10,3,5,6,7]``. 
   ~~~~
   def too_big(): 
       pass # replace this line with your function body

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(too_big([12, 19, 5, 10, 10, 13, 4, 16]), [12, 19], "Testing the function too_big on the input [12, 19, 5, 10, 10, 13, 4, 16].")
         self.assertEqual(too_big([2, 3, 4, 5, 2, 2, 7, 2, 4, 19, 6, 5, 4, 2, 2]), [2, 3, 4, 5, 2, 2, 7, 2, 4], "Testing the function too_big on the input [2, 3, 4, 5, 2, 2, 7, 2, 4, 19, 6, 5, 4, 2, 2].")

   myTests().main()   
