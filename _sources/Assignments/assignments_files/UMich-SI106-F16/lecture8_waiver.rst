
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

Lecture 8: Waiver Challenge Exercises
=====================================

.. _lecture_8_waiver:


.. activecode:: ee_ch13_051
   :tags: DictionaryAccumulation/AccumulatingtheBestKey.rst, DictionaryAccumulation/AccumulatingaMaximumValue.rst
   :autograde: unittest

   Create a dictionary that contains all the letters in ``quote`` and the number of times they occur. Then, find the letter in the string ``quote`` that occurs the LEAST often. Save this letter to the variable name ``unpop``. 
   ~~~~
   quote = "bananas and berries, ribs, series"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(unpop, 'd', "Testing that upop was assigned to the correct letter.")

   myTests().main()

.. activecode:: ee_ch13_06
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst
   :autograde: unittest

   Given the string ``str1``, make a dictionary assigned to the variable ``char_dict`` with each letter in ``str1`` as a key and the letter's frequency as its value. Make sure that capitalization does not matter, i.e. "G" and "g" should count as the same letter.
   ~~~~
   str1 = "SupercaliFragilisticExpialiDocious"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testSixA(self):
         self.assertEqual(char_dict['s'], 3, "Testing that s has correct value.")
      def testSixB(self):
         self.assertEqual(char_dict['f'], 1, "Testing that f has correct value.")
      def testSixC(self):
         self.assertEqual(char_dict['e'], 2, "Testing that e has correct value.")
      def testSixD(self):
         self.assertEqual(char_dict['d'], 1, "Testing that d has correct value.")

   myTests().main()

.. activecode:: ee_ch13_041
   :tags: DictionaryAccumulation/AccumulatingtheBestKey.rst, DictionaryAccumulation/AccumulatingaMaximumValue.rst
   :autograde: unittest

   Provided is a string saved to the variable ``str1``. Using string methods and dictionary accumulation, find the word that occurs most often. Save the word to the variable name ``most_pop_word``. 
   ~~~~
   str1 = "There are many many seasons and I often cannot decide which is my favorite. In the fall, there are many leaves falling and I really enjoy leaping in them. In the winter, there are many snowflakes that fall everywhere. I love both seasons!"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(most_pop_word, 'many', "Testing that most_pop_word was assigned to the correct word.")

   myTests().main()


.. activecode:: ee_ch13_012
   :tags: DictionaryAccumulation/AccumulatingResultsFromaDictionary.rst
   :autograde: unittest

   ``schedule`` is a dictionary where a class name is a key and its value is how many credits it was worth. Go through and accumulate the total number of credits that have been recorded so far in *SI classes* only, and assign that to the variable ``si_credits``, using dictionary mechanics and the accumulation pattern. Do not hard-code!
   ~~~~
   schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4, "SI 764": 3}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(si_credits, 15, "Testing that si_credits has the correct value.")

   myTests().main()