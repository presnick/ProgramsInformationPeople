Lecture 9 Exercises
===================


.. activecode:: lec9_1
   :tags: Functions/Returningavaluefromafunction.rst, Functions/FunctionDefinitions.rst

   Write a function called ``int_return`` that takes an integer as input and returns the same integer.
   ~~~~
   #Define your function here

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(int_return(10), 10, "Testing that function int_return(10) returns 10")

   myTests().main()



.. activecode:: lec9_2
   :tags: Functions/Returningavaluefromafunction.rst

   Write a function called ``add`` that takes any number as its input and returns that sum with 2 added. 
   ~~~~
   # Define your function here.
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwo(self):
         self.assertEqual(add(-2), 0, "Testing that add(-2) returns 0")
         self.assertEqual(add(6), 8, "Testing that add(6) returns 8")
         self.assertEqual(add(4), 6, "Testing that add(4) returns 6")

   myTests().main()


.. activecode:: lec9_3
   :tags: Functions/Returningavaluefromafunction.rst

   Write a function called ``s_change`` that takes one string as input and returns that string, concatenated with the string "for fun.".
   ~~~~
   # Define your function here.

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(s_change("Coding"), "Coding for fun." ,"Testing the function s_change with input coding")
         self.assertEqual(s_change("We go to the beach"), "We go to the beach for fun." , "Testing the function s_change with input We go to the beach")

   myTests().main()