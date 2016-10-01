Lecture 8 Exercises
===================


.. activecode:: lec8_1
   :tags: DictionaryAccumulation/AccumulatingResultsFromaDictionary.rst

   The dictionary ``Junior`` shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of credits taken this semester and assign it to the variable ``credits``. Do not hardcode this -- use dictionary accumulation!
   ~~~~
   courses = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(credits, 18, "Testing that credits is assigned to correct values")

   myTests().main() 

.. activecode:: lec8_2
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst

   Create a dictionary, ``freq``, that displays each letter in string ``str1`` as the key and the number of times it occurs in the string as the value.
   ~~~~
   str1 = "peter piper picked a peck of pickled peppers"
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwo(self):
         self.assertEqual(sorted(freq.items()), sorted([(' ', 7), ('a', 1), ('c', 3), ('d', 2), ('e', 8), ('f', 1), ('i', 3), ('k', 3), ('l', 1), ('o', 1), ('p', 9), ('r', 3), ('s', 1), ('t', 1)]), "Testing that freq is correct.")

   myTests().main()