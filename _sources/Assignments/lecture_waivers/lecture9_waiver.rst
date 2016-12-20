
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

Lecture 9: Waiver Challenge Exercises
=====================================

.. _lecture_9_waiver:

.. activecode:: ee_functions_061
   :tags: Functions/Returningavaluefromafunction.rst, Functions/Functionscancallotherfunctions.rst
   :autograde: unittest

   This problem will require you to write two functions. The first function, named ``func1``, should take a number as input, and return that number multiplied by 3. The second function, named ``func2``, should take a number as input, multiply it by 3, and then add 10. You should call on ``func1`` within ``func2`` to accomplish this.
   ~~~~
   def func1():


   def func2():

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(func1(10), 30, "Testing func1 on input 10.")
         self.assertEqual(func1(0), 0, "Testing func1 on input 0.")
         self.assertEqual(func2(-2), 4, "Testing func2 on input -2.")
         self.assertEqual(func2(0), 10, "Testing func2 on input 0.")

   myTests().main()
 

.. activecode:: ee_Function_07
   :tags: Functions/Afunctionthataccumulates.rst, Functions/Returningavaluefromafunction.rst
   :autograde: unittest

   Write a function called ``dict_test`` that takes in 2 parameters: a dictionary whose keys are strings and values are integers, and a character. The function should go through the dictionary and see if the inputted character is in each key of the dictionary. It should total the values of all keys which include that character, and return that sum.
   ~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testSeven(self):

         self.assertEqual(dict_test({'swimming':10, 'running':15, 'walking':5, 'jogging':10}, 'w'), 15, "Testing that dict_test({'swimming':10, 'running':15, 'walking':5, 'jogging':10}, 'w') returns 15")

         self.assertEqual(dict_test({}, "x"), 0, "Testing that dict_test({}, 'x') returns 0")

         self.assertEqual(dict_test({'cat':4, 'dog':4,'chicken':2, 'snake':0, 'horse':4}, 'g'), 4, "Testing that dict_test({'cat':4, 'dog':4,'chicken':2, 'snake':0, 'horse':4}, 'g') returns 4")


   myTests().main()


.. activecode:: ee_functions_072
   :tags: Functions/Returningavaluefromafunction.rst
   :autograde: unittest

   Write a function called ``work`` that takes 3 inputs: an integer, a string, and a list, in that order. Your function should check to see if the string input is in the list input, and if it is, then return the string multiplied by the first parameter. If the string is not in the list, then your function ``work`` should return the string plus the phrase ``"is not in the list"``. (For example, if your second parameter was ``"whelp"`` and was not in the list, then the string ``"whelp is not in the list"`` should be returned.)
   ~~~~ 

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(work(2,"why",["hello", 3, 3.4, 'why', 'velma']), "whywhy", "Testing the function work with inputs 2, 'why', ['hello', 3, 3.4, 'why', 'velma']")

         self.assertEqual(work(8, 'how', [3, "02", "however", "scooby", "snacks", ['hose']]), "how is not in the list", "Testing the function work with inputs 8, 'how', [3, '02', 'however', 'scooby', 'snacks', ['hose']]")

         self.assertEqual(work(4, '4', [3, 4, '5', 'UofM', '4']), "4444", "Testing the function word with inputs 4, '4', [3, 4, '5', 'UofM', '4']")

   myTests().main()
   

.. activecode:: ee_functions_08
   :tags: Functions/Returningavaluefromafunction.rst
   :autograde: unittest

   Write a function named ``add_all`` that takes two parameters. The first parameter should be a list of numbers, and the second should be an integer. The function should return a new list whose elements are all the numbers from the old list with the integer added to them (For example: Given the inputs [1, 2, 3], 1, the function should return [2, 3, 4]).
   ~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(add_all([1, 2, 3], 0), [1, 2, 3], "Testing add_all on inputs [1, 2, 3], 0.")
         self.assertEqual(add_all([], 10), [], "Testing add_all on inputs [], 10.")
         self.assertEqual(add_all([5], 7), [12], "Testing add_all on inputs [5], 7.")

   myTests().main() 



