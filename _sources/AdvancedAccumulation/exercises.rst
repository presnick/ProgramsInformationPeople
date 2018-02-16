..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Exercises
---------


Write equivalent code using map instead of the manual accumulation below

.. activecode:: map_exercise_1
   :language: python
   :autograde: unittest
   :topics: AdvancedAccumulation/map

   things = [3, 5, -4, 7]
   
   accum = []
   for thing in things:
       accum.append(thing+1)
   print(accum)

Use manual accumulation to define the lengths function below.
 
.. activecode:: map_exercise_2
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Iteration/TheAccumulatorPatternwithLists

   def lengths(strings):
       """lengths takes a list of strings as input and returns a list of numbers that are the lengths
       of strings in the input list. Use manual accumulation!"""
       # fill in this function's definition to make the test pass.
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(lengths(["Hello", "hi", "bye"]), [5, 2, 3], "Testing whether lengths has been correctly defined.")

   myTests().main()
  
Now define lengths using map instead.
 
.. activecode:: map_exercise_3
   :language: python
   :autograde: unittest
   :practice: T
   :topics: AdvancedAccumulation/map

   def lengths(strings):
       """lengths takes a list of strings as input and returns a list of numbers that are the lengths
       of strings in the input list. Use map!"""
       # fill in this function's definition to make the test pass.

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(lengths(["Hello", "hi", "bye"]), [5, 2, 3], "Testing whether lengths has been correctly defined.")

   myTests().main()

Now define lengths using a list comprehension instead.
 
.. activecode:: listcomp_exercise_1
   :language: python
   :autograde: unittest
   :practice: T
   :topics: AdvancedAccumulation/listcomp

   def lengths(strings):
       """lengths takes a list of strings as input and returns a list of numbers that are the lengths
       of strings in the input list. Use a list comprehension!"""
       # fill in this function's definition to make the test pass.
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(lengths(["Hello", "hi", "bye"]), [5, 2, 3], "Testing whether lengths has been correctly defined.")

   myTests().main()
   
   
.. activecode:: filter_exercise_1
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Iteration/TheAccumulatorPatternwithLists

   # Write a function called positives_Acc that receives list of things as the input and returns a list of only the positive things, [3, 5, 7], via manual accumulation.



   things = [3, 5, -4, 7]
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         things = [3, 5, -4, 7]
         self.assertEqual(positives_Acc(things), [3, 5, 7], "Testing whether positives_Acc has been correctly defined.")

   myTests().main()


.. activecode:: filter_exercise_2
   :language: python
   :autograde: unittest
   :practice: T
   :topics: AdvancedAccumulation/filter

   # Write a function called positives_Fil that receives list of things as the input and returns a list of only the positive things, [3, 5, 7], using the filter function.



   things = [3, 5, -4, 7]
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         things = [3, 5, -4, 7]
         self.assertEqual(positives_Fil(things), [3, 5, 7], "Testing whether positives_Fil has been correctly defined.")

   myTests().main()


.. activecode:: filter_exercise_2a
   :language: python
   :autograde: unittest
   :practice: T
   :topics: AdvancedAccumulation/listcomp

   # Write a function called positives_Li_Com that receives list of things as the input and returns a list of only the positive things, [3, 5, 7], using the list comprehension.



   things = [3, 5, -4, 7]
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         things = [3, 5, -4, 7]
         self.assertEqual(positives_Li_Com(things), [3, 5, 7], "Testing whether positives_Li_Com has been correctly defined.")

   myTests().main()


# define longwords using manual accumulation

.. activecode:: filter_exercise_3
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Iteration/TheAccumulatorPatternwithLists

   def longwords(strings):
       """Return a shorter list of strings containing only the strings with more than four characters. Use manual accumulation."""
       # write your code here

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(longwords(["Hello", "hi", "bye", "wonderful"]), ["Hello", "wonderful"], "Testing whether longwords has been correctly defined.")

   myTests().main()

# define longwords using filter
   
.. activecode:: filter_exercise_4
   :language: python
   :autograde: unittest
   :practice: T
   :topics: AdvancedAccumulation/filter

   def longwords_Fil(strings):
       """Return a shorter list of strings containing only the strings with more than four characters. Use the filter function."""
       # write your code here

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(longwords_Fil(["Hello", "hi", "bye", "wonderful"]), ["Hello", "wonderful"], "Testing whether longwords_Fil has been correctly defined.")

   myTests().main()

# define longwords using a list comprehension

.. activecode:: listcomp_exercise_2
   :language: python
   :autograde: unittest
   :practice: T
   :topics: AdvancedAccumulation/listcomp

   def longwords_Li_Comp(strings):
       """Return a shorter list of strings containing only the strings with more than four characters. Use a list comprehension."""
       # write your code here
              
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(longwords_Li_Comp(["Hello", "hi", "bye", "wonderful"]), ["Hello", "wonderful"], "Testing whether longwords_Li_Comp has been correctly defined.")

   myTests().main()


.. activecode:: listcomp_exercise_3
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: AdvancedAccumulation/listcomp

   Write a function called `longlengths` that returns the lengths of those strings that have at least 4 characters. Try it with a list comprehension.
   ~~~~
   def longlengths(strings):
       return None

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(longlengths(["Hello", "hi", "bye", "wonderful"]), [5, 9], "Testing whether longlengths has been correctly defined.")

   myTests().main()


.. activecode:: listcomp_exercise_4
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: AdvancedAccumulation/filter

   Write a function called `longlengths` that returns the lengths of those strings that have at least 4 characters. Try it using map and filter.
   ~~~~

   def longlengths(strings):
       return None
       
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(longlengths(["Hello", "hi", "bye", "wonderful"]), [5, 9], "Testing whether longlengths has been correctly defined.")

   myTests().main()


.. activecode:: reduce_exercise_2
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Iteration/TheAccumulatorPatternwithLists

   Write a function that takes a list of numbers and returns the sum of the squares of all the numbers. Try it using an accumulator pattern.
   ~~~~

   def sumSquares(L):
       return None
   
   nums = [3, 2, 2, -1, 1]
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sumSquares(nums), 19, "Testing whether sumSquares has been correctly defined.")

   myTests().main()


.. activecode:: reduce_exercise_3
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: AdvancedAccumulation/map

   Write a function that takes a list of numbers and returns the sum of the squares of all the numbers. Try it using map and sum.
   ~~~~

   def sumSquares(L):
       return None
   
   nums = [3, 2, 2, -1, 1]
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sumSquares(nums), 19, "Testing whether sumSquares has been correctly defined.")

   myTests().main()


.. activecode:: reduce_exercise_4
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :topics: AdvancedAccumulation/reduce

   Write a function that takes a list of numbers and returns the sum of the squares of all the numbers. Try it using reduce.
   ~~~~

   def sumSquares(L):
       return None
   
   nums = [3, 2, 2, -1, 1]
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sumSquares(nums), 19, "Testing whether sumSquares has been correctly defined.")

   myTests().main()


.. activecode:: zip_exercise_1
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: AdvancedAccumulation/zip

   Use the zip function to take the lists below and turn them into a list of tuples, with all the first items in the first tuple, etc.
   ~~~~

   L1 = [1, 2, 3, 4]
   L2 = [4, 3, 2, 3]
   L3 = [0, 5, 0, 5]
   
   tups = []
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(tups, [(1, 4, 0), (2, 3, 5), (3, 2, 0), (4, 3, 5)], "Testing whether tups has been correctly defined.")

   myTests().main()


.. activecode:: zip_exercise_2
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: AdvancedAccumulation/zip

   Use zip and map or a list comprehension to make a list consisting the maximum value for each position. For L1, L2, and L3, you would end up with a list [4, 5, 3, 5].

   ~~~~

   L1 = [1, 2, 3, 4]
   L2 = [4, 3, 2, 3]
   L3 = [0, 5, 0, 5]
   
   maxs = []
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(maxs, [4, 5, 3, 5], "Testing whether maxs has been correctly defined.")

   myTests().main()

