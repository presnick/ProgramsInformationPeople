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

1. The dictionary ``courses`` shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of credits taken this semester and assign it to the variable ``credits``. Do not hardcode this -- use dictionary accumulation!

.. activecode:: ee_ch13_01
   :tags: DictionaryAccumulation/AccumulatingResultsFromaDictionary.rst

   courses = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(credits, 18, "Testing that credits is assigned to correct values")

   myTests().main()

1.1 The dictionary ``travel`` contains the number of countries within each continent that Jackie has traveled to. Find the total number of countries that Jackie has been to, and save this number to the variable name ``total``. Do not hard code this!

.. activecode:: ee_ch13_011
   :tags: DictionaryAccumulation/AccumulatingResultsFromaDictionary.rst

   travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(total, 19, "Testing that total is correct.")

   myTests().main()

1.2 ``schedule`` is a dictionary where a class name is a key and its value is how many credits it was worth. Go through and accumulate the total number of credits that have been earned so far and assign that to the variable ``total_credits``. Do not hardcode.

.. activecode:: ee_ch13_012
   :tags: DictionaryAccumulation/AccumulatingResultsFromaDictionary.rst

   schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(total_credits, 63, "Testing that total_credits has the correct value.")

   myTests().main()

2. Create a dictionary, ``freq``, that displays each letter in string ``str1`` as the key and its frequency as the value.

.. activecode:: ee_ch13_02
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst

   str1 = "peter piper picked a peck of pickled peppers"
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwo(self):
         self.assertEqual(sorted(freq.items()), sorted([(' ', 7), ('a', 1), ('c', 3), ('d', 2), ('e', 8), ('f', 1), ('i', 3), ('k', 3), ('l', 1), ('o', 1), ('p', 9), ('r', 3), ('s', 1), ('t', 1)]), "Testing that freq is correct.")

   myTests().main()

2.1 Provided is a string saved to the variable name ``s1``. Create a dictionary named ``counts`` that contains each letter in ``s1`` and the number of times it occurs.

.. activecode:: ee_ch13_021
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst

   s1 = "hello"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(counts.items()), [('e', 1), ('h', 1), ('l', 2), ('o', 1)], "Testing that counts was created correctly.")

   myTests().main()

2.2 Create a dictionary called ``char_d`` from the string ``stri``, so that the key is a character and the value is how many times you see it.

.. activecode:: ee_ch13_022
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst

   stri = "what can I do"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(char_d.items()), sorted([('w', 1), ('h', 1), ('a', 2), ('t', 1), (' ', 3), ('c', 1), ('n', 1), ('I', 1), ('d', 1), ('o', 1)]), "Testing that char_d has been created correctly.")

   myTests().main()

3. Create a dictionary, ``freq_words``, that displays each word in string ``str1`` as the key and its frequency as the value.

.. activecode:: ee_ch13_03
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst

   str1 = "I wish, I wish, with all my heart, to fly with dragons, in a land apart"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testThree(self):
         self.assertEqual(sorted(freq_words.items()), sorted([('a', 1), ('I', 2), ('wish,', 2), ('with', 2), ('all', 1), ('my', 1), ('heart,', 1), ('to', 1), ('fly', 1), ('dragons,', 1), ('in', 1), ('land', 1), ('apart', 1)]), "Testing that freq_words was created correctly.")

   myTests().main()

3.1 Provided is a string saved to the variable name ``sentence``. Split the string into a list of words, then create a dictionary that contains each word and the number of times it occurs. Save this dictionary to the variable name ``word_counts``.

.. activecode:: ee_ch13_031
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst

   sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(word_counts.items()), sorted([('The', 1), ('dog', 1), ('chased', 1), ('the', 3), ('rabbit', 2), ('into', 1), ('forest', 1), ('but', 1), ('was', 1), ('too', 1), ('quick.', 1)]), "Testing that word_counts was created correctly.")

   myTests().main()

3.2 Create a dictionary called ``wrd_d`` from the string ``sent``, so that the key is a word and the value is how many times you have seen that word. Don't worry about punctuation or capitalization in this problem.

.. activecode:: ee_ch13_032
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst

   sent = "Singing in the rain and playing in the rain are two entirely different situations, but both can be good."

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(wrd_d.items()), sorted([('Singing', 1), ('in', 2), ('the', 2), ('rain', 2), ('and', 1), ('playing', 1), ('are', 1), ('two', 1), ('entirely', 1), ('different', 1), ('situations,', 1), ('but', 1), ('both', 1), ('can', 1), ('be', 1), ('good.', 1)]), "Testing that wrd_d has been created correctly.")

   myTests().main()

4. Create the dictionary ``characters`` that shows each character from the string ``sally`` and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable ``best_char``.

.. activecode:: ee_ch13_04
   :tags: DictionaryAccumulation/AccumulatingtheBestKey.rst, DictionaryAccumulation/AccumulatingaMaximumValue.rst

   sally = "sally sells sea shells by the sea shore"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFourA(self):
         self.assertEqual(sorted(characters.items()), sorted([('s', 8), ('o', 1), ('e', 6), ('t', 1), ('h', 3), ('a', 3), ('r', 1), ('l', 6), ('y', 2), (' ', 7), ('b', 1)]), "Testing that characters has correct values." )

      def testFourB(self):
         self.assertEqual(best_char, "s", "Testing that best_char is assigned to correct value.")

   myTests().main()

4.1 Create a dictionary called ``lett_d`` that keeps track of all of the characters in the string ``product`` and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to ``max_value``.

.. activecode:: ee_ch13_042
   :tags: DictionaryAccumulation/AccumulatingaMaximumValue.rst, DictionaryAccumulation/AccumulatingtheBestKey.rst

   product = "iphone and android phones"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(lett_d.items()), sorted([('h', 2), ('a', 2), (' ', 3), ('n', 4), ('d', 3), ('o', 3), ('i', 2), ('p', 2), ('e', 2), ('r', 1), ('s', 1)]), "Testing that lett_d has been created correctly.")
      def testTwo(self):
         self.assertEqual(max_value, "n", "Testing that max_value has been correctly assigned")


   myTests().main()

5. Do the same as above but now find the least frequent letter. Create the dictionary ``characters`` that shows each character from string ``sally`` and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable ``worst_char``.

.. activecode:: ee_ch13_05
   :tags: DictionaryAccumulation/AccumulatingtheBestKey.rst, DictionaryAccumulation/AccumulatingaMaximumValue.rst

   sally = "sally sells sea shells by the sea shore and by the road"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFiveA(self):
         self.assertEqual(sorted(characters.items()), sorted([('s', 8), ('a', 5), ('l', 6), ('y', 3), (' ', 11), ('e', 7), ('h', 4), ('b', 2), ('t', 2), ('o', 2), ('r', 2), ('n', 1), ('d', 2)]), "Testing that characters has been updated correctly.")

      def testFourB(self):
         self.assertEqual(worst_char, "n", "Testing that worst_char is assigned to correct value.")

   myTests().main()

5.2 Create a dictionary called ``d`` that keeps track of all the characters in the string ``placement`` and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to ``min_value``.

.. activecode:: ee_ch13_052
   :tags: DictionaryAccumulation/AccumulatingaMaximumValue.rst, DictionaryAccumulation/AccumulatingtheBestKey.rst

   placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(d.keys()), sorted(['B', 'e', 'a', 'c', 'h', 's', ' ', 'r', 'o', 'l', 'p', 't', 'v', 'i', 'n', 'g', 'w', 'M', 'k', 'd', '.', 'x']), "Testing the keys were created correctly")
         self.assertEqual(sorted(d.values()), sorted([2, 17, 12, 8, 4, 10, 27, 7, 10, 8, 6, 8, 3, 13, 7, 2, 3, 3, 2, 2, 2, 1]), "Testing the values were created correctly")
      def testTwo(self):
         self.assertEqual(min_value, "x", "Testing that min_value has been correctly assigned")


   myTests().main()

6.1 Create a dictionary named ``letter_counts`` that contains each letter and the number of times it occurs in ``string1``. **Challenge:** Letters should not be counted separately as upper-case and lower-case.

.. activecode:: ee_ch13_061
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst

   string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(letter_counts['t'], 19, "Testing that the letter 't' has the correct value.")

      def testTwo(self):
         self.assertEqual(letter_counts['w'], 6, "Testing that the letter 'w' has the correct value.")

      def testThree(self):
         self.assertEqual(letter_counts['o'], 17, "Testing that the letter 'o' has the correct value.")

      def testFour(self):
         self.assertEqual(letter_counts['a'], 17, "Testing that the letter 'a' has the correct value.")



   myTests().main()


6.2 Create a dictionary called ``low_d`` that keeps track of all the characters in the string ``p`` and notes how many times each character was seen. Make sure that there are no repeats of characters as keys, such that "T" and "t" are both seen as a "t" for example.

.. activecode:: ee_ch13_062
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst

   p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(low_d["s"], 5, "Testing the key s")
      def testThree(self):
         self.assertEqual(low_d["y"], 1, "Testing the key y")


   myTests().main()


7.1 The string ``state_data`` contains a specially formatted string that contains population information for various states. Every state is on a different line. There are four "columns": state name, abbreviation, region, and population. Every column is separated by a comma. Use a ``for`` loop to loop through every line of ``state_data`` and print out each line.

Hint: use ``.split('\n')`` to split the lines of ``state_data`` into a list.

.. activecode:: ee_ch13_071
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst

   # COLUMNS:
   # 0: state name
   # 1: state abbreviation
   # 2: region
   # 3: population

   state_data = """Alabama,         AL,     South,   4849377
      Alaska,          AK,      West,    736732
      Arizona,         AZ,      West,   6731484
      Arkansas,        AR,     South,   2966369
      California,      CA,      West,  38802500
      Colorado,        CO,      West,   5355866
      Connecticut,     CT, Northeast,   3596677
      Delaware,        DE,     South,    935614
      Florida,         FL,     South,  19893297
      Georgia,         GA,     South,  10097343
      Hawaii,          HI,      West,   1419561
      Idaho,           ID,      West,   1634464
      Illinois,        IL,   Midwest,  12880580
      Indiana,         IN,   Midwest,   6596855
      Iowa,            IA,   Midwest,   3107126
      Kansas,          KS,   Midwest,   2904021
      Kentucky,        KY,     South,   4413457
      Louisiana,       LA,     South,   4649676
      Maine,           ME, Northeast,   1330089
      Maryland,        MD,     South,   5976407
      Massachusetts,   MA, Northeast,   6745408
      Michigan,        MI,   Midwest,   9909877
      Minnesota,       MN,   Midwest,   5457173
      Mississippi,     MS,     South,   2994079
      Missouri,        MO,   Midwest,   6063589
      Montana,         MT,      West,   1023579
      Nebraska,        NE,   Midwest,   1881503
      Nevada,          NV,      West,   2839099
      New Hampshire,   NH, Northeast,   1326813
      New Jersey,      NJ, Northeast,   8938175
      New Mexico,      NM,      West,   2085572
      New York,        NY, Northeast,  19746227
      North Carolina,  NC,     South,   9943964
      North Dakota,    ND,   Midwest,    739482
      Ohio,            OH,   Midwest,  11594163
      Oklahoma,        OK,     South,   3878051
      Oregon,          OR,      West,   3970239
      Pennsylvania,    PA, Northeast,  12787209
      Rhode Island,    RI, Northeast,   1055173
      South Carolina,  SC,     South,   4832482
      South Dakota,    SD,   Midwest,    853175
      Tennessee,       TN,     South,   6549352
      Texas,           TX,     South,  26956958
      Utah,            UT,      West,   2942902
      Vermont,         VT, Northeast,    626562
      Virginia,        VA,     South,   8326289
      Washington,      WA,      West,   7061530
      West Virginia,   WV,     South,   1850326
      Wisconsin,       WI,   Midwest,   5757564
      Wyoming,         WY,      West,    584153"""

   # COLUMNS:
   # 0: state name
   # 1: state abbreviation
   # 2: region
   # 3: population



   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
      def testOne(self):
         self.assertIn("Michigan,        MI,   Midwest,   9909877", self.getOutput(), "Testing output (Don't worry about actual and expected values).")

      def testOneA(self):
         self.assertIn('for', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")

   myTests().main()

7.2 We have ``state_data`` from before, but this time for every state, only print the state abbreviation (**MI** for Michigan). You may use your code from the previous problem. Your output should contain "AL" on one line, "AK" on the next, etc.

Hint: use ``.split(',')`` to split a given line of ``state_data`` by commas. You may use ``.strip()`` on any string to remove left and right whitespace.

.. activecode:: ee_ch13_072
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst

   # COLUMNS:
   # 0: state name
   # 1: state abbreviation
   # 2: region
   # 3: population

   state_data = """Alabama,         AL,     South,   4849377
      Alaska,          AK,      West,    736732
      Arizona,         AZ,      West,   6731484
      Arkansas,        AR,     South,   2966369
      California,      CA,      West,  38802500
      Colorado,        CO,      West,   5355866
      Connecticut,     CT, Northeast,   3596677
      Delaware,        DE,     South,    935614
      Florida,         FL,     South,  19893297
      Georgia,         GA,     South,  10097343
      Hawaii,          HI,      West,   1419561
      Idaho,           ID,      West,   1634464
      Illinois,        IL,   Midwest,  12880580
      Indiana,         IN,   Midwest,   6596855
      Iowa,            IA,   Midwest,   3107126
      Kansas,          KS,   Midwest,   2904021
      Kentucky,        KY,     South,   4413457
      Louisiana,       LA,     South,   4649676
      Maine,           ME, Northeast,   1330089
      Maryland,        MD,     South,   5976407
      Massachusetts,   MA, Northeast,   6745408
      Michigan,        MI,   Midwest,   9909877
      Minnesota,       MN,   Midwest,   5457173
      Mississippi,     MS,     South,   2994079
      Missouri,        MO,   Midwest,   6063589
      Montana,         MT,      West,   1023579
      Nebraska,        NE,   Midwest,   1881503
      Nevada,          NV,      West,   2839099
      New Hampshire,   NH, Northeast,   1326813
      New Jersey,      NJ, Northeast,   8938175
      New Mexico,      NM,      West,   2085572
      New York,        NY, Northeast,  19746227
      North Carolina,  NC,     South,   9943964
      North Dakota,    ND,   Midwest,    739482
      Ohio,            OH,   Midwest,  11594163
      Oklahoma,        OK,     South,   3878051
      Oregon,          OR,      West,   3970239
      Pennsylvania,    PA, Northeast,  12787209
      Rhode Island,    RI, Northeast,   1055173
      South Carolina,  SC,     South,   4832482
      South Dakota,    SD,   Midwest,    853175
      Tennessee,       TN,     South,   6549352
      Texas,           TX,     South,  26956958
      Utah,            UT,      West,   2942902
      Vermont,         VT, Northeast,    626562
      Virginia,        VA,     South,   8326289
      Washington,      WA,      West,   7061530
      West Virginia,   WV,     South,   1850326
      Wisconsin,       WI,   Midwest,   5757564
      Wyoming,         WY,      West,    584153"""

   # COLUMNS:
   # 0: state name
   # 1: state abbreviation
   # 2: region
   # 3: population



   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
      def testOne(self):
         self.assertIn("MI\n", self.getOutput(), "Testing output (Don't worry about actual and expected values).")

      def testOneA(self):
         self.assertIn('for', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")

   myTests().main()

7.3 We have ``state_data`` from before. This time, create a **dictionary** called ``state_abbreviations`` that maps state abbreviations to their names. For example, ``"MI"`` should be mapped to ``"Michigan"``.


.. activecode:: ee_ch13_073
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst

   state_data = """Alabama,AL,South,4849377
   Alaska,AK,West,736732
   Arizona,AZ,West,6731484
   Arkansas,AR,South,2966369
   California,CA,West,38802500
   Colorado,CO,West,5355866
   Connecticut,CT,Northeast,3596677
   Delaware,DE,South,935614
   Florida,FL,South,19893297
   Georgia,GA,South,10097343
   Hawaii,HI,West,1419561
   Idaho,ID,West,1634464
   Illinois,IL,Midwest,12880580
   Indiana,IN,Midwest,6596855
   Iowa,IA,Midwest,3107126
   Kansas,KS,Midwest,2904021
   Kentucky,KY,South,4413457
   Louisiana,LA,South,4649676
   Maine,ME,Northeast,1330089
   Maryland,MD,South,5976407
   Massachusetts,MA,Northeast,6745408
   Michigan,MI,Midwest,9909877
   Minnesota,MN,Midwest,5457173
   Mississippi,MS,South,2994079
   Missouri,MO,Midwest,6063589
   Montana,MT,West,1023579
   Nebraska,NE,Midwest,1881503
   Nevada,NV,West,2839099
   New Hampshire,NH,Northeast,1326813
   New Jersey,NJ,Northeast,8938175
   New Mexico,NM,West,2085572
   New York,NY,Northeast,19746227
   North Carolina,NC,South,9943964
   North Dakota,ND,Midwest,739482
   Ohio,OH,Midwest,11594163
   Oklahoma,OK,South,3878051
   Oregon,OR,West,3970239
   Pennsylvania,PA,Northeast,12787209
   Rhode Island,RI,Northeast,1055173
   South Carolina,SC,South,4832482
   South Dakota,SD,Midwest,853175
   Tennessee,TN,South,6549352
   Texas,TX,South,26956958
   Utah,UT,West,2942902
   Vermont,VT,Northeast,626562
   Virginia,VA,South,8326289
   Washington,WA,West,7061530
   West Virginia,WV,South,1850326
   Wisconsin,WI,Midwest,5757564
   Wyoming,WY,West,584153"""

   # COLUMNS:
   # 0: state name
   # 1: state abbreviation
   # 2: region
   # 3: population


   state_abbreviations = {}
   for line in state_data.split('\n'):
      cells = line.split(',')



   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
      def testOne(self):
         self.assertEqual(state_abbreviations['MI'], "Michigan", "Testing MI abbreviation")
         self.assertEqual(state_abbreviations['PA'], "Pennsylvania", "Testing PA abbreviation")
         self.assertEqual(state_abbreviations['MA'], "Massachusetts", "Testing MA abbreviation")

      def testOneA(self):
         self.assertIn('for', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")

   myTests().main()


7.4 We have ``state_data`` from before. This time, use **accumulation** to find the **least** populous state. Assign that state's name to the variable ``least_pop``.

Hint: You don't need to use a dictionary to do this.
Hint: Use ``int()`` to cast the population as an integer

.. activecode:: ee_ch13_074
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst


   state_data = """Alabama,AL,South,4849377
   Alaska,AK,West,736732
   Arizona,AZ,West,6731484
   Arkansas,AR,South,2966369
   California,CA,West,38802500
   Colorado,CO,West,5355866
   Connecticut,CT,Northeast,3596677
   Delaware,DE,South,935614
   Florida,FL,South,19893297
   Georgia,GA,South,10097343
   Hawaii,HI,West,1419561
   Idaho,ID,West,1634464
   Illinois,IL,Midwest,12880580
   Indiana,IN,Midwest,6596855
   Iowa,IA,Midwest,3107126
   Kansas,KS,Midwest,2904021
   Kentucky,KY,South,4413457
   Louisiana,LA,South,4649676
   Maine,ME,Northeast,1330089
   Maryland,MD,South,5976407
   Massachusetts,MA,Northeast,6745408
   Michigan,MI,Midwest,9909877
   Minnesota,MN,Midwest,5457173
   Mississippi,MS,South,2994079
   Missouri,MO,Midwest,6063589
   Montana,MT,West,1023579
   Nebraska,NE,Midwest,1881503
   Nevada,NV,West,2839099
   New Hampshire,NH,Northeast,1326813
   New Jersey,NJ,Northeast,8938175
   New Mexico,NM,West,2085572
   New York,NY,Northeast,19746227
   North Carolina,NC,South,9943964
   North Dakota,ND,Midwest,739482
   Ohio,OH,Midwest,11594163
   Oklahoma,OK,South,3878051
   Oregon,OR,West,3970239
   Pennsylvania,PA,Northeast,12787209
   Rhode Island,RI,Northeast,1055173
   South Carolina,SC,South,4832482
   South Dakota,SD,Midwest,853175
   Tennessee,TN,South,6549352
   Texas,TX,South,26956958
   Utah,UT,West,2942902
   Vermont,VT,Northeast,626562
   Virginia,VA,South,8326289
   Washington,WA,West,7061530
   West Virginia,WV,South,1850326
   Wisconsin,WI,Midwest,5757564
   Wyoming,WY,West,584153"""

   # COLUMNS:
   # 0: state name
   # 1: state abbreviation
   # 2: region
   # 3: population

   for line in state_data.split('\n'):
      cells = line.split(',')


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
      def testOne(self):
         self.assertEqual(least_pop, 'Wyoming')

      def testOneA(self):
         self.assertIn('for', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")

   myTests().main()

7.5 We have ``state_data`` from before. This time, use **dictionary accumulation** to create a dictionary called ``region_pop`` that maps *regions* (e.g. Midwest) to the total population for that region. Then, use the max accumulation pattern to find the **most** populous region and store it in ``high_region_pop``.

Hint: Use ``int()`` to cast strings to integers.

.. activecode:: ee_ch13_075
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst

   # COLUMNS:
   # 0: state name
   # 1: state abbreviation
   # 2: region
   # 3: population

   state_data = """Alabama,AL,South,4849377
   Alaska,AK,West,736732
   Arizona,AZ,West,6731484
   Arkansas,AR,South,2966369
   California,CA,West,38802500
   Colorado,CO,West,5355866
   Connecticut,CT,Northeast,3596677
   Delaware,DE,South,935614
   Florida,FL,South,19893297
   Georgia,GA,South,10097343
   Hawaii,HI,West,1419561
   Idaho,ID,West,1634464
   Illinois,IL,Midwest,12880580
   Indiana,IN,Midwest,6596855
   Iowa,IA,Midwest,3107126
   Kansas,KS,Midwest,2904021
   Kentucky,KY,South,4413457
   Louisiana,LA,South,4649676
   Maine,ME,Northeast,1330089
   Maryland,MD,South,5976407
   Massachusetts,MA,Northeast,6745408
   Michigan,MI,Midwest,9909877
   Minnesota,MN,Midwest,5457173
   Mississippi,MS,South,2994079
   Missouri,MO,Midwest,6063589
   Montana,MT,West,1023579
   Nebraska,NE,Midwest,1881503
   Nevada,NV,West,2839099
   New Hampshire,NH,Northeast,1326813
   New Jersey,NJ,Northeast,8938175
   New Mexico,NM,West,2085572
   New York,NY,Northeast,19746227
   North Carolina,NC,South,9943964
   North Dakota,ND,Midwest,739482
   Ohio,OH,Midwest,11594163
   Oklahoma,OK,South,3878051
   Oregon,OR,West,3970239
   Pennsylvania,PA,Northeast,12787209
   Rhode Island,RI,Northeast,1055173
   South Carolina,SC,South,4832482
   South Dakota,SD,Midwest,853175
   Tennessee,TN,South,6549352
   Texas,TX,South,26956958
   Utah,UT,West,2942902
   Vermont,VT,Northeast,626562
   Virginia,VA,South,8326289
   Washington,WA,West,7061530
   West Virginia,WV,South,1850326
   Wisconsin,WI,Midwest,5757564
   Wyoming,WY,West,584153"""

   # COLUMNS:
   # 0: state name
   # 1: state abbreviation
   # 2: region
   # 3: population

   region_pop = {}

   for line in state_data.split('\n'):
      cells = line.split(',')

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
      def testOne(self):
         answer = {'South': 119113041, 'West': 75187681, 'Northeast': 56152333, 'Midwest': 67745108}
         self.assertEqual(sorted(region_pop.values()), sorted(answer.values()), "Checking values")
         self.assertEqual(sorted(region_pop.keys()), sorted(answer.keys()), "Checking values")
         self.assertEqual(high_region_pop, "South", "Checking high_region_pop")

      def testOneA(self):
         self.assertIn('for', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")

   myTests().main()

7.6 We have ``state_data`` from before. Assign ``most_pop_midwest`` to the name of the state whose region is ``"Midwest"`` with the highest population.

.. activecode:: ee_ch13_076
   :tags: DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary.rst

   # COLUMNS:
   # 0: state name
   # 1: state abbreviation
   # 2: region
   # 3: population

   state_data = """Alabama,AL,South,4849377
   Alaska,AK,West,736732
   Arizona,AZ,West,6731484
   Arkansas,AR,South,2966369
   California,CA,West,38802500
   Colorado,CO,West,5355866
   Connecticut,CT,Northeast,3596677
   Delaware,DE,South,935614
   Florida,FL,South,19893297
   Georgia,GA,South,10097343
   Hawaii,HI,West,1419561
   Idaho,ID,West,1634464
   Illinois,IL,Midwest,12880580
   Indiana,IN,Midwest,6596855
   Iowa,IA,Midwest,3107126
   Kansas,KS,Midwest,2904021
   Kentucky,KY,South,4413457
   Louisiana,LA,South,4649676
   Maine,ME,Northeast,1330089
   Maryland,MD,South,5976407
   Massachusetts,MA,Northeast,6745408
   Michigan,MI,Midwest,9909877
   Minnesota,MN,Midwest,5457173
   Mississippi,MS,South,2994079
   Missouri,MO,Midwest,6063589
   Montana,MT,West,1023579
   Nebraska,NE,Midwest,1881503
   Nevada,NV,West,2839099
   New Hampshire,NH,Northeast,1326813
   New Jersey,NJ,Northeast,8938175
   New Mexico,NM,West,2085572
   New York,NY,Northeast,19746227
   North Carolina,NC,South,9943964
   North Dakota,ND,Midwest,739482
   Ohio,OH,Midwest,11594163
   Oklahoma,OK,South,3878051
   Oregon,OR,West,3970239
   Pennsylvania,PA,Northeast,12787209
   Rhode Island,RI,Northeast,1055173
   South Carolina,SC,South,4832482
   South Dakota,SD,Midwest,853175
   Tennessee,TN,South,6549352
   Texas,TX,South,26956958
   Utah,UT,West,2942902
   Vermont,VT,Northeast,626562
   Virginia,VA,South,8326289
   Washington,WA,West,7061530
   West Virginia,WV,South,1850326
   Wisconsin,WI,Midwest,5757564
   Wyoming,WY,West,584153"""

   for line in state_data.split('\n'):
      cells = line.split(',')

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
      def testOne(self):
         self.assertEqual(most_pop_midwest, "Illinois", "Checking most_pop_midwest")

      def testOneA(self):
         self.assertIn('for', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")

   myTests().main()