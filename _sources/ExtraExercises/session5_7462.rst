
Lecture 5 Exercises
===================

.. activecode:: lec5_1

   For each character in the string already saved in the variable ``str1``, append each character to a list called ``chars``. 
   ~~~~

   str1 = "I love python"
   # HINT: what's the accumulator? That should go here.
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwo(self):
         self.assertEqual(chars, ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n'], "Testing that chars has the correct value.")

   myTests().main()

.. activecode:: lec5_2

   Iterate over the list ``lm`` (which contains only strings) and print out the first character of each string in the list! 
   ~~~~

   lm = ["a","dreamer","a","wisher","a","liar"]
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testone(self):
         self.assertIn("a\nd\na\nw\na\nl",self.getOutput(),"Testing printed output. (Don't worry about actual and expected values.)")

   myTests().main()

