
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

Lecture 7: Waiver Challenge Exercises
=====================================

.. _lecture_7_waiver:


.. activecode:: ee_ch12_04
   :tags:Dictionaries/Dictionarymethods.rst

   The dictionary ``china_medals`` shows the events China has medaled in and the number of medals won. Create a list of only the keys from ``china_medals`` and save it in a variable called ``events``. Do not hard-code this. (You can do this in one line of code!)
   ~~~~
   china_medals = {'weightlifting':7, 'diving':6, 'table tennis':4, 'shooting':7, 'swimming':6}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(sorted(events), sorted(['weightlifting', 'diving', 'table tennis', 'shooting', 'swimming']) , "Testing that events holds the correct list.")

   myTests().main()



.. activecode:: ee_ch12_05
   :tags:Dictionaries/Dictionaryoperations.rst
   :autograde: unittest

   The dictionary ``dives`` contains the moves and the number of times each move has been performed. The list ``performed`` is a list of additional diving moves that have just been performed. Write code to update the dictionary ``dives``, so that for each move in the list ``performed``, if the move is in the dictionary ``dives`` already, you should update the value in the dictionary by 1. If that move is not in the dictionary ``dives`` yet, add a new key-value pair to the dictionary to record that move.
   ~~~~
   performed = ['reverse tuck', 'forward 2 1/2 somersault pike', 'back dive', 'twist in pike']
      
   dives = {'twist in free': 1, 'back dive': 2, 'armstand reverse': 1, 'forward tuck':5, 'reverse tuck': 3}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFive(self):
         self.assertEqual(sorted(dives.items()), sorted([('forward tuck', 5), ('reverse tuck', 4), ('forward 2 1/2 somersault pike', 1), ('back dive', 3), ('twist in free', 1), ('armstand reverse', 1), ('twist in pike', 1)]), "Testing that dives has been updated correctly.")

   myTests().main()


.. activecode:: ee_ch12_051
   :tags:Dictionaries/Dictionaryoperations.rst

   The list ``current`` contains some of the sports that were played in the 2016 Olympics. The dictionary ``sport_counts`` contains some of the sports that have been played in prior Olympic meets, and how many Olympics they were played in. 

   Iterate through each sport included in the dictionary ``sport_counts`` and update its value by 1 if it was played in 2016 (if it was not played in 2016, its value should not be changed, and you should not record sports that are not already recorded in the dives dictionary).
   ~~~~
   current = ["basketball", "soccer", "volleyball", "gymnastics", "wrestling", "golf", "equestrian", "swimming", "diving"]

   sport_counts = {"equestrian": 30, "tug of war": 3, "soccer": 15, "basketball": 8, "polo": 20, "swimming": 32, "gymnastics": 20, "diving": 24, "cricket": 12, "volleyball": 11, "croquet": 9}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(sport_counts.items()), sorted([("equestrian", 31), ("tug of war", 3), ("soccer", 16), ("basketball", 9), ("polo", 20), ("swimming", 33), ("gymnastics", 21), ("diving", 25), ("cricket", 12), ("volleyball", 12), ("croquet", 9)]), "Testing that sport_counts has been updated correctly.")

   myTests().main()


.. activecode:: ee_ch12_052
   :tags:Dictionaries/Dictionaryoperations.rst

   We have a dictionary of synchronized swimming moves called ``sswim_moves``, with the move names as keys and the amount of times they are used as the values. We also have a list of some moves that have not been added yet. Go through the list, called ``moves_to_add``, and if the move is in ``sswim_moves``, then update the value by 1. Otherwise, do nothing. 
   ~~~~
   sswim_moves = {'sculls': 23, 'sailboat': 12, 'back layout': 9, 'The Oyster': 8}
   moves_to_add = ['sculls', 'The Oyster' 'eggbeaters', 'eggbeaters', 'back layout', 'sculls', 'sailboat', 'The Oyster', 'The Water Wheel', 'sculls']

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(sswim_moves.items()), sorted([('sculls', 26), ('sailboat', 13), ('back layout', 10), ('The Oyster', 9)]), "Testing that sswim_moves was updated correctly.")        

   myTests().main()