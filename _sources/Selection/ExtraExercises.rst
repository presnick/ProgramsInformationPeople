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

1. Write code to assign the string "You can apply to SI!" to ``output`` if "SI 106" is in the list ``courses``. If it is not in ``courses``, assign ``output`` to "Take SI 106!"

.. activecode:: ee_ch11_01
   :tags:Selection/ConditionalExecutionBinarySelection.rst

   courses = ["ENGR 101", "SI 110", "ENG 125", "SI 106", "CHEM 130"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(output, "You can apply to SI!", "Testing that output is assigned to correct values")

   myTests().main()

1.1 Write code so that if "STATS 250" is in the list ``schedule`` then the string "You could be in Information Science!" is assigned to the variable ``resp``. Otherwise, the string "That's too bad." is assigned to the variable ``resp``.

.. activecode:: ee_ch11_011
   :tags: Selection/ConditionalExecutionBinarySelection.rst

   schedule = ["SI 106", "STATS 250", "SI 110", "ENGLISH 124/125"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(resp, "You could be in Information Science!", "Testing the value of resp.")

   myTests().main()

2. Create another variable, ``b``, and assign it the value of 15. Then, test to see if ``b`` is greater than ``a``. If so, then multiply ``a`` by 2. If ``b`` is less than ``a``, nothing should happen. Finally, create variable ``c`` and assign it the value of the sum of ``a`` and ``b``.

.. activecode:: ee_ch11_02
   :tags:Selection/OmittingtheelseClauseUnarySelection.rst

   a = 20
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwoA(self):
         self.assertEqual(a, 20, "Testing that a is assigned to correct value.")

      def testTwoB(self):
         self.assertEqual(c, 35, "Testing that c is assigned to correct value.")

   myTests().main()

2.2 Create the variable ``z`` whose value is 30. Test to see if z is greater than ``y``,  if so then add 5 to y, otherwise do nothing. Then, multiply z and y, and assign that value to the variable ``x``.

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

3. Create one conditional to test if "false" is in string ``str1``. If so, assign variable ``output`` to "False. You aren't you?". Otherwise, test if "true" is in string ``str1``. If so, assign variable ``output`` to "True! You are you!". If neither are in ``str1``, assign ``output`` to "Neither true nor false!"

.. activecode:: ee_ch11_03
   :tags:Selection/Chainedconditionals.rst

   str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testThree(self):
         self.assertEqual(output, "True! You are you!", "Testing that action is assigned to correct values.")

   myTests().main()

3.1 Create one conditional so that if "Friendly" is in ``w``, then "Friendly is here!" should be assigned to the variable ``wrd``, otherwise if "Friend" is in w, then "Friend is here!" should be assigned to the variable wrd, otherwise "No variation of friend is in here." should be assigned to the variable wrd.

.. activecode:: ee_ch11_031
   :tags: Selection/Chainedconditionals.rst

   w = "Friendship is a wonderful human experience!"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(wrd, "Friend is here!", "Testing the value of wrd")

   myTests().main()


4. **Challenge** For each grade in list ``grades``, if the grade is greater than 90, add "Good job!" to list ``notes``. If less than 90 but greater than 80, add "Keep it up!". If less than 80 but greater than 70, add "Study some more!". If less than 70, add "Try going to office hours!"

.. activecode:: ee_ch11_04
   :tags:Selection/Chainedconditionals.rst
      
   grades = [95, 50, 85, 74, 67]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(notes, ['Good job!', 'Try going to office hours!', 'Keep it up!', 'Study some more!', 'Try going to office hours!'], "Testing that notes is assigned to correct values.")

   myTests().main()

4.1 Create an empty list called ``resps``. Using the list ``grades``, for each grade, if it is above 90, add the string 'Congrats!' to resps, otherwise if it is above 80, add the string 'Good work!' to resps, otherwise if it is above 70, add the string 'You can do it!' to resps, otherwise, add the string 'You should try going to office hours.' to resps.

.. activecode:: ee_ch11_041
   :tags: Selection/Chainedconditionals.rst

   grades = [94.3, 87, 100, 78, 83, 63.5, 79, 86]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(resps, ['Congrats!','Good work!','Congrats!','You can do it!',"Good work!",'You should try going to office hours.','You can do it!',"Good work!"], "Testing the value of resps")

   myTests().main()


5. For each word in list ``words``, find the number of characters in the string. If the number of characters in each string is greater than 3, add 1 to the variable "num_words" so that num_words should have the total number of words with less than 3 characters.

.. activecode:: ee_ch11_05
   :tags:Selection/ConditionalExecutionBinarySelection.rst
      
   words = ["water", "chair", "pen", "basket", "hi", "car"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFive(self):
         self.assertEqual(num_words, 3, "Testing that num_words is assigned to correct values.")

   myTests().main()

5.1 For each string in ``wrd_lst``, find the number of characters in the string. If the number of characters is less than 6, add 1 to ``accum`` so that in the end, accum will have the total number of words that have fewer than 6 characters.

.. activecode:: ee_ch11_051
   :tags: Selection/OmittingtheelseClauseUnarySelection.rst

   wrd_lst = ["Hello", "activecode", "Java", "C#", "Python", "HTML and CSS", "Javascript", "Swift", "php"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(accum, 5, "Testing the value of accum")

   myTests().main()

6. We have created conditionals for you to use. Find an integer value of x that will output "True" and "None".

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
         self.assertEqual(output, ["True", "None"], "Testing that output is correct.")

      def testSixB(self):
         self.assertEqual(x in [64, 65, 66, 67], True, "Testing that value of x is correct.")

   myTests().main()

.. works for 64-67

6.1 We have written conditionals for you to use. Create the variable x and assign it to some integer so that at the end of the code, ``output`` will be assigned the string "Consistently working".

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

7. Create a set of conditionals to determine shipping prices. Usually, it will cost you $7 to ship a large package within your state. In this case, ``location`` would be "domestic", the variable ``cost`` would be set to 7, and ``destination`` would be ``0``. If you continue to ship domestically, the cost of shipping for 1 state away is $11. For 2 states away, the cost is $15. For 3 states away, the cost is $19. If the destination is 4 or more states away, the shipping cost is fixed at $25. If you ship international the variable ``i_dest`` is 0 (within your continent), the cost is $30. Anywhere other than your continent ``i_dest`` would be set to 1 and the cost is $45. 
The variable ``location`` will have either the value "domestic" or "international". If domestic, the variable ``destination`` could have the values 0 (within the state), 1 (1 state away), 2 (2 states away), 3 (3 states away), or 4 and above (4 or more states away). If international, ``i_dest`` will either be 0 (within your continent) or 1 (out of your continent)
Use nested conditionals to help someone determine the shipping cost. Uncomment each set of variables one at a time to test.

.. activecode:: ee_ch11_07
   :tags: Selection/Nestedconditionals.rst

   #Uncomment next two lines to test domestic and 2 states away.
   #location = "domestic"
   #destination = 2

   #Uncomment next two lines to test international and not on your continent.
   #location = "international"
   #i_dest = 1

   #Uncomment next two lines to test domestic and 6 states away.
   #location = "domestic"
   #destination = 6
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testSeven(self):
         if location == "domestic" and destination == 2:
          self.assertEqual(cost, 15, "Testing that cost is assigned to correct value.")

         elif location == "international" and i_dest == 1:
          self.assertEqual(cost, 45, "Testing that cost is assigned to correct value.")

         elif location == "domestic" and destination == 6:
          self.assertEqual(cost, 25, "Testing that cost is assigned to correct value.")

         else:
          print "Test not able to run. Check for specific values."

   myTests().main()


7.1 Say you are shipping a package that costs 5 dollars to ship usually. You want to find out the price though for shipping farther than your town. Create conditionals so that if it is shipping domestically, within the state, then the variable ``price`` is set to 5, if is one state away, then price is set to 10, otherwise it is set to 15. Otherwise, if it is not domestic, then if it is within the continent, then price is set to 40, otherwise, price is set to 60. The variable ``country`` will have "domestic" or "international" as the values, and ``d_dist`` will have an integer value for domestic state distance (0 being within the state, 1, being 1 state away, 3 as 3 states away) and ``i_dist`` will have the value of True or False to distinguish if it is within the same continent(True) or not (False). Use nested conditionals to help someone determine the shipping price. Uncomment each set of variables one at a time to test.

.. activecode:: ee_ch11_071
   :tags: Selection/Nestedconditionals.rst

   #Uncomment the next 3 lines to test domestic, in-state
   #country = "domestic"
   #d_dist = 0

   #Uncomment the next 3 lines to test domestic, one state away
   #country = "domestic"
   #d_dist = 1

   #Uncomment the next 3 lines to test domestic, multiple states away
   #country = "domestic"
   #d_dist = 3

   #Uncomment the next 3 lines to test international, within continent
   #country = "international"
   #i_dist = True

   #Uncomment the next 3 lines to test international, not in continent
   #country = "international"
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
            print "Test not able to run, looking for specific values, check spelling and value types."


   myTests().main()


8. **Challenge** In XYZ University, upper level math classes are numbered 300 and up. Upper level English classes are numbered 200 and up. Upper level Psychology classes are 400 and up. Create two lists, ``upper`` and ``lower``. Assign each course in ``classes`` to the correct list, upper or lower. As a hint, remember you can convert strings to different types.

.. activecode:: ee_ch11_08
   :tags: Selection/Nestedconditionals.rst
      
   classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testEightA(self):
         self.assertEqual(upper, ['PSYCH 412', 'MATH 300', 'MATH 404', 'ENG 201', 'PSYCH 508', 'ENG 220'], "Testing that u_math is assigned to correct values.")
      def testEightB(self):
         self.assertEqual(lower, ['MATH 150', 'PSYCH 111', 'PSYCH 313', 'MATH 206', 'ENG 100', 'ENG 103', 'ENG 125', 'ENG 124'], "Testing that l_math is assigned to correct values.")
      

   myTests().main()

8.1 **Challenge:** We're trying to find out if you'll get a ticket or not depending on your speed and where you're driving on the highway. In Michigan, the speed limit is 70, in Hawaii, the speed limit is 60, in Montana the speed limit is 80. Create a list called ``result``. For each element in cases, decide if there should be a ticket given. If their speed is above the speed limit for that state, add "Ticket" to result. Otherwise, add "No Ticket" to result. As a hint, remember that you can convert values to different types.

.. activecode:: ee_ch11_081
   :tags: Selection/Nestedconditionals.rst

   cases = ["Michigan 70", "Michigan 75", "Hawaii 65", "Montana 80", "Michigan 90", "Hawaii 50", "Montana 65"]


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(result, ['No Ticket', 'Ticket', 'Ticket', 'No Ticket', 'Ticket', 'No Ticket', 'No Ticket'], "Testing the contents of result")

   myTests().main()

9. For each word in ``words``, add '-d' to the end of the word if the word ends in "e" to make it past tense. Otherwise, add '-ed' to make it past tense. Save these past tense words to a list called ``past_tense``.

.. activecode:: ee_ch11_09

   words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testNine(self):
         self.assertEqual(past_tense, ['adopted', 'baked', 'beamed', 'confided', 'grilled', 'planted', 'timed', 'waved', 'wished'], "Testing that past_tense is assigned to correct values.")

   myTests().main()

9.1 For each word in ``wrds``, if 'e' is the last letter of the word, then add 'd', otherwise add 'ed' to the end of the word to make it past tense. Save these past tense words to a list called ``old_wrds``.

.. activecode:: ee_ch11_091
   :tags: Selection/ConditionalExecutionBinarySelection.rst

   wrds = ["end", "work", "confess", "decide", "like", "play", "start", "walk", "hate", "love",  "look", "open", "close", "rain", "notice", "learn", "clean", "taste"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(old_wrds, ["ended", 'worked', "confessed", "decided", "liked", "played", "started", "walked", "hated", "loved", "looked", "opened", "closed", "rained", "noticed", "learned", "cleaned", "tasted"], "Testing that old_wrds has been created correctly." )

   myTests().main()














​


