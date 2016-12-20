..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Extra Exercises
===============

1. Write code to create a list of integers from 0 through 52 and assign that list to the variable ``numbers``. You should use a special Python function -- do not type out the whole list yourself. HINT: You can do this in one line of code!

.. activecode:: ee_ch10_01
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(numbers, range(53), "Testing that numbers is a list that contains the correct elements.")

   myTests().main()

1.1 Write code to create a list of numbers from 0 to 67 and assign that list to the variable ``nums``. Do not hard code the list.

.. activecode:: ee_ch10_011

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(nums, range(68), "Testing that nums is a list that contains the correct elements.")

   myTests().main()

.. Iteration/TraversalandtheforLoopByIndex.rst, Iteration/TheAccumulatorPatternwithStrings.rst

2. For each character in the string already saved in the variable ``str1``, append each character to a list called ``chars``. 

.. activecode:: ee_ch10_02

   str1 = "I love python"
   # HINT: what's the accumulator? That should go here.
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwo(self):
         self.assertEqual(chars, ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n'], "Testing that chars is assigned to correct values.")

   myTests().main()

2.1 For each character in the string saved in ``ael``, append that character to a list that should be saved in a variable ``app``.

.. activecode:: ee_ch10_022

   ael = "python!"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(app, ['p','y','t','h','o','n', "!"], "Testing that app has the correct elements." )

   myTests().main()

.. Iteration/Stringsandforloops.rst, Iteration/TheAccumulatorPatternwithStrings.rst

3. Assign an empty string to the variable ``output``. Using the ``range`` function, write code to make it so that the variable ``output`` has 35 ``a`` s inside it (like ``"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"``). Hint: use the accumulation pattern!

.. activecode:: ee_ch10_03
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testThree(self):
         self.assertEqual(output, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "Testing that output has the correct value.")

   myTests().main()

3.1 Create an empty string and assign it to the variable ``lett``. Then using range, write code such that when your code is run, lett has 7 b's (``"bbbbbbb"``).

.. activecode:: ee_ch10_031

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(lett, "bbbbbbb", "Testing that lett has the correct value." )

   myTests().main()

.. Iteration/TraversalandtheforLoopByIndex.rst, Iteration/TheAccumulatorPatternwithStrings.rst

4. Given the list of numbers, ``numbs``, create a new list of those same numbers increased by 5. Save this new list to the variable ``newlist``. 

.. activecode:: ee_ch10_04
      
   numbs = [5, 10, 15, 20, 25]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(newlist, [10, 15, 20, 25, 30], "Testing that the newlist value contains the correct elements.")

   myTests().main()

4.1 For each number in ``lst_nums``, multiply that number by 2 and append it to a new list called ``larger_nums``. 

.. activecode:: ee_ch10_041

   lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(larger_nums, [8, 58, 10.6, 20, 4, 3634, 3934, 18, 62.64], "Testing that larger_nums has been created correctly." )

   myTests().main()

5. **Challenge** Now do the same as in problem 4, but do not create a new list. Overwrite the list ``numbs`` so that each of the original numbers are increased by 5.

.. activecode:: ee_ch10_05
      
   numbs = [5, 10, 15, 20, 25]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFive(self):
         self.assertEqual(numbs, [10, 15, 20, 25, 30], "Testing that numbs is assigned to correct values.")

   myTests().main()


6. For each word in the list ``verbs``, add an -ing ending. Save this new list in a new list, ``ing``.

.. activecode:: ee_ch10_06
      
   verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testSix(self):
         self.assertEqual(ing, ['kayaking', 'crying', 'walking', 'eating', 'drinking', 'flying'], "Testing that the variable ing has the correct value.")

   myTests().main()


6.1 **Challenge** Do the same as above, but do not create a new list. Instead, overwrite the old list so that ``verbs`` has the same words with ``ing`` at the end of each one. 

.. activecode:: ee_ch10_07
      
   verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testSeven(self):
         self.assertEqual(verbs, ['kayaking', 'crying', 'walking', 'eating', 'drinking', 'flying'], "Testing that verbs is assigned to correct values.")

   myTests().main()

7. For each string in ``wrds``, add 'ed' to the end of the word (to make the word past tense). Save these past tense words to a list called ``past_wrds``.

.. activecode:: ee_ch10_061

   wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(past_wrds, ["ended", 'worked', "played", "started", "walked", "looked", "opened", "rained", "learned", "cleaned"], "Testing that past_wrds has the correct value." )

   myTests().main()


8. Count the number of characters in string ``str1``. Do not use ``len()``. Save the number in variable ``numbs``.

.. activecode:: ee_ch10_08
      
   str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testEight(self):
         self.assertEqual(numbs, 90, "Testing that numbs is assigned to correct values.")

   myTests().main()

9. Create a list of numbers 0 through 40 and assign this list to the variable ``numbers``. Then, accumulate the total of the list's values and assign that sum to the variable ``sum1``. 

.. activecode:: ee_ch10_09
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testNineA(self):
         self.assertEqual(numbers, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], "Testing that numbers is assigned to correct values.")

      def testNineB(self):
         self.assertEqual(sum1, 820, "Testing that sum1 has the correct value.")

   myTests().main()
