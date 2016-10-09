Lecture 10 Exercises
==================== 

.. activecode:: ee_07_01
   :tags: IndefiniteIteration/ThewhileStatement.rst

   Using a while loop, create a list ``numbers`` that contains the numbers 0 through 35. Your while loop should initialize a counter variable to 0. On each iteration, the loop should append the current value of the counter to the list and the counter should increase by 1. The while loop should stop when the counter is greater than 35.
   ~~~~
   # Write your code here.

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(numbers, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], "Testing that numbers is assigned to correct values")

   myTests().main()

.. activecode:: lec10_2

	Write code that uses a while loop to accept input from a user repeatedly, until the user inputs the string ``"stop"``.

	(We cannot write tests for this because it requires user input, so you'll just have to gauge whether it works correctly yourself!)
	~~~~
	# Write code here.

	
