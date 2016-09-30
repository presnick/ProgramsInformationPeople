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


4 Create an empty list called ``resps``. Using the list ``percent_rain``, for each percent, if it is above 90, add the string 'Bring an umbrella.' to ``resps``, otherwise if it is above 80, add the string 'Good for the flowers?' to ``resps``, otherwise if it is above 50, add the string 'Watch out for clouds!' to ``resps``, otherwise, add the string 'Nice day!' to ``resps``.

.. activecode:: ee_ch11_041
   :tags: Selection/Chainedconditionals.rst

   percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(resps, ['Bring an umbrella.','Nice day!','Bring an umbrella.','Watch out for clouds!',"Nice day!",'Nice day!','Watch out for clouds!',"Good for the flowers?"], "Testing the value of resps")

   myTests().main()


5. For each word in list ``words``, find the number of characters in the string. If the number of characters in each string is greater than 3, add 1 to the variable ``num_words`` so that ``num_words`` should end up with the total number of words with more than 3 characters.

.. activecode:: ee_ch11_05
   :tags:Selection/ConditionalExecutionBinarySelection.rst
      
   words = ["water", "chair", "pen", "basket", "hi", "car"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFive(self):
         self.assertEqual(num_words, 3, "Testing that num_words has the correct value.")

   myTests().main()

5.1 For each string in ``wrd_lst``, find the number of characters in the string. If the number of characters is less than 6, add 1 to ``accum`` so that in the end, ``accum`` will contain an integer representing the total number of words in the list that have fewer than 6 characters.

.. activecode:: ee_ch11_051
   :tags:Selection/OmittingtheelseClauseUnarySelection.rst

   wrd_lst = ["Hello", "activecode", "Java", "C#", "Python", "HTML and CSS", "Javascript", "Swift", "php"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(accum, 5, "Testing the value of accum")

   myTests().main()

6. We have created conditionals for you to use. Do not change the provided conditional statements. Find an integer value for ``x`` that will cause ``output`` to hold the values ``True`` and ``None``. (Drawing diagrams or flow charts for yourself may help!)

.. activecode:: ee_ch11_06
   :tags:Selection/Chainedconditionals.rst

   x = 
   output = []

   if x > 63:
       output.append(True)
   elif x > 55:
       output.append(False)
   else: 
       output.append("Neither")

   if x > 67:
       output.append(True)
   else:
       output.append(None)

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testSixA(self):
         self.assertEqual(output, [True, None], "Testing that value of output is correct.")

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


8. **Challenge** In XYZ University, upper level math classes are numbered 300 and up. Upper level English classes are numbered 200 and up. Upper level Psychology classes are 400 and up. Create two lists, ``upper`` and ``lower``. Assign each course in ``classes`` to the correct list, ``upper`` or ``lower``. HINT: remember, you can convert some strings to different types!

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


9. For each word in ``words``, add 'd' to the end of the word if the word ends in "e" to make it past tense. Otherwise, add 'ed' to make it past tense. Save these past tense words to a list called ``past_tense``.

.. activecode:: ee_ch11_09

   words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testNine(self):
         self.assertEqual(past_tense, ['adopted', 'baked', 'beamed', 'confided', 'grilled', 'planted', 'timed', 'waved', 'wished'], "Testing that the past_tense list is correct.")

   myTests().main()


