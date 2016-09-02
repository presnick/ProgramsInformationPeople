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

1. Sort the following string alphabetically, from z to a and assign it to the variable ``sorted_letters``.

.. activecode:: ee_sort_01
   :tags: Sort/Optionalkeyparameter.rst, Sort/Optionalreverseparameter.rst, Sort/intro-SortingwithSortandSorted.rst

   letters = "alwnfiwaksuezlaeiajsdl"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted_letters, sorted(letters, reverse = True), "Testing that sorted_letters has the correct value.")

   myTests().main()

1.1 Sort the list, ``lst``, from largest to smallest. Save this new list to the variable ``lst_sorted``.

.. activecode:: ee_sort_011
   :tags: Sort/intro-SortingwithSortandSorted.rst, Sort/Optionalkeyparameter.rst, Sort/Optionalreverseparameter.rst, 

   lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(lst_sorted, sorted(lst, reverse = True), "Testing that lst_sorted value is assigned to correct values.")

   myTests().main()

1.2 Sort the list below, ``animals``, into alphabetical order. Save the new list as ``animals_sorted``. 

.. activecode:: ee_sort_012
   :tags: Sort/intro-SortingwithSortandSorted.rst

   animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(animals_sorted, ['antelope', 'bear', 'cat', 'cow', 'deer', 'elephant', 'elk', 'giraffe', 'goat', 'minx', 'moose', 'otter', 'rabbit', 'salamander', 'tiger', 'yak', 'zebra'], "Testing that animals_sorted was created correctly.")

   myTests().main()

2. The dictionary, ``medals``, shows the medal count for six countries during the Rio Olympics. Sort the country names so they appear alphabetically. Save this list to the variable ``alphabetical``.

.. activecode:: ee_sort_02
   :tags: Sort/SortingaDictionary.rst, Sort/intro-SortingwithSortandSorted.rst
  
   medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwo(self):
         self.assertEqual(alphabetical, sorted(medals.keys()), "Testing that alphabetical value is assigned to correct values.")

   myTests().main()

2.1 Sort the following dictionary based on the keys so that they are sorted a to z. Assign the resulting value to the variable ``sorted_keys``.

.. activecode:: ee_sort_021
   :tags: Sort/SortingaDictionary.rst, Sort/intro-SortingwithSortandSorted.rst

   dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted_keys, sorted(dictionary), "Testing that sorted_keys has the correct value.")

   myTests().main()

2.2 Below, we have provided the dictionary ``groceries``, whose keys are grocery items, and values are the number of each item that you need to buy at the store. Sort the dictionary's keys into alphabetical order, and save them as a list called ``grocery_keys_sorted``. 

.. activecode:: ee_sort_022
   :tags: Sort/intro-SortingwithSortandSorted.rst, Sort/SortingaDictionary.rst

   groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(grocery_keys_sorted, ['apples', 'bananas', 'carrots', 'cereal', 'coffee', 'granola bars', 'onions', 'orange juice', 'pasta', 'peanut butter', 'popcorn', 'rice', 'salsa', 'spinach'], "Testing that grocery_keys_sorted was created correctly.")

   myTests().main()  

3. Given the same dictionary, ``medals``, now sort by the medal count. Save the three countries with the highest medal count to the list, ``top_three``. 

.. activecode:: ee_sort_03
   :tags: Sort/Anonymousfunctionswithlambdaexpressions.rst, Sort/SortingaDictionary.rst, Sort/Optionalkeyparameter.rst, Sort/Optionalreverseparameter.rst, Sort/intro-SortingwithSortandSorted.rst
   
   medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testThree(self):
         self.assertEqual(top_three, sorted(medals, key = lambda x: medals[x], reverse = True)[:3], "Testing that top_three value is assigned to correct values.")

   myTests().main()

3.1 Sort the following dictionary based on the value from highest to lowest. Assign the resulting value to the variable ``sorted_values``.

.. activecode:: ee_sort_031
   :tags: Sort/SortingaDictionary.rst, Sort/Optionalkeyparameter.rst, Sort/Optionalreverseparameter.rst, Sort/intro-SortingwithSortandSorted.rst

   dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted_values, sorted(dictionary, key = lambda x: dictionary[x], reverse = True), "Testing that sorted_values has the correct value.")

   myTests().main()

3.2 Once again, we have provided the dictionary ``groceries``. Once again, you should return a list of its keys, but this time they should be sorted by their values, from highest to lowest. Save the new list as ``most_needed``. 

.. activecode:: ee_sort_032
   :tags: Sort/intro-SortingwithSortandSorted.rst, Sort/SortingaDictionary.rst, Sort/Optionalreverseparameter.rst, Sort/Optionalkeyparameter.rst
 
   groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(most_needed, ['granola bars', 'carrots', 'spinach', 'bananas', 'onions', 'coffee', 'apples', 'cereal', 'salsa', 'pasta', 'peanut butter', 'orange juice', 'rice', 'popcorn'], "Testing that most_needed was created correctly.")

   myTests().main() 

4. Create a function called ``last_four`` that takes in an ID number and returns the last four digits. For example, the number 17573005 should return 3005. Then, use this function to sort the list of ids stored in the variable, ``ids``, from lowest to highest. Save this sorted list in the variable, ``sorted_ids``. Hint: Remember that only strings can be indexed, so conversions may be needed.

.. activecode:: ee_sort_04
   :tags:Sort/intro-SortingwithSortandSorted.rst
   
   def last_four(x):




   ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(sorted_ids, sorted(ids, key = last_four), "Testing that sorted_ids is assigned to correct values.")

   myTests().main()

4.1 Sort the following list by each element's second letter a to z. Do so by creating a function called ``second_let`` for the key. Assign the resulting value to the variable ``func_sort``.

.. activecode:: ee_sort_041
   :tags: Sort/intro-SortingwithSortandSorted.rst, Sort/Optionalkeyparameter.rst

   ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(func_sort, sorted(ex_lst, key = second_let), "Testing that func_sort has the correct value.")

   myTests().main()

4.2 Below, we have provided a list of strings called ``nums``. Write a function called ``last_char`` that takes a string as input, and returns only its last character. Use this function to sort the list ``nums`` by the last digit of each number, from highest to lowest, and save this as a new list called ``nums_sorted``. 

.. activecode:: ee_sort_042
   :tags: Sort/intro-SortingwithSortandSorted.rst, Sort/Optionalreverseparameter.rst, Sort/Optionalkeyparameter.rst

   nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

   def last_char(): 

   nums_sorted = 

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testA(self):
         self.assertEqual(nums_sorted, ['19', '14378', '8907', '16', '1005', '44', '33', '32', '871', '1450'], "Testing that nums_sorted was created correctly.")
      def testB(self): 
         self.assertEqual(last_char('pants'), 's', "Testing the function last_char on input 'pants'.")


   myTests().main() 

5. Sort the list ``ids`` by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable ``sorted_id``.

.. activecode:: ee_sort_05
   :tags: Sort/Anonymousfunctionswithlambdaexpressions.rst, Sort/intro-SortingwithSortandSorted.rst
      
   ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFive(self):
         self.assertEqual(sorted_id, [17570002, 17572342, 17572345, 17573005, 17579000, 17579329], "Testing that sorted_id is assigned to correct value.")

   myTests().main()

5.1 Sort the following list by each element's second letter a to z. Do so by using lambda. Assign the resulting value to the variable ``lambda_sort``.

.. activecode:: ee_sort_051
   :tags: Sort/Anonymousfunctionswithlambdaexpressions.rst, Sort/intro-SortingwithSortandSorted.rst

   ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(lambda_sort, sorted(ex_lst, key = lambda z: z[1]), "Testing that lambda_sort has the correct value.")

   myTests().main()

5.2 Once again, sort the list ``nums`` based on the last digit of each number from highest to lowest. However, now you should do so by writing a lambda function. Save the new list as ``nums_sorted_lambda``. 

.. activecode:: ee_sort_052
   :tags: Sort/intro-SortingwithSortandSorted.rst, Sort/Anonymousfunctionswithlambdaexpressions.rst, Sort/Optionalreverseparameter.rst

   nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

   nums_sorted_lambda = 

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testA(self):
         self.assertEqual(nums_sorted_lambda, ['19', '14378', '8907', '16', '1005', '44', '33', '32', '871', '1450'], "Testing that nums_sorted_lambda was created correctly.")


   myTests().main() 

6. **Challenge** Given is the nested dictionary, ``pokemon``, which shows the pokemon each trainer has caught in the early stages of Pokemon Go. Pool this data together in a dictionary assigned to the variable name, ``pooled``. The pooled dictionary should have the total number of rattatas, eevees, etc. Then, sort the compiled dictionary based on the number of pokemon from greatest number to least number to the variable ``sorted_pooled``. Assign the most common pokemon to the variable ``common``. 

.. activecode:: ee_sort_06
   :tags: Sort/SortingaDictionary.rst, Sort/Optionalkeyparameter.rst, Sort/Optionalreverseparameter.rst, Sort/Anonymousfunctionswithlambdaexpressions.rst, Sort/intro-SortingwithSortandSorted.rst
      
   pokemon = {'Trainer1':
                    {'rattatas':15, 'eevees': 2, 'ditto':1, 'magikarps':3, 'zubats':8, 'pidgey': 12}, 
               'Trainer2':
                    {'rattatas':25, 'eevees': 1, 'magikarps':7, 'zubats':3, 'pidgey': 15}, 
               'Trainer3':
                    {'rattatas':10, 'eevees': 3, 'ditto':2, 'magikarps':2, 'zubats':3, 'pidgey': 20}, 
               'Trainer4':
                    {'rattatas':17, 'eevees': 1, 'magikarps':9, 'zubats':12, 'pidgey': 14}}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testSixA(self):
         self.assertEqual(sorted(pooled.items()), [('ditto', 3), ('eevees', 7), ('magikarps', 21), ('pidgey', 61), ('rattatas', 67), ('zubats', 26)], "Testing that pooled contains correct values.")
      def testSixB(self):
         self.assertEqual(common, "rattatas", "Testing that common contains the correct value.")

   myTests().main()


6.1 **Challenge:** Below, we have provided the nested dictionary ``medals`` that describes how many medals the USA won in various sports at the Rio Olympics. Write code to sort the sports in ``medals`` based on the total number of medals that were won, from highest to lowest. Save the list of sorted sports as ``sorted_sports``. Save the sport with the most medals as ``most_medals`` and the sport with the least medals as ``least_medals``. 

.. activecode:: ee_sort_061
   :tags: Sort/intro-SortingwithSortandSorted.rst, Sort/Optionalreverseparameter.rst, Sort/Optionalkeyparameter.rst, Sort/Anonymousfunctionswithlambdaexpressions.rst, Sort/SortingaDictionary.rst

   medals = {'gymnastics': {'gold': 4, 'silver': 6, 'bronze': 2}, 'basketball': {'gold': 2, 'silver': 0, 'bronze': 0}, 'fencing': {'gold': 0, 'silver': 2, 'bronze': 2}, 'swimming': {'gold': 16, 'silver': 8, 'bronze': 9}, 'wrestling': {'gold': 2, 'silver': 0, 'bronze': 1}, 'volleyball': {'gold': 0, 'silver': 0, 'bronze': 2}, 'track & field': {'gold': 13, 'silver': 10, 'bronze': 9}, 'boxing': {'gold': 1, 'silver': 1, 'bronze': 1}, 'diving': {'gold': 0, 'silver': 2, 'bronze': 1}, 'water polo': {'gold': 1, 'silver': 0, 'bronze': 0}}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testA(self):
         self.assertEqual(sorted_sports, ['swimming', 'track & field', 'gymnastics', 'fencing', 'diving', 'boxing', 'wrestling', 'volleyball', 'basketball', 'water polo'], "Testing that sorted_sports was created correctly.")
      def testB(self): 
         self.assertEqual(most_medals, 'swimming', "Testing that most_medals was assigned correctly.")
      def testC(self): 
         self.assertEqual(least_medals, 'water polo', "Testing that least_medals was asigned correctly.")


   myTests().main()  


6.2 **Challenge** Here is a dictionary called pokemon_go_data that contains 4 trainers and their data about which pokemon they have caught and how many candy they have for each one. Compress the data so that there is just one dictionary that has all of the information on how many candy each pokemon has overall. Sort this dictionary and assign to the variable ``popular_pokemon`` the top 5 pokemon (those who have the most amount of candy).

.. activecode:: ee_sort_062
   :tags: Sort/SortingaDictionary.rst, Sort/Optionalkeyparameter.rst, Sort/Optionalreverseparameter.rst, Sort/Anonymousfunctionswithlambdaexpressions.rst, Sort/intro-SortingwithSortandSorted.rst

   pokemon_go_data = {'bentspoon':
                      {'Rattata': 203, 'Pidgey': 120, 'Drowzee': 89, 'Squirtle': 35, 'Pikachu': 3, 'Eevee': 34, 'Magikarp': 300, 'Paras': 38},
                  'Laurne':
                      {'Pidgey': 169, 'Rattata': 245, 'Squirtle': 9, 'Caterpie': 38, 'Weedle': 97, 'Pikachu': 6, 'Nidoran': 44, 'Clefairy': 15, 'Zubat': 79, 'Dratini': 4},
                  'picklejarlid':
                       {'Rattata': 32, 'Drowzee': 15, 'Nidoran': 4, 'Bulbasaur': 3, 'Pidgey': 56, 'Weedle': 21, 'Oddish': 18, 'Magmar': 6, 'Spearow': 14},
                  'professoroak':
                       {'Charmander': 11, 'Ponyta': 9, 'Rattata': 107, 'Belsprout': 29, 'Seel': 19, 'Pidgey': 93, 'Shellder': 43, 'Drowzee': 245, 'Tauros': 18, 'Lapras': 18}}

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(popular_pokemon, ['Rattata', 'Pidgey', 'Drowzee', 'Magikarp', 'Weedle'], "Testing that popular_pokemon has the correct value.")

   myTests().main()


