..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Extra Exercises
===============

1. Assign the value of the 34st element of ``lst`` to the variable ``output``.

.. activecode:: ee_ch9_01
   
   lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(output, "laptop", "Testing that output value is assigned to correct value.")

   myTests().main()

1.1 Assign the value of the 23rd element of ``lst`` to the variable ``checking``.

.. activecode:: ee_ch9_011
   :tags: Sequences/AccessingElements.rst
   
   lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(checking, "leaders and the best", "Testing that checking has the correct element assigned.")

   myTests().main()

2. Assign the number of elements in ``lst`` to the variable ``output``.

.. activecode:: ee_ch9_02
  
   lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwo(self):
         self.assertEqual(output, 52, "Testing that output value is assigned to correct value.")

   myTests().main()

2.1 Assign the number of elements in ``lst`` to the variable ``num_lst``.

.. activecode:: ee_ch9_021
   :tags: Sequences/Length.rst
   
   lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(num_lst, 30, "Testing that num_lst has the correct length assigned.")

   myTests().main()

3. Assign the value of the last element of ``lst`` to the variable the variable ``output``. Do this so that it doesn't matter the length of lst. 

.. activecode:: ee_ch9_03
   
   lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testThree(self):
         self.assertEqual(output, "EECS", "Testing that output value is assigned to correct value.")

   myTests().main()

3.1 Assign the last element of ``lst`` to the variable ``end_elem``. Do this so that it works no matter how long lst is.

.. activecode:: ee_ch9_031
   :tags: Sequences/AccessingElements.rst
   
   lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(end_elem, lst[-1], "Testing that end_elem has the correct element assigned.")

   myTests().main()

4. Create a new list of the 6th through 13th elements of ``lst`` (eight items in all) and assign it to the variable ``output``.

.. activecode:: ee_ch9_04
   
   lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(output, lst[5:13], "Testing that output value is assigned to correct value.")

   myTests().main()

4.1 Create a new list using the 9th through 12th elements (four items in all) of ``new_lst`` and assign it to the variable``sub_lst``.

.. activecode:: ee_ch9_041
   :tags: Sequences/TheSliceOperator.rst

   new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sub_lst, new_lst[8:12], "Testing that sub_lst has the correct elements assigned.")

   myTests().main()

5. Create a new string from ``str1`` that is all lower case, and assign it to the variable ``output``. Do not hard code this: use a python string method to convert str1 to lower case.

.. activecode:: ee_ch9_05
      
   str1 = "OH THE PLACES YOU WILL GO"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFive(self):
         self.assertEqual(output, "oh the places you will go", "Testing that output value is assigned to correct value.")

   myTests().main()

5.1 Create a variable called ``low_stri`` and assign it the value of stri, but lowercased. Do not hard code this: use a python string method to convert str1 to lower case.

.. activecode:: ee_ch9_051
   :tags: Sequences/StringMethods.rst

   stri = "HELLO AND WELCOME TO THE ACTIVECODE WINDOW."

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(low_stri, stri.lower(), "Testing that low_stri has the correct string assigned.")

   myTests().main()

6. Create a variable ``output`` and assign it to a list whose elements are the words in the string ``str1``. 

.. activecode:: ee_ch9_06
      
   str1 = "OH THE PLACES YOU'LL GO"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testSix(self):
         self.assertEqual(output, ["OH", "THE", "PLACES", "YOU'LL", "GO"], "Testing that output value is assigned to correct value.")

   myTests().main()

6.1 Create a variable called ``wrds`` and assign to it a list whose elements are the words in the string ``sent``. Do not worry about punctuation.

.. activecode:: ee_ch9_061
   :tags: Sequences/SplitandJoin.rst

   sent = "The bicentennial for our university is in 2017!"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(wrds, sent.split(), "Testing that wrds has been correctly assigned.")

   myTests().main()


7. Add the pet "goldfish" to the end of the list of pets, ``pets``. Do this using a list method.

.. activecode:: ee_ch9_07
    
   pets = ["cat", "dog", "lizard", "parrot", "hamster"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testSeven(self):
         self.assertEqual(pets, ["cat", "dog", "lizard", "parrot", "hamster", "goldfish"], "Testing that pets value is assigned to correct value.")

   myTests().main()


7.1 Add the string "dogs" to the end of the list ``pets``. Do this using a list method.

.. activecode:: ee_ch_071
   :tags: Sequences/AppendversusConcatenate.rst

   pets = ["cats", "birds", "pigs", "hampsters", "turtles", "snakes", "mice", "rats", "fish"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(pets, ["cats", "birds", "pigs", "hampsters", "turtles", "snakes", "mice", "rats", "fish", "dogs"], "Testing the list pets.") 

   myTests().main()

8. Get rid of all values of 7 from the list, ``numbers``. 

.. activecode:: ee_ch9_08

   numbers = [1, 1, 2, 2, 3, 3, 6, 6, 7, 7, 7, 7, 8, 8, 12, 15]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testEight(self):
         self.assertEqual(numbers, [1, 1, 2, 2, 3, 3, 6, 6, 8, 8, 12, 15], "Testing that output value is assigned to correct value.")

   myTests().main()

8.1 Please get rid of the e's from this list.

.. activecode:: ee_ch_081
   :tags: Sequences/ListDeletion.rst

   letts = ['a', 'b', 'b', 'c', 'd', 'e', 'e', 'e', 'f', 'f']

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(letts, ['a', 'b', 'b', 'c', 'd', 'f', 'f'], "Testing the list letts.") 

   myTests().main()
