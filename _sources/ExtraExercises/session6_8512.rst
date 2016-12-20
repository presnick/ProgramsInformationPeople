Lecture 6 Exercises
===================

These are not graded for correctness, but if you did not complete the Lecture Waiver with 100% before today's lecture, you should either try at least one of them, or do work on these on paper and hand them to an instructor after lecture! 

.. activecode:: lec6_1
   :tags:Selection/ConditionalExecutionBinarySelection.rst

   Write code to assign the string ``"You can apply to SI!"`` to ``output`` *if* the string ``"SI 106"`` is in the list ``courses``. If it is not in ``courses``, assign the value ``"Take SI 106!"`` to the variable ``output``.
   ~~~~
   courses = ["ENGR 101", "SI 110", "ENG 125", "SI 106", "CHEM 130"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(output, "You can apply to SI!", "Testing that output has the correct value, given the courses list provided")

   myTests().main()


.. activecode:: lec6_2
   :tags: Selection/OmittingtheelseClauseUnarySelection.rst

   Create the variable ``z`` whose value is ``30``. Write code to see if ``z`` is greater than ``y``. If so, add 5 to ``y``'s value, otherwise do nothing. Then, multiply ``z`` and ``y``, and assign the resulting value to the variable ``x``.
   ~~~~
   y = 22

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(x, 810, "Testing the value of x")
      def testTwo(self):
         self.assertEqual(z, 30, "Testing that z has correctly been defined.")

   myTests().main()


.. activecode:: lec6_3
   :tags: Selection/Nestedconditionals.rst

   **Challenge** In XYZ University, upper level math classes are numbered 300 and up. Upper level English classes are numbered 200 and up. Upper level Psychology classes are 400 and up. Create two lists, ``upper`` and ``lower``. Then write code that uses iteration and conditional statements to assign each course in ``classes`` to the correct list, ``upper`` or ``lower``. HINT: remember, you can convert some strings to different types!
   ~~~~
   classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testEightA(self):
         self.assertEqual(upper, ['PSYCH 412', 'MATH 300', 'MATH 404', 'ENG 201', 'PSYCH 508', 'ENG 220'], "Testing that the upper list exists and contains the correct elements.")
      def testEightB(self):
         self.assertEqual(lower, ['MATH 150', 'PSYCH 111', 'PSYCH 313', 'MATH 206', 'ENG 100', 'ENG 103', 'ENG 125', 'ENG 124'], "Testing that the lower list exists and contains the correct elements.")
      

   myTests().main()