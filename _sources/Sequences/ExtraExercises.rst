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

4. Create a new list of the 6th through 14th elements of ``lst`` and assign it to the variable ``output``.

.. activecode:: ee_ch9_04
   
   lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(output, ["shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold"], "Testing that output value is assigned to correct value.")

   myTests().main()

4.1 Create a new list using the 9th through 12th elements of ``new_lst`` and assign it to the variable``sub_lst``.

.. activecode:: ee_ch9_041
   :tags: Sequences/TheSliceOperator.rst

   new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sub_lst, new_lst[8:13], "Testing that sub_lst has the correct elements assigned.")

   myTests().main()

5. Create a new string of ``str1`` but lowercase and assign it to the variable ``output``. Do not hard code this.

.. activecode:: ee_ch9_05
      
   str1 = "OH THE PLACES YOU WILL GO"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFive(self):
         self.assertEqual(output, "oh the places you will go", "Testing that output value is assigned to correct value.")

   myTests().main()

5.1 Create a variable called ``low_stri`` and assign it the value of stri, but lowercase. Do not hardcode this.

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


7.1 Add the string dogs to the end of the list ``pets``. Do this using a list method.

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

9. **Challenge** Please get rid of the pet "cat" from the list ``pets``. Add the pet "dog" in its place.

.. activecode:: ee_ch9_09

   pets = ["goldfish", "cat", "parrot", "hamster"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testNine(self):
         self.assertEqual(pets[1], "dog", "Testing that dog is in correct location.")
         self.assertEqual(pets, ["goldfish", "dog", "parrot", "hamster"], "Testing that output value is assigned to correct value.")

   myTests().main()

9.1 **Challenge:** Please get rid of the fourth element in the list ``office``. Then, replace that element with the string chair.

.. activecode:: ee_ch_091
   :tags: Sequences/ListDeletion.rst, Sequences/ListMethods.rst

   office = ["table", "computer", "clock", "smoothie machine", "water cooler", "fax machine", "printers", "pencils", "desks"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(office[3], "chair", "Testing the fourth element of office.") 
         self.assertEqual(office, ["table", "computer", "clock", "chair", "water cooler", "fax machine", "printers", "pencils", "desks"], "Testing the contents of office.")

   myTests().main()  

10. **Challenge** Create a list made up of the 5th and 37th element from the list ``words`` and assign it to the variable ``output``.

.. activecode:: ee_ch9_10

   words = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTen(self):
         self.assertEqual(output, ["caterpillar", "hotdog"], "Testing that output value is assigned to correct value.")

   myTests().main()

10.1 **Challenge:** Create a list made up of the 11th and 29th elements from the list ``practice`` and assign that to the variable ``content``.

.. activecode:: ee_ch9_101
   :tags: Sequences/ConcatenationandRepetition.rst, Sequences/AccessingElements.rst
   
   practice = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(content, ["wolverine", ["women", "olympics", "gold", "rio", 21, "2016", "men"]], "Testing that content has the correct elements assigned.")

   myTests().main()

11. **Challenge** Create a new list, ``newlist``, that is made up of the last 6 elements of ``lst``. Then assign the fourth element of the new list to the variable ``output``. Note: This should work regardless of the length of the list.

.. activecode:: ee_ch9_11

   lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testElevenA(self):
         self.assertEqual(newlist, ["plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"], "Testing that newlist value is assigned to correct value.")

      def testElevenB(self):
         self.assertEqual(output, 22, "Testing that output value is assigned to correct value.")

   myTests().main()

11.1 **Challenge:** Create a new list called ``small_lst`` whose elements are the last five of ``new_lst``. Do this so that it would work, no matter how long new_lst is. Then assign the third element of small_lst to the variable ``third``.

.. activecode:: ee_ch9_111
   :tags: Sequences/TheSliceOperator.rst, Sequences/AccessingElements.rst

   new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(small_lst, new_lst[-5:], "Testing that small_lst has the correct elements assigned.")

      def testTwo(self):
         self.assertEqual(third, small_lst[2], "Testing that third has the correct element assigned.")

   myTests().main()

12. **Challenge** Remove the whitespace from ``str1`` and assign the new string to variable ``newstring``. Then save the number of characters of ``newstring`` to ``newlength``. Next, split ``newstring`` on every occurrence the letter 'p' and assign to ``output``.

.. activecode:: ee_ch9_12

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

12.1 **Challenge:** Remove the white space in the variable ``full_sent`` and assign that to the variable ``sent``. Then, save the number of characters in sent to a variable called ``char_sent``. Finally, assign to the variable ``word_c``, the value of sent, split on every occurance of the letter c.

.. activecode:: ee_ch_121
   :tags: Sequences/StringMethods.rst, Sequences/Length.rst, Sequences/SplitandJoin.rst

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