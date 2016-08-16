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

1. At the halfway point during the Rio Olympics, the United States had 70 medals, Great Britain had 38 medals, China had 45 medals, Russia had 30 medals, and Germany had 17 medals. Create a dictionary assigned to the variable ``medal_count`` with the country names as the keys and the number of medals the country had as each key's value. 

.. activecode:: ee_ch12_01
   :tags:Dictionaries/intro-Dictionaries.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(medal_count.items()), sorted([('China', 45), ('Germany', 17), ('Great Britain', 38), ('Russia', 30), ('United States', 70)]), "Testing that the medal_count dictionary has the correct key-value pairs")

   myTests().main()

1.1 Create a dictionary that keeps track of the USA's Olympic medal count. Each key of the dictionary should be the type of medal (gold, silver, or bronze) and each key's value should be the number of that type of medal the USA's won. Currently, the USA has 33 gold medals, 17 silver, and 12 bronze. Create a dictionary saved in the variable ``medals`` that reflects this information. 

.. activecode:: ee_ch12_011
   :tags:Dictionaries/intro-Dictionaries.rst


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(medals.items()), sorted([("gold", 33), ("silver", 17), ("bronze", 12)]), "Testing that medals is correct.")

   myTests().main()

1.2 You are keeping track of olympic medals for Italy in the 2016 Rio Summer Olympics! At the moment, Italy has 7 gold medals, 8 silver metals, and 6 bronze medals. Create a dictionary called ``olympics`` where the keys are the types of medals, and the values are the number of that type of medals that Italy has won so far. 

.. activecode:: ee_ch12_012
   :tags:Dictionaries/intro-Dictionaries.rst


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(olympics.items()), sorted([('gold', 7), ('silver', 8), ('bronze', 6)]), "Testing that olympics was created correctly.")     

   myTests().main()

2. Given the dictionary ``swimmers``, add an additional key-value pair to the dictionary with ``"Phelps"`` as the key and the integer ``23`` as the value. Do not rewrite the entire dictionary.

.. activecode:: ee_ch12_02
   :tags:Dictionaries/intro-Dictionaries.rst

   swimmers = {'Manuel':4, Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwo(self):
         self.assertEqual(sorted(swimmers.items()), sorted([('Adrian', 7), ('Dirado', 4), ('Manuel',4), ('Ledecky', 5), ('Lochte', 12), ('Phelps', 23)]), "Testing that swimmers is assigned to correct value.")

   myTests().main()

2.1 Every four years, the summer Olympics are held in a different country. Add a key-value pair to the dictionary ``places`` that reflects that the 2016 Olympics were held in Brazil. Do not rewrite the entire dictionary to do this! 

.. activecode:: ee_ch12_021
   :tags:Dictionaries/intro-Dictionaries.rst

   places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(places.items()), sorted([("Australia", 2000), ("Greece", 2004), ("China", 2008), ("England", 2012), ("Brazil", 2016)]), "Testing that places has been updated correctly.")

   myTests().main()

2.2 Add the string "hockey" as a key to the dictionary ``sports_periods`` and assign it the value of 3. Do not rewrite the entire dictionary.

.. activecode:: ee_ch12_022
   :tags:Dictionaries/intro-Dictionaries.rst

   sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(sports_periods.items()), sorted([('baseball', 9), ("basketball", 4), ('soccer', 4), ('cricket', 2), ('hockey', 3)]), "Testing that sports_period was created correctly.")


   myTests().main()


3. Update the value for "Phelps" in the dictionary ``swimmers`` to include his medals from the Rio Olympics by adding 5 to the current value (Phelps will now have 28 total medals). Do not rewrite the dictionary.

.. activecode:: ee_ch12_03
   :tags:Dictionaries/Dictionaryoperations.rst

   swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testThree(self):
         self.assertEqual(sorted(swimmers.items()), sorted([('Adrian', 7), ('Dirado', 4), ('Ledecky', 5), ('Lochte', 12), ('Phelps', 28), ('Manuel',4)]), "Testing that swimmers is assigned to correct values.")

   myTests().main()

3.1 The dictionary ``golds`` contains information about how many gold medals each country won in the 2016 Olympics. But today, Spain won 2 more gold medals. Update ``golds`` to reflect this information. 

.. activecode:: ee_ch12_031
   :tags:Dictionaries/Dictionaryoperations.rst

   golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(golds.items()), sorted([("Italy", 12), ("USA", 33), ("Brazil", 15), ("China", 27), ("Spain", 21), ("Canada", 22), ("Argentina", 8), ("England", 29)]), "Testing that golds has been updated correctly.")

   myTests().main()


4. The dictionary ``china_medals`` shows the events China has medaled in and the number of medals won. Create a list of only the keys from ``china_medals`` and save it in a variable called ``events``. Do not hard-code this.

.. activecode:: ee_ch12_04
   :tags:Dictionaries/Dictionarymethods.rst
      
   china_medals = {'weightlifting':7, 'diving':6, 'table tennis':4, 'shooting':7, 'swimming':6}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(sorted(events), sorted(['weightlifting', 'diving', 'table tennis', 'shooting', 'swimming']) , "Testing that events holds the correct list.")

   myTests().main()

4.1 Create a list of the countries that are in the dictionary ``golds``, and assign that list to the variable name ``countries``. Do not hard code this. 

.. activecode:: ee_ch12_041
   :tags:Dictionaries/Dictionarymethods.rst

   golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(countries), sorted(["Italy", "USA", "Brazil", "China", "Spain", "Canada", "Argentina", "England"]), "Testing that countries has been created correctly.")

   myTests().main()

4.2 We have a dictionary of the specific events that Italy has won medals in and the number of medals they have won for each event. Assign to the variable ``events`` a list of the keys from the dictionary ``medal_events``. Do not hard code this.

.. activecode:: ee_ch12_042
   :tags:Dictionaries/Dictionarymethods.rst

   medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(events), sorted(['Shooting', 'Fencing', 'Judo', 'Swimming', "Diving"]), "Testing that events was created correctly")   

   myTests().main()

5. **Challenge** The list ``performed`` contains diving moves that have been performed. The dictionary ``dives`` contains the moves and the number of times each move has been performed.  The list ``performed`` is a list of additional diving moves that have just been done. Write code to update the dictionary ``dives``, so that for each move in the list ``performed``, if the move is in the dictionary ``dives`` already, you should update the value in the dictionary by 1. If that move is not in the dictionary ``dives`` yet, add a new key-value pair to the dictionary to record that move.

.. activecode:: ee_ch12_05
   :tags:Dictionaries/Dictionaryoperations.rst

   performed = ['reverse tuck', 'forward 2 1/2 somersault pike', 'back dive', 'twist in pike']
      
   dives = {'twist in free': 1, 'back dive': 2, 'armstand reverse': 1, 'forward tuck':5, 'reverse tuck': 3}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFive(self):
         self.assertEqual(sorted(dives.items()), sorted([('forward tuck', 5), ('reverse tuck', 4), ('forward 2 1/2 somersault pike', 1), ('back dive', 3), ('twist in free', 1), ('armstand reverse', 1), ('twist in pike', 1)]), "Testing that dives has been updated correctly.")

   myTests().main()

5.1 **Challenge** The list ``current`` contains some of the sports that were played in the 2016 Olympics. The dictionary ``sport_counts`` contains some of the sports that have been played in prior Olympic meets, and how many Olympics they were played in. Iterate through each sport included in the dictionary ``sport_counts`` and update its value by 1 if it was played in 2016 (if it was not played in 2016, its value should not be changed, and you should not record sports that are not already recorded in the dives dictionary).

.. activecode:: ee_ch12_051
   :tags:Dictionaries/Dictionaryoperations.rst

   current = ["basketball", "soccer", "volleyball", "gymnastics", "wrestling", "golf", "equestrian", "swimming", "diving"]

   sport_counts = {"equestrian": 30, "tug of war": 3, "soccer": 15, "basketball": 8, "polo": 20, "swimming": 32, "gymnastics": 20, "diving": 24, "cricket": 12, "volleyball": 11, "croquet": 9}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(sport_counts.items()), sorted([("equestrian", 31), ("tug of war", 3), ("soccer", 16), ("basketball", 9), ("polo", 20), ("swimming", 33), ("gymnastics", 21), ("diving", 25), ("cricket", 12), ("volleyball", 12), ("croquet", 9)]), "Testing that sport_counts has been updated correctly.")

   myTests().main()

5.2 **Challenge:** We have a dictionary of synchronized swimming moves called ``sswim_moves``, with the move names as keys and the amount of times they are used as the values. We also have a list of some moves that have not been added yet. Go through the list, called ``moves_to_add``, and if the move is in ``sswim_moves``, then update the value by 1. Otherwise, do nothing. 

.. activecode:: ee_ch12_052
   :tags:Dictionaries/Dictionaryoperations.rst

   sswim_moves = {'sculls': 23, 'sailboat': 12, 'back layout': 9, 'The Oyster': 8}
   moves_to_add = ['sculls', 'The Oyster' 'eggbeaters', 'eggbeaters', 'back layout', 'sculls', 'sailboat', 'The Oyster', 'The Water Wheel', 'sculls']

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(sswim_moves.items()), sorted([('sculls', 26), ('sailboat', 13), ('back layout', 10), ('The Oyster', 9)]), "Testing that sswim_moves was updated correctly.")        

   myTests().main()

6. Provided is the dictionary, ``medal_count``, which lists countries and their respective medal count at the halfway point in the 2016 Rio Olympics. Using dictionary mechanics, assign the medal count value for ``"Belarus"`` to the variable ``belarus``. Do not hardcode this.

.. activecode:: ee_ch12_06
   :tags:Dictionaries/Dictionarymethods.rst

   medal_count = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testSix(self):
         self.assertEqual(belarus, 4, "Testing that belarus is assigned the correct value.")

   myTests().main()


6.1 The dictionary ``total_golds`` contains the total number of gold medals that countries have won over the course of history. Use a dictionary method to find the number of golds Chile has won, and assign that number to the variable name ``chile_golds``. Do not hard code this!  

.. activecode:: ee_ch12_061
   :tags:Dictionaries/Dictionarymethods.rst

   total_golds = {"Italy": 114, "Germany": 782, "Pakistan": 10, "Sweden": 627, "USA": 2681, "Zimbabwe": 8, "Greece": 111, "Mongolia": 24, "Brazil": 108, "Croatia": 34, "Algeria": 15, "Switzerland": 323, "Yugoslavia": 87, "China": 526, "Egypt": 26, "Norway": 477, "Spain": 133, "Australia": 480, "Slovakia": 29, "Canada": 22, "New Zealand": 100, "Denmark": 180, "Chile": 13, "Argentina": 70, "Thailand": 24, "Cuba": 209, "Uganda": 7,  "England": 806, "Denmark": 180, "Ukraine": 122, "Bahamas": 12}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(chile_golds, 13, "Testing that chile_golds has been set correctly.")

   myTests().main()

6.2 Provided is a dictionary called ``US_medals`` which has the first 70 metals that the United States has won in 2016, and in which category they have won it in. Using dictionary mechanics, assign the value of the key ``''Fencing''`` to a variable ``fencing_value``. Remember, do not hard code this.

.. activecode:: ee_ch12_062
   :tags:Dictionaries/Dictionarymethods.rst

   US_medals = {"Swimming": 33, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3, "Cycling - Road": 1, "Fencing": 4, "Diving": 2, "Archery": 2, "Cycling - Track": 1, "Equestrian": 2, "Golf": 1, "Weightlifting": 1}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(fencing_value, US_medals.get("Fencing"), "Testing that fencing_value was created correctly.")
         

   myTests().main()
