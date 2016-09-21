:orphan:

..  Copyright (C) Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Lecture 2 Exercises
===================

.. activecode:: lec2_1

   Write code to divide the integer value ``3`` by the integer value ``7``, and save the resulting value in the variable ``y``. Then write code to divide the floating point value ``3.0`` by the integer value ``7``, and save the resulting value in the variable ``b``. (**Consider,** before you write the code or print out the values: what type of value will be stored in the variable ``y``? What type of value will be stored in the variable ``b``?)
   ~~~~

   =====
   
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
          self.assertEqual(y, 0, "Testing the value of the variable y.")
          self.assertEqual(b, 3.0/7, "Testing the value of the variable b.")

   myTests().main()


.. activecode:: lec2_2

   Write code to let the user input their name. Store the string in a variable. Then write code to print out ``Welcome to the world of programming, <USER'S NAME>`` (except instead of "<USER'S NAME>" should be the name the user typed).
   ~~~~
   # Write your code here.

   =====
   print "\n We can't test code that requires user input in this case.\n"

.. activecode:: lec2_3

   Below is some code that assigns values to variables. Write code below it that makes it so that the variable ``x`` holds an integer value that is greater by 2 than the integer value it currently holds. That code should work no matter what the current value of ``x`` is! Then, write code that makes the variable ``apple`` hold the string value ``"television"``. Do not change any of the existing code.
   ~~~~
   y = 5
   apple = 7
   x = 3
   pasta = "delicious"


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(x,5,"Testing value of x.")
         self.assertEqual(apple,"television", "Testing value of apple.")
         self.assertNotIn("x = 5", self.getEditorText(), "Testing to make sure there is no hard-coding to reassign the variable x. (Don't worry about actual and expected values.)")

   myTests().main()
