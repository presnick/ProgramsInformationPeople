
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

.. datafile:: files_extra.txt
   :hide:

   This summer I will be travelling.
   I will go to...
   Italy: Rome
   Greece: Athens
   England: London, Manchester
   France: Paris, Nice, Lyon
   Spain: Madrid, Barcelona, Granada
   Austria: Vienna
   I will probably not even want to come back! 
   However, I wonder how I will get by with all the different languages.
   I only know English!

Lecture 6: Waiver Challenge Exercises
=====================================

.. _lecture_6_waiver:


.. activecode:: ee_ch11_04
   :tags:Selection/Chainedconditionals.rst
   :autograde: unittest

   For each grade in list ``grades``, if the grade is greater than 90, add "Whoa, good job!" to list ``notes``. If less than 90 but greater than 80, add "Keep it up!" to the list. If less than 80 but greater than 70, add "Great opportunity to figure out confusions!". If less than 70, add "Join us at office hours! It's great."
   ~~~~  
   grades = [95, 50, 85, 74, 67]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(notes, ['Whoa, good job!', "Join us at office hours! It's great.", 'Keep it up!', 'Great opportunity to figure out confusions!', "Join us at office hours! It's great."], "Testing that notes holds a list with the correct elements.")

   myTests().main()


.. activecode:: ee_ch11_071
   :tags: Selection/Nestedconditionals.rst
   :autograde: unittest

   Say you are shipping a package that normally costs 5 dollars to ship to another place in your city. You want to find out the price for shipping it further away. 

   Create conditionals so that if it is shipping domestically (where the variable ``country`` has the value ``domestic``), and 0 states away (``d_dist`` = ``0``), then the variable ``price`` is set to ``5``, if is one state away, then price is set to ``10``, and otherwise, the price is set to ``15``. Otherwise, if it is not domestic, then you need to know if it is within the continent. If it is (``i_dist`` = ``0``), then ``price`` is set to ``40``, otherwise, ``price`` is set to ``60``. 

   The variable ``country`` will have ``"domestic"`` or ``"international"`` as the values, and ``d_dist`` will have an integer value for domestic state distance (0 being within the state, 1, being 1 state away, 3 as 3 states away) and ``i_dist`` will have the value of True or False to distinguish if it is within the same continent (``True``) or not (``False``). 

   Use nested conditionals to help someone determine the correct shipping price. Uncomment each set of variables one at a time to test.
   ~~~~
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
   

.. activecode:: ee_ch11_081
   :tags: Selection/Nestedconditionals.rst
   :autograde: unittest

   We're trying to find out if you'll get a ticket or not depending on your speed and where you're driving on the highway. 

   In Michigan, the speed limit is 70, in Hawaii, the speed limit is 60, in Montana the speed limit is 80. 

   Create a list called ``result``. For each element in ``cases``, decide if there should be a ticket given. If their speed is above the speed limit for that state, add "Ticket" to ``result``. Otherwise, add "No Ticket" to ``result``. As a hint, remember that you can convert values to different types.
   ~~~~
   cases = ["Michigan 70", "Michigan 75", "Hawaii 65", "Montana 80", "Michigan 90", "Hawaii 50", "Montana 65"]


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(result, ['No Ticket', 'Ticket', 'Ticket', 'No Ticket', 'Ticket', 'No Ticket', 'No Ticket'], "Testing the contents of result")

   myTests().main()


.. activecode:: ee_ch11_091
   :tags: Selection/ConditionalExecutionBinarySelection.rst
   :autograde: unittest

   For each word in ``wrds``, if 'e' is the last letter of the word, then add 'd', otherwise add 'ed' to the end of the word to make it past tense. Save these past tense words to a list called ``old_wrds``.
   ~~~~
   wrds = ["end", "work", "confess", "decide", "like", "play", "start", "walk", "hate", "love",  "look", "open", "close", "rain", "notice", "learn", "clean", "taste"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(old_wrds, ["ended", 'worked', "confessed", "decided", "liked", "played", "started", "walked", "hated", "loved", "looked", "opened", "closed", "rained", "noticed", "learned", "cleaned", "tasted"], "Testing that the old_wrds list is correct." )

   myTests().main()


.. activecode:: ee_files_03
   :tags: Files/intro-WorkingwithDataFiles.rst
   :autograde: unittest

   Assign the second word of every line of the file called ``files_extra.txt``  to the list saved in the variable ``second``.
   ~~~~
   second = []
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testThree(self):
         self.assertEqual(second, ['summer', 'will', 'Rome', 'Athens', 'London,', 'Paris,', 'Madrid,', 'Vienna', 'will', 'I', 'only'], "Testing that second is assigned to correct value.")

   myTests().main()