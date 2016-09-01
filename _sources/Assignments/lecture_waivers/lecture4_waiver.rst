
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

Lecture 4: Waiver Challenge Exercises
=====================================

.. _lecture_4_waiver:

.. activecode:: ee_ch10_091
   :language: python

	Create a list of numbers from 0-74 and assign that to the variable ``nums``. Then accumulate the total of that list's values so that the total is assigned to the variable ``total``.
	~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(nums, range(75), "Testing that nums has been created correctly.")

      def testTwo(self):
         self.assertEqual(total, 2775, "Testing that total has the correct value." )

   myTests().main()


.. activecode:: ee_ch10_081
   :language: python

	Count how many characters there are in ``sent`` and assign that number to the variable ``char_sent``. Do not use ``len()``.

	~~~~

   sent = "Oh the places you'll go."
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(char_sent, 23, "Testing that char_sent has the correct value." )
      def testTwo(self):
      	self.assertNotIn("len",self.getEditorText(),"Testing whether the len function is used in your code. (Don't worry about actual and expected values.)")

   myTests().main()


.. activecode:: ee_ch10_071
   :language: python

	For each string in ``wrds``, add 'ed' to the end of the word (to make the word past tense). Instead of saving the words into a new list, overwrite the old list ``wrds``. So at the end of the code execution, ``wrds`` should have the new, past tense words.
	~~~~
   wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(wrds, ["ended", 'worked', "played", "started", "walked", "looked", "opened", "rained", "learned", "cleaned"], "Testing that wrds has been created correctly." )

   myTests().main()