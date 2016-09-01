
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

Lecture 3: Waiver Challenge Exercises
=====================================

.. _lecture_3_waiver:

.. activecode:: ee_ch9_09

   Get rid of the pet ``"cat"`` from the list ``pets``. Add the pet ``"dog"`` in its place.
   ~~~~
   pets = ["goldfish", "cat", "parrot", "hamster"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testNine(self):
         self.assertEqual(pets[1], "dog", "Testing that dog is in correct location.")
         self.assertEqual(pets, ["goldfish", "dog", "parrot", "hamster"], "Testing that output value is assigned to correct value.")

   myTests().main()


.. activecode:: ee_ch_091
   :tags: Sequences/ListDeletion.rst, Sequences/ListMethods.rst

   Get rid of the fourth element in the list ``office``. Then, replace that element with the string "chair".
   ~~~~
   office = ["table", "computer", "clock", "smoothie machine", "water cooler", "fax machine", "printers", "pencils", "desks"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(office[3], "chair", "Testing the fourth element of office.") 
         self.assertEqual(office, ["table", "computer", "clock", "chair", "water cooler", "fax machine", "printers", "pencils", "desks"], "Testing the contents of office.")

   myTests().main()  

.. activecode:: ee_ch9_10

   Create a list made up of the 5th and 37th element from the list ``words`` and assign it to the variable ``output``. As always, do not hard code!
   ~~~~
   words = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTen(self):
         self.assertEqual(output, ["caterpillar", "hotdog"], "Testing that output value is assigned to correct value.")

   myTests().main()

.. activecode:: ee_ch9_101
   :tags: Sequences/ConcatenationandRepetition.rst, Sequences/AccessingElements.rst

   Create a list made up of the 11th and 29th elements from the list ``practice`` and assign that to the variable ``content``.
   ~~~~
   practice = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(content, ["wolverine", ["women", "olympics", "gold", "rio", 21, "2016", "men"]], "Testing that content has the correct elements assigned.")

   myTests().main()


.. activecode:: ee_ch9_11

   Create a new list, ``newlist``, that is made up of the last 6 elements of ``lst``. Then assign the fourth element of the new list to the variable ``output``. Note: This should work regardless of the length of the list.
   ~~~~
   lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testElevenA(self):
         self.assertEqual(newlist, ["plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"], "Testing that newlist value is assigned to correct value.")

      def testElevenB(self):
         self.assertEqual(output, 22, "Testing that output value is assigned to correct value.")

   myTests().main()


.. activecode:: ee_ch9_111
   :tags: Sequences/TheSliceOperator.rst, Sequences/AccessingElements.rst

   Create a new list called ``small_lst`` whose elements are the last five of ``new_lst``. Do this so that it would work, no matter how long new_lst is. Then assign the third element of small_lst to the variable ``third``.
   ~~~~
   new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(small_lst, new_lst[-5:], "Testing that small_lst has the correct elements assigned.")

      def testTwo(self):
         self.assertEqual(third, small_lst[2], "Testing that third has the correct element assigned.")

   myTests().main()


.. activecode:: ee_ch9_12

   Remove the whitespace from the beginning and end of ``str1`` and assign the new string to variable ``newstring``. Then save the number of characters of ``newstring`` to ``newlength``. Next, split ``newstring`` on every occurrence the letter 'p' and assign that to ``output``.
   ~~~~
   str1 = "     peter piper picked a peck of pickled peppers.               "
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwelveA(self):
         self.assertEqual(newstring, "peter piper picked a peck of pickled peppers.", "Testing that newstring value is assigned to correct value.")

      def testTwelveB(self):
         self.assertEqual(newlength, 45, "Testing that newlength value is assigned to correct value.")

      def testTwelveC(self):
         self.assertEqual(output, ['', 'eter ', 'i', 'er ', 'icked a ', 'eck of ', 'ickled ', 'e', '', 'ers.'], "Testing that output value is assigned to correct value.")

   myTests().main()


.. activecode:: ee_ch_121
   :tags: Sequences/StringMethods.rst, Sequences/Length.rst, Sequences/SplitandJoin.rst

   Remove the white space from the beginning and the end of the string bound to the variable ``full_sent`` and assign that to the variable ``sent``. Then, save the number of characters in sent to a variable called ``char_sent``. Finally, assign to the variable ``word_c``, the value of ``sent`` that is split on every occurance of the letter **c**.
   ~~~~
   full_sent = "     A broken clock is correct at least twice a day.    "

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sent, full_sent.strip(), "Testing that sent has been correctly assigned.")
      
      def testTwo(self): 
         self.assertEqual(char_sent, len(sent), "Testing that char_sent has been correctly assigned.")
      
      def testThree(self):
         self.assertEqual(word_c, sent.split('c'), "Testing that word_c has been correctly assigned.")

   myTests().main() 