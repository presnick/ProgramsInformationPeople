..  Copyright (C)  Lauren Murphy, Susan Doong, Haley Yaremych, Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Exercises
=========

.. activecode:: ee_ch9_01
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/AccessingElements

   **1.** Assign the value of the 34th element of ``lst`` to the variable ``output``.
   ~~~~
   lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(output, "laptop", "Testing that output value is assigned to correct value.")

   myTests().main()


.. activecode:: ee_ch9_011
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/AccessingElements
   
   **2.** Assign the value of the 23rd element of ``lst`` to the variable ``checking``.
   ~~~~
   lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(checking, "leaders and the best", "Testing that checking has the correct element assigned.")

   myTests().main()


.. activecode:: ee_ch9_02
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/ListLength

   **3.** Assign the number of elements in ``lst`` to the variable ``output``.
   ~~~~
   lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwo(self):
         self.assertEqual(output, 52, "Testing that output value is assigned to correct value.")

   myTests().main()


.. activecode:: ee_ch9_021
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/ListLength
   
   **4.** Assign the number of elements in ``lst`` to the variable ``num_lst``.
   ~~~~
   lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(num_lst, 30, "Testing that num_lst has the correct length assigned.")

   myTests().main()


.. activecode:: ee_ch9_03
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/AccessingElements

   **5.** Assign the value of the last element of ``lst`` to the variable ``output``. Do this so that the length of lst doesn't matter.
   ~~~~
   lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testThree(self):
         self.assertEqual(output, "EECS", "Testing that output value is assigned to correct value.")

   myTests().main()


.. activecode:: ee_ch9_031
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/AccessingElements
   
   **6.** Assign the last element of ``lst`` to the variable ``end_elem``. Do this so that it works no matter how long lst is.
   ~~~~
   lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(end_elem, lst[-1], "Testing that end_elem has the correct element assigned.")

   myTests().main()


.. activecode:: ee_ch9_04
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/ListSlices

   **7.** Create a new list of the 6th through 13th elements of ``lst`` (eight items in all) and assign it to the variable ``output``.
   ~~~~
   lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(output, lst[5:13], "Testing that output value is assigned to correct value.")

   myTests().main()


.. activecode:: ee_ch9_041
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/ListSlices

   **8.** Create a new list using the 9th through 12th elements (four items in all) of ``new_lst`` and assign it to the variable``sub_lst``.
   ~~~~
   new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sub_lst, new_lst[8:12], "Testing that sub_lst has the correct elements assigned.")

   myTests().main()


.. activecode:: ee_ch9_05
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/StringMethods

   **9.** Create a new string from ``str1`` that is all lower case, and assign it to the variable ``output``. Do not hard code this: use a python string method to convert ``str1`` to lower case.
   ~~~~
   str1 = "OH THE PLACES YOU WILL GO"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFive(self):
         self.assertEqual(output, "oh the places you will go", "Testing that output value is assigned to correct value.")

   myTests().main()


.. activecode:: ee_ch9_051
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/StringMethods

   **10.** Create a variable called ``low_stri`` and assign it the value of stri, but lowercased. Do not hard code this: use a python string method to convert str1 to lower case.
   ~~~~
   stri = "HELLO AND WELCOME TO THE ACTIVECODE WINDOW."

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(low_stri, stri.lower(), "Testing that low_stri has the correct string assigned.")

   myTests().main()


.. activecode:: ee_ch9_06
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/SplitandJoin

   **11.** Create a variable ``output`` and assign it to a list whose elements are the words in the string ``str1``.
   ~~~~
   str1 = "OH THE PLACES YOU'LL GO"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testSix(self):
         self.assertEqual(output, ["OH", "THE", "PLACES", "YOU'LL", "GO"], "Testing that output value is assigned to correct value.")

   myTests().main()


.. activecode:: ee_ch9_061
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/SplitandJoin

   **12.** Create a variable called ``wrds`` and assign to it a list whose elements are the words in the string ``sent``. Do not worry about punctuation.
   ~~~~
   sent = "The bicentennial for our university is in 2017!"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(wrds, sent.split(), "Testing that wrds has been correctly assigned.")

   myTests().main()


.. activecode:: ee_ch9_07
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/AppendversusConcatenate

   **13.** Add the pet "goldfish" to the end of the list of pets, ``pets``. Do this using a list method.
   ~~~~
   pets = ["cat", "dog", "lizard", "parrot", "hamster"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testSeven(self):
         self.assertEqual(pets, ["cat", "dog", "lizard", "parrot", "hamster", "goldfish"], "Testing that pets value is assigned to correct value.")

   myTests().main()


.. activecode:: ee_ch_071
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/AppendversusConcatenate

   **14.** Add the string "dogs" to the end of the list ``pets``. Do this using a list method.
   ~~~~
   pets = ["cats", "birds", "pigs", "hampsters", "turtles", "snakes", "mice", "rats", "fish"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(pets, ["cats", "birds", "pigs", "hampsters", "turtles", "snakes", "mice", "rats", "fish", "dogs"], "Testing the list pets.") 

   myTests().main()


.. activecode:: ee_ch9_08
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/ListDeletion

   **15.** Get rid of all values of 7 from the list, ``numbers``.
   ~~~~
   numbers = [1, 1, 2, 2, 3, 3, 6, 6, 7, 7, 7, 7, 8, 8, 12, 15]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testEight(self):
         self.assertEqual(numbers, [1, 1, 2, 2, 3, 3, 6, 6, 8, 8, 12, 15], "Testing that output value is assigned to correct value.")

   myTests().main()


.. activecode:: ee_ch_081
   :language: python
   :autograde: unittest
   :practice: T
   :topics: Sequences/ListDeletion

   **16.** Please get rid of the e's from this list.
   ~~~~
   letts = ['a', 'b', 'b', 'c', 'd', 'e', 'e', 'e', 'f', 'f']

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(letts, ['a', 'b', 'b', 'c', 'd', 'f', 'f'], "Testing the list letts.") 

   myTests().main()

