
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

Lecture 5: Waiver Challenge Exercises
=====================================

Note that iteration is *very important* for the remainder of this course, and if you feel at all concerned about it, we recommend very strongly that you attend lecture! 

.. _lecture_5_waiver:

.. activecode:: l5w_1
   :language: python
   :autograde: unittest

   Create a list of numbers from 0-74 using a Python function, and assign that to the variable ``nums``. Then use the accumulator pattern to accumulate the total of that list's values, so that the total is assigned to the variable ``total``.
   ~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(nums, range(75), "Testing that nums has been created correctly.")

      def testTwo(self):
         self.assertEqual(total, 2775, "Testing that total has the correct value." )

   myTests().main()


.. activecode:: l5w_2
   :language: python
   :autograde: unittest

   Count how many characters there are in ``sent`` and assign that number to the variable ``char_sent``. Do *not* use ``len()``.
   ~~~~
   sent = "Oh the places you'll go."

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(char_sent,len(sent), "Testing that char_sent has the correct value." )
      def testTwo(self):
        self.assertNotIn("len",self.getEditorText(),"Testing whether the len function is used in your code. If you used it to test your answer, you should get rid of it in order to pass this test! (Don't worry about actual and expected values.)")

   myTests().main()


.. activecode:: l5w_3
   :language: python
   :autograde: unittest

   For each string in ``wrds``, add 'ed' to the end of the word (to make the word past tense). Save the past-tense list to a list called ``past_tense``.
   ~~~~
   wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(past_tense, ["ended", 'worked', "played", "started", "walked", "looked", "opened", "rained", "learned", "cleaned"], "Testing that past_tense has been created correctly." )
         self.assertIn("for",self.getEditorText(), "Testing whether for iteration is being used. Don't worry about actual and expected values.")
         self.assertIn("in wrds",self.getEditorText(), "Testing that iteration over the wrds list is occurring. Don't worry about actual and expected values.")

   myTests().main()