:orphan:

..  Copyright (C) Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

506: Lecture 3 Exercises
========================

.. activecode:: lec3_1

   Use the accumulator pattern to create a new list, saved in the variable ``e``, which contains the *length* of each string in the list ``str_lst``. For example, if ``str_lst`` contained ``["hi","bye"]``, ``e`` should end up with the value ``[2,3]``.
   ~~~~
   str_lst = ["hello","everyone","don't","you","love","python?"]

   =====
   
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
          self.assertEqual(e, [len(x) for x in str_lst], "Testing the value of the variable e.")

   myTests().main()


.. activecode:: lec3_2

   Write code to print out the last element of the string ``spf``, which should work no matter what the string saved in ``spf`` is. Then write code, using the slicing operation, to print out a list that is the same as the list in ``lst`` but does NOT contain the first two elements in ``lst``.
   ~~~~
   lst = ["hello","everyone","don't","you","love","python?"]
   spf = "supercalifragilisticexpialidocious"

   =====
   
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
          self.assertIn("s", self.getOutput(), "Testing the printed output of your code. Don't worry about actual and expected values.")
          self.assertIn(str(["don't","you","love","python?"]), self.getOutput(), "Testing the printed output of your code. Don't worry about actual and expected values.")

   myTests().main()


.. activecode:: lec3_3

   The following code has a bunch of errors. Try to fix them, so the code will run! As you do so, examine the error messages carefully: why are they happening? Each time you fix an error in a line of code, think about an explanation: what was wrong with it? How did you fix it? (If you're doing this on paper, you can just make notes about what errors there are and how you could fix them. 

   This is an exercise in thought and debugging. (Note that it may be surprising which errors Python gets caught at first -- when you fix one, you'll find another, which is exactly what happens when you make errors by accident!)
   ~~~~
   x = len("hello")
   print x()

   print len()

   b = y

   f = len
   print f("hi")

   print len("sixteen"

   print len - 6
   m = len("seven") + 4
   n = m + " letters!"

   =====
   print "============="
   print "\n No tests; if the code runs without error messages, you've done the right thing!\n"