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


.. activecode:: ee_Ch09_01
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Tuples/Tuples
      
   **1.** Create a tuple called ``olympics`` with four elements: "Beijing", "London", "Rio", "Tokyo".
   ~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(olympics, ('Beijing', 'London', 'Rio', 'Tokyo'), "Testing that olympics is assigned to correct values")

   myTests().main()


.. activecode:: ee_ch09_011
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Tuples/Tuples

   **1.1** Create a tuple called ``practice`` that has four elements: 'y', 'h', 'z', and 'x'.
   ~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(practice, ('y','h','z','x'), "Testing that pratice value is assigned to correct value.")

   myTests().main()


.. activecode:: ee_ch09_012
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Tuples/Tuples

   **1.2** Create a tuple named ``tup1`` that has three elements: 'a', 'b', and 'c'.
   ~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(tup1, ('a', 'b', 'c'), "Testing that tup1 was created correctly.")

   myTests().main()


.. activecode:: ee_ch09_02
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Tuples/Tuples

   **2.** The list below, `tuples_lst`, is a list of tuples. Create a list of the second elements of each tuple and assign this list to the variable ``country``.
   ~~~~

   tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwo(self):
         self.assertEqual(country, ['China', 'England', 'Brazil', 'Japan'], "Testing that third is assigned to correct values")

   myTests().main()


.. activecode:: ee_ch09_021
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Tuples/Tuples

   **2.1** Provided is a list of tuples. Create another list called ``t_check`` that contains the third element of every tuple.
   ~~~~

   lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(t_check, ['Zaptos', 'Charizard', 'Diglett', 'Tauros', 'Lanturn', 'Wailord'], "Testing that pratice value is assigned to correct value.")

   myTests().main()


.. activecode:: ee_ch09_022
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Tuples/Tuples

   **2.2** Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called ``seconds``.
   ~~~~

   tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(seconds, ['b', 7, 'green', 9.99, 'chipmunk'], "Testing that seconds was created correctly.")

   myTests().main()


.. activecode:: ee_ch09_03
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Tuples/TupleAssignmentwithunpacking

   **3.** With only one line of code, assign the variables ``city``, ``country``, and ``year`` to the values of the tuple ``olymp``.
   ~~~~

   olymp = ('Rio', 'Brazil', 2016)
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testThree(self):
         self.assertEqual(city, "Rio", "Testing that city is assigned to correct value.")
         self.assertEqual(country, "Brazil", "Testing that country is assigned to correct value.")
         self.assertEqual(year, 2016, "Testing that year is assigned to correct value.")

   myTests().main()


.. activecode:: ee_ch09_031
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Tuples/TupleAssignmentwithunpacking

   **3.1** With only one line of code, assign the variables water, fire, electric, and grass to the values "Squirtle", "Charmander", "Pikachu", and "Bulbasaur"
   ~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(water, "Squirtle", "Testing that water is assigned to the correct value.")
         self.assertEqual(fire, "Charmander", "Testing that fire is assigned to the correct value.")
         self.assertEqual(electric, "Pikachu", "Testing that electric is assigned to the correct value.")
         self.assertEqual(grass, "Bulbasaur", "Testing that grass is assigned to the correct value.")

   myTests().main()


.. activecode:: ee_ch09_032
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Tuples/TupleAssignmentwithunpacking

   **3.2** With only one line of code, assign four variables, ``v1``, ``v2``, ``v3``, and ``v4``, to the following four values: 1, 2, 3, 4.
   ~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(v1, 1, "Testing that v1 was assigned correctly.")
         self.assertEqual(v2, 2, "Testing that v2 was assigned correctly.")
         self.assertEqual(v3, 3, "Testing that v3 was assigned correctly.")
         self.assertEqual(v4, 4, "Testing that v4 was assigned correctly.")

   myTests().main()


.. activecode:: ee_ch09_04
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Tuples/TuplesasReturnValues

   **4.** Define a function called ``info`` with five parameters: name, gender, age, bday_month, and hometown. The function should then return a tuple with all five parameters in that order.
   ~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(info("Sue", "Female", 20, "March", "Ann Arbor"), ("Sue", "Female", 20, "March", "Ann Arbor"), "Testing that info('Sue', 'Female', 20, 'March', 'Ann Arbor') returns('Sue', 'Female', 20, 'March', 'Ann Arbor')")

   myTests().main()


.. activecode:: ee_ch09_041
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Tuples/TuplesasReturnValues

   **4.1** Define a function called ``information`` that takes as input, the variables ``name``, ``birth_year``, ``fav_color``, and ``hometown``. It should return a tuple of these variables in this order.
   ~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(information("Lauren", 1996, "purple", "St. Louis"), ("Lauren", 1996, "purple", "St. Louis"), "Testing that information returns the correct tuple on input ('Lauren', 1996, 'purple', 'St. Louis')")

   myTests().main()


.. activecode:: ee_ch09_042
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Tuples/TuplesasReturnValues

   **4.2** Define a function called ``info`` with the following required parameters: ``name``, ``age``, ``birth_year``, ``year_in_college``, and ``hometown``. The function should return a tuple that contains all the inputted information.
   ~~~~

   def info():

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(info(name='Tina', age=20, birth_year=1996, year_in_college='sophomore', hometown='Detroit'), ('Tina', 20, 1996, 'sophomore', 'Detroit'), "Testing the function info on input: name='Tina', age=20, birth_year=1996, year_in_college='sophomore', hometown='Detroit'.")

   myTests().main()


.. activecode:: ee_ch09_05
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Tuples/UnpackingDictionaryItems

   **5.** Given is the dictionary, ``gold``, which shows the country and the number of gold medals they have earned so far in the 2016 Olympics. Create a list, ``num_medals``, that contains only the number of medals for each country. Note: The .items() method provides a list of tuples. Do not use .keys() method.
   ~~~~

   gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFive(self):
         self.assertEqual(sorted(num_medals), sorted([31, 19, 19, 13, 12, 10, 8, 8]), "Testing that num_medals is assigned to correct values.")

   myTests().main()


.. activecode:: ee_ch09_051
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Tuples/UnpackingDictionaryItems

   **5.1** If you remember, the .items() dictionary method produces a list of tuples. Keeping this in mind, we have provided you a dictionary called ``pokemon``. For every key value pair, append the key to the list ``p_names``, and append the value to the list ``p_number``. Do not use the .keys() or .values() methods.
   ~~~~

   pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(p_names), sorted(['Rattata', 'Machop', 'Seel', 'Volbeat', 'Solrock']), "Testing that p_name has the correct values")
      def testTwo(self):
         self.assertEqual(sorted(p_number), sorted([19,66,86,86,126]), "Testing that p_number hsa the correct values")

   myTests().main()


.. activecode:: ee_ch09_052
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: Tuples/UnpackingDictionaryItems

   **5.2** The .items() method produces a list of key-value pair tuples. With this in mind, write code to create a list of keys from the dictionary ``track_medal_counts`` and assign the list to the variable name ``track_events``. Do **NOT** use the .keys() method.
   ~~~~

   track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(track_events), sorted(['shot put', 'long jump', '100 meters', '400 meters', '100 meter hurdles', 'triple jump', 'steeplechase', '1500 meters', '5K', '10K', 'marathon', '200 meters', '400 meter hurdles', 'high jump']) , "Testing that track_events was created correctly.")

   myTests().main()

