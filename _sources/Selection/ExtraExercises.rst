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

1. Write code to assign the string ``"You can apply to SI!"`` to ``output`` *if* the string ``"SI 106"`` is in the list ``courses``. If it is not in ``courses``, assign the value ``"Take SI 106!"`` to the variable ``output``.

.. activecode:: ee_ch11_01
   :tags:Selection/ConditionalExecutionBinarySelection.rst

   courses = ["ENGR 101", "SI 110", "ENG 125", "SI 106", "CHEM 130"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(output, "You can apply to SI!", "Testing that output has the correct value, given the courses list provided")

   myTests().main()

1.1 Write code so that if ``"STATS 250"`` is in the list ``schedule``, then the string ``"You could be in Information Science!"`` is assigned to the variable ``resp``. Otherwise, the string ``"That's too bad."`` should be assigned to the variable ``resp``.

.. activecode:: ee_ch11_011
   :tags: Selection/ConditionalExecutionBinarySelection.rst

   schedule = ["SI 106", "STATS 250", "SI 110", "ENGLISH 124/125"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(resp, "You could be in Information Science!", "Testing the value of resp given the schedule list provided.")

   myTests().main()

2. Create a variable, ``b``, and assign it the value of ``15``. Then, write code to see if the value ``b`` is greater than that of ``a``. If it is, ``a``'s value should be multiplied by 2. If the value of ``b`` is less than or equal to ``a``, nothing should happen. Finally, create variable ``c`` and assign it the value of the sum of ``a`` and ``b``.

.. activecode:: ee_ch11_02
   :tags:Selection/OmittingtheelseClauseUnarySelection.rst

   a = 20
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwoA(self):
         self.assertEqual(a, 20, "Testing that a has the correct value.")

      def testTwoB(self):
         self.assertEqual(c, 35, "Testing that c has the correct value.")

   myTests().main()

2.2 Create the variable ``z`` whose value is ``30``. Write code to see if ``z`` is greater than ``y``. If so, add 5 to ``y``'s value, otherwise do nothing. Then, multiply ``z`` and ``y``, and assign the resulting value to the variable ``x``.

.. activecode:: ee_ch11_022
   :tags: Selection/OmittingtheelseClauseUnarySelection.rst

   y = 22

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(x, 810, "Testing the value of x")
      def testTwo(self):
         self.assertEqual(z, 30, "Testing that z has correctly been defined.")

   myTests().main()

3. Create one conditional to find whether "false" is in string ``str1``. If so, assign variable ``output`` to  the string ``"False. You aren't you?".`` Otherwise, if "true" is in string ``str1``. If so, assign variable ``output`` to "True! You are you!". If neither are in ``str1``, assign ``output`` to "Neither true nor false!"

.. activecode:: ee_ch11_03
   :tags:Selection/Chainedconditionals.rst

   str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testThree(self):
         self.assertEqual(output, "True! You are you!", "Testing that output has the correct value, given the str1 provided.")

   myTests().main()

3.1 Create one conditional so that if "Friendly" is in ``w``, then "Friendly is here!" should be assigned to the variable ``wrd``. If it's not, check if "Friend" is in w. If so, the string "Friend is here!" should be assigned to the variable ``wrd``, otherwise "No variation of friend is in here." should be assigned to the variable wrd. (Also consider: does the order of your conditional statements matter for this problem? Why?)

.. activecode:: ee_ch11_031
   :tags: Selection/Chainedconditionals.rst

   w = "Friendship is a wonderful human experience!"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(wrd, "Friend is here!", "Testing the value of wrd")

   myTests().main()


4. **Challenge** For each grade in list ``grades``, if the grade is greater than 90, add "Whoa, good job!" to list ``notes``. If less than 90 but greater than 80, add "Keep it up!". If less than 80 but greater than 70, add "Great opportunity to figure out confusions!". If less than 70, add "Join us at office hours!"

.. activecode:: ee_ch11_04
   :tags:Selection/Chainedconditionals.rst
      
   grades = [95, 50, 85, 74, 67]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(notes, ['Whoa, good job!', 'Join us at office hours!', 'Keep it up!', 'Great opportunity to figure out confusions!', 'Join us at office hours!'], "Testing that notes holds a list with the correct elements.")

   myTests().main()

4.1 Create an empty list called ``resps``. Using the list ``percent_rain``, for each grade, if it is above 90, add the string 'Bring an umbrella.' to resps, otherwise if it is above 80, add the string 'Good for the flowers?' to resps, otherwise if it is above 50, add the string 'Watch out for clouds!' to resps, otherwise, add the string 'Nice day!' to resps.

.. activecode:: ee_ch11_041
   :tags: Selection/Chainedconditionals.rst

   percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(resps, ['Bring an umbrella.','Nice day!','Bring an umbrella.','Watch out for clouds!',"Nice day!",'Nice day!','Watch out for clouds!',"Good for the flowers?"], "Testing the value of resps")

   myTests().main()


5. For each word in list ``words``, find the number of characters in the string. If the number of characters in each string is greater than 3, add 1 to the variable "num_words" so that ``num_words`` should end up with the total number of words with more than 3 characters.

.. activecode:: ee_ch11_05
   :tags:Selection/ConditionalExecutionBinarySelection.rst
      
   words = ["water", "chair", "pen", "basket", "hi", "car"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFive(self):
         self.assertEqual(num_words, 3, "Testing that num_words has the correct value.")

   myTests().main()

5.1 For each string in ``wrd_lst``, find the number of characters in the string. If the number of characters is less than 6, add 1 to ``accum`` so that in the end, accum will have the total number of words that have fewer than 6 characters.

.. activecode:: ee_ch11_051
   :tags:Selection/OmittingtheelseClauseUnarySelection.rst

   wrd_lst = ["Hello", "activecode", "Java", "C#", "Python", "HTML and CSS", "Javascript", "Swift", "php"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(accum, 5, "Testing the value of accum")

   myTests().main()

6. We have created conditionals for you to use. Do not change the conditional statements. Find an integer value of x that will cause ``output`` to hold the string values ``"True"`` and ``"None"``. (Drawing diagrams or flow charts for yourself may help!)

.. activecode:: ee_ch11_06
   :tags:Selection/Chainedconditionals.rst

   x = 
   output = []

   if x > 63:
       output.append("True")
   elif x > 55:
       output.append("False")
   else: 
       output.append("Neither")

   if x > 67:
       output.append("True")
   else:
       output.append("None")

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testSixA(self):
         self.assertEqual(output, ["True", "None"], "Testing that value of output is correct.")

      def testSixB(self):
         self.assertEqual(x in [64, 65, 66, 67], True, "Testing that value of x is reasonable for this problem")

   myTests().main()


6.1 We have written conditionals for you to use. Create the variable x and assign it to some integer so that at the end of the code, ``output`` will be assigned the string ``"Consistently working"``.

.. activecode:: ee_ch11_061
   :tags: Selection/Chainedconditionals.rst


   if x >= 10:
       output = "working"
   else:
       output = "Still working"
   if x > 12:
       output = "Always working"
   elif x < 7:
       output = "Forever working"
   else:
       output = "Consistently working"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(output, "Consistently working", "Testing the value of output")
      def testTwo(self):
         self.assertEqual(x in [7,8,9,10,11,12], True, "Testing that x was assigned a correct number" )

   myTests().main()


7. **Challenge** Say you are shipping a package that normally costs 5 dollars to ship to another place in your city. You want to find out the price for shipping further away. Create conditionals so that if it is shipping domestically (where the variable ``country`` has the value ``domestic``), and 0 states away (``d_dist`` = ``0``), then the variable ``price`` is set to ``5``, if is one state away, then price is set to ``10``, and otherwise, the price is set to ``15``. Otherwise, if it is not domestic, then you need to know if it is within the continent. If it is (``i_dist`` = ``0``), then ``price`` is set to ``40``, otherwise, ``price`` is set to ``60``. The variable ``country`` will have ``"domestic"`` or ``"international"`` as the values, and ``d_dist`` will have an integer value for domestic state distance (0 being within the state, 1, being 1 state away, 3 as 3 states away) and ``i_dist`` will have the value of True or False to distinguish if it is within the same continent (``True``) or not (``False``). Use nested conditionals to help someone determine the correct shipping price. Uncomment each set of variables one at a time to test.

.. activecode:: ee_ch11_071
   :tags: Selection/Nestedconditionals.rst

   #Uncomment the next 3 lines to test domestic, in-state
   #country = "domestic"
   #d_dist = 0
   #i_dist = True

   #Uncomment the next 3 lines to test domestic, one state away
   #country = "domestic"
   #d_dist = 1
   #i_dist = True

   #Uncomment the next 3 lines to test domestic, multiple states away
   #country = "domestic"
   #d_dist = 3
   #i_dist = True

   #Uncomment the next 3 lines to test international, within continent
   #country = "international"
   #d_dist = 0
   #i_dist = True

   #Uncomment the next 3 lines to test international, not in continent
   #country = "international"
   #d_dist = 0
   #i_dist = False


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         if country == "domestic" and d_dist == 0:
            self.assertEqual(price, 5, "Testing the value of price with domestic, in-state")
         elif country == "domestic" and d_dist == 1:
            self.assertEqual(price, 10, "Testing the value of price with domestic, one state away")
         elif country == "domestic" and d_dist >= 2:
            self.assertEqual(price, 15, "Testing the value of price with domestic, multiple states away")
         elif country == "international" and i_dist == True:
            self.assertEqual(price, 40, "Testing the value of price with international, within continent")
         elif country == "international" and i_dist == False:
            self.assertEqual(price, 60, "Testing the value of price with international, not in continent")
         else:
            print "Test not able to run, looking for specific values. Check your spelling and value types and use print statements."


   myTests().main()


8. **Challenge** In XYZ University, upper level math classes are numbered 300 and up. Upper level English classes are numbered 200 and up. Upper level Psychology classes are 400 and up. Create two lists, ``upper`` and ``lower``. Assign each course in ``classes`` to the correct list, upper or lower. As a hint, remember you can convert some strings to different types.

.. activecode:: ee_ch11_08
   :tags: Selection/Nestedconditionals.rst
      
   classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testEightA(self):
         self.assertEqual(upper, ['PSYCH 412', 'MATH 300', 'MATH 404', 'ENG 201', 'PSYCH 508', 'ENG 220'], "Testing that the upper list exists and contains the correct elements.")
      def testEightB(self):
         self.assertEqual(lower, ['MATH 150', 'PSYCH 111', 'PSYCH 313', 'MATH 206', 'ENG 100', 'ENG 103', 'ENG 125', 'ENG 124'], "Testing that the lower list exists and contains the correct elements.")
      

   myTests().main()

8.1 **Challenge:** We're trying to find out if you'll get a ticket or not depending on your speed and where you're driving on the highway. In Michigan, the speed limit is 70, in Hawaii, the speed limit is 60, in Montana the speed limit is 80. Create a list called ``result``. For each element in ``cases``, decide if there should be a ticket given. If their speed is above the speed limit for that state, add "Ticket" to ``result``. Otherwise, add "No Ticket" to ``result``. As a hint, remember that you can convert values to different types.

.. activecode:: ee_ch11_081
   :tags: Selection/Nestedconditionals.rst

   cases = ["Michigan 70", "Michigan 75", "Hawaii 65", "Montana 80", "Michigan 90", "Hawaii 50", "Montana 65"]


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(result, ['No Ticket', 'Ticket', 'Ticket', 'No Ticket', 'Ticket', 'No Ticket', 'No Ticket'], "Testing the contents of result")

   myTests().main()

9. For each word in ``words``, add 'd' to the end of the word if the word ends in "e" to make it past tense. Otherwise, add 'ed' to make it past tense. Save these past tense words to a list called ``past_tense``.

.. activecode:: ee_ch11_09

   words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testNine(self):
         self.assertEqual(past_tense, ['adopted', 'baked', 'beamed', 'confided', 'grilled', 'planted', 'timed', 'waved', 'wished'], "Testing that the past_tense list is correct.")

   myTests().main()

9.1 For each word in ``wrds``, if 'e' is the last letter of the word, then add 'd', otherwise add 'ed' to the end of the word to make it past tense. Save these past tense words to a list called ``old_wrds``.

.. activecode:: ee_ch11_091
   :tags: Selection/ConditionalExecutionBinarySelection.rst

   wrds = ["end", "work", "confess", "decide", "like", "play", "start", "walk", "hate", "love",  "look", "open", "close", "rain", "notice", "learn", "clean", "taste"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(old_wrds, ["ended", 'worked', "confessed", "decided", "liked", "played", "started", "walked", "hated", "loved", "looked", "opened", "closed", "rained", "noticed", "learned", "cleaned", "tasted"], "Testing that the old_wrds list is correct." )

   myTests().main()


