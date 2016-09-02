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

1. Create a class called Bike that contains two instance variables, color and price. Assign to the variable testOne, an instance of Bike whose color is blue and price is 89.99. Assign to the variable testTwo, an instance of Bike whose color is purple and price is 25. 

.. activecode:: ee_ch13_01
   :tags: Classes/ImprovingourConstructor.rst


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(testOne.color, "blue", "Testing that testOne has the correct color assigned.")
         self.assertEqual(testOne.price, 89.99, "Testing that testOne has the correct price assigned.")

      def testTwo(self):
         self.assertEqual(testTwo.color, "purple", "Testing that testTwo has the correct color assigned.")
         self.assertEqual(testTwo.price, 25, "Testing that testTwo has the correct color assigned.")

   myTests().main()

1.1 Create a class called ``inst_var`` that defines two instance variables: ``num1`` and ``num2``. Then, create an instance where num1 is 6 and num2 is 10 and save this instance to the variable ``t``. 

.. activecode:: ee_ch13_011
   :tags:Classes/ImprovingourConstructor.rst

      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOneA(self):
         self.assertEqual(t.num1, 6, "Testing that t.num1 has correct number assigned.")
      def testOneB(self):
         self.assertEqual(t.num2, 10, "Testing that t.num2 has correct number assigned.")

   myTests().main()

1.2 Create a class called House that has three instance variables: color, rooms, and price. To the variable name ``houseOne``, assign an instance of House whose color is white, has 3 rooms, and costs 50000. To the variable name ``houseTwo``, assign an instance of House whose color is red, has 9 rooms, and costs 1000000. 

.. activecode:: ee_ch13_012
   :tags: Classes/ImprovingourConstructor.rst


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(houseOne.color, "white", "Testing that houseOne has the correct color assigned.")
         self.assertEqual(houseOne.rooms, 3, "Testing that houseOne was assigned the correct number of rooms.")
         self.assertEqual(houseOne.price, 50000, "Testing that houseOne was assigned the correct price.")

      def testTwo(self):
         self.assertEqual(houseTwo.color, "red", "Testing that houseTwo has the correct color assigned.")
         self.assertEqual(houseTwo.rooms, 9, "Testing that houseTwo was assigned the correct number of rooms.")
         self.assertEqual(houseTwo.price, 1000000, "Testing that houseTwo was assigned the correct price.")

   myTests().main()

2. Create a class called ``math_op`` with one instance variable and a method. The instance variable should be ``numb``. The method should be called ``squared`` and return the instance variable squared. Create an instance of this class with an initial number of 8. Assign to the variable ``output`` the value of numb without hardcoding. Call the method so that the value is 64. 

.. activecode:: ee_ch13_02
   :tags: Classes/AddingOtherMethodstoourClass.rst, Classes/ImprovingourConstructor.rst

      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(output, 64, "Testing that output has correct value assigned.")

   myTests().main()

2.1 Create a class called Apple that contains one instance variable, quantity. Write a class method called ``increase`` that increases the quantity by 1 each time it is run. Assign to the variable tester, an instance of Apple that has an initial quantity of 4. Assign to the variable ``initial_quantity`` the value of tester's quantity without hardcoding. Call the method four times. 

.. activecode:: ee_ch13_021
   :tags: Classes/ImprovingourConstructor.rst, Classes/AddingOtherMethodstoourClass.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(tester.quantity, 8, "Testing that testOne has the correct value assigned.")
      def testTwo(self):   
         self.assertEqual(initial_quantity, 4, "Testing that initial_quantity has the correct value assigned.")


   myTests().main()

2.2 Create a class called Animal that has two instance variables: arms and legs. Create a class method called limbs that, when called, returns the total number of limbs the animal has. To the variable name ``spider``, assign an instance of Animal that has 4 arms and 4 legs. Call the limbs method on ``spider`` and save the result to the variable name ``spidlimbs``. 

.. activecode:: ee_ch13_022
   :tags: Classes/ImprovingourConstructor.rst, Classes/AddingOtherMethodstoourClass.rs


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(spider.arms, 4, "Testing that spider was assigned the correct number of arms.")
         self.assertEqual(spider.legs, 4, "Testing that spider was assigned the correct number of legs.")
         self.assertEqual(spidlimbs, 8, "Testing that spidlimbs was assigned correctly.")

   myTests().main()    


3. Create a class called ``bank`` that contains two instance variables, ``name`` and ``amt``. Add the instance method that allows you to customize the message returned when you print the instance so that it says "Your account, [name goes here], has [start_amt goes here] dollars." Create an instance of this class with "Bob" as the name and 100 as the amount. Save this to the variable ``t1``.

.. activecode:: ee_ch13_03
   :tags: Classes/AddingOtherMethodstoourClass.rst, Classes/ImprovingourConstructor.rst, Classes/ConvertinganObjecttoaString.rst

   

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(t1.__str__(), "Your account, Bob, has 100 dollars.", "Testing that t1 is assigned to correct value")

   myTests().main()

3.1 Create a class called Sports that contains 2 instance variables, name and number_of_players. Add the instance method that allows you to customize the message returned when you print the instance so that it says "The name of this sport is [name goes here] and [number_of_players goes here] people create one team!" Create two instances of the class, one assigned to the variable football_info and one called quidditch_info. The first uses football as the name and has 11 players, the second uses quidditch as the name and has 7 players.

.. activecode:: ee_ch13_031
   :tags: Classes/ImprovingourConstructor.rst, Classes/AddingOtherMethodstoourClass.rst, Classes/ConvertinganObjecttoaString.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(football_info.__str__(), "The name of the sport is football and 11 people create one team!", "Testing that football_info has the correct value assigned.")
      def testTwo(self):   
         self.assertEqual(quidditch_info.__str__(), 'The name of the sport is quidditch and 7 people create one team!', "Testing that quidditch_info has the correct value assigned.")


   myTests().main()

3.2 Create a class called Cereal that has three instance variables: name, brand, and fiber. When an instance of Cereal is printed, the user should see the following: "[name] cereal is produced by [brand] and has [fiber] grams of fiber in every serving!" To the variable name ``c1``, assign an instance of Cereal whose name is Corn Flakes, brand is Kellogg's, and fiber is 2. To the variable name ``c2``, assign an instance of Cereal whose name is Honey Nut Cheerios, brand is General Mills, and fiber is 3. Practice printing both! 

.. activecode:: ee_ch13_032
   :tags: Classes/ImprovingourConstructor.rst, Classes/AddingOtherMethodstoourClass.rst, Classes/ConvertinganObjecttoaString.rst


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(c1.__str__(), "Corn Flakes cereal is produced by Kellogg's and has 2 grams of fiber in every serving!", "Testing that c1 prints correctly.")
      def testTwo(self): 
         self.assertEqual(c2.__str__(), "Honey Nut Cheerios cereal is produced by General Mills and has 3 grams of fiber in every serving!", "Testing that c2 prints correctly.")

   myTests().main()  

4. This problem will modify your previously defined class, ``bank``. Add two more instance variables, ``deposits`` and ``withdrawals``.Add two more methods, ``add_deposit`` and ``less_withdrawals``. The add_deposit method should add the deposit amount to amt and the less_withdrawals method should subtract the withdrawal amount from amt. Create two instances of the class, the first assigned to ``bob`` and the second to ``sally``. The first uses "Bob" as the name, 100 as the start_amt, and 50 as the deposit amount. The second uses "Sally" as the name, 200 as the start amount, 0 as the deposit, and 125 as the withdrawal amount. For ``bob``, call add_deposit enough times so that the start_amt is 200 dollars and save to the variable ``bob_amt``. For ``sally``, call less_withdrawal enough times so that the start_amt is 75 dollars and save to the variable ``sally_amt``.

.. activecode:: ee_ch13_04
   :tags: Classes/AddingOtherMethodstoourClass.rst, Classes/ImprovingourConstructor.rst, Classes/ConvertinganObjecttoaString.rst
   

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFourA(self):
         self.assertEqual(bob.__str__(), "Your account, Bob, has 200 dollars.", "Testing that bob is assigned to correct value")
      def testFourB(self):
         self.assertEqual(sally.__str__(), 'Your account, Sally, has 75 dollars.', "Testing that sally is assigned to correct value")
      def testFourC(self):
         self.assertEqual(bob_amt, 200, "Testing that bob_amt is assigned to correct value")
      def testFourD(self):
         self.assertEqual(sally_amt, 75, "Testing that sally is assigned to correct value")

   myTests().main()

4.1 Create a class called Sports that contains 3 instance variables, name, number_of_players, and recruit_max. Add the instance method that allows you to customize the message returned when you print the instance so that it says "The name of this sport is [name goes here] and [number_of_players goes here] people create one team!" There should also be another class method called recruiting, which will add the recruit_max to the current value for number_of_players.Create two instances of the class, one assigned to the variable football_info and one called quidditch_info. The first uses football as the name and has 11 players and a max number of 3 recruits, the second uses quidditch as the name and has 7 players and a max number of 2 recruits. Call recruiting enough times so that football_info has 17 players and that quidditch_info has 9 players.

.. activecode:: ee_ch13_041
   :tags: Classes/ImprovingourConstructor.rst, Classes/AddingOtherMethodstoourClass.rst, Classes/ConvertinganObjecttoaString.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(football_info.__str__(), "The name of the sport is football and 11 people create one team!", "Testing that football_info has the correct value assigned.")
      def testTwo(self):   
         self.assertEqual(quidditch_info.__str__(), 'The name of the sport is quidditch and 7 people create one team!', "Testing that quidditch_info has the correct value assigned.")
   
   myTests().main()

4.2 Create a class called Cereal that has three instance variables: name, brand, and fiber. When an instance of Cereal is printed, the user should see the following: "[name] cereal is produced by [brand] and has [fiber] grams of fiber in every serving!" Create an instance method called add_fiber that increases an instance's fiber count by 1 when it is called. To the variable name ``c1``, assign an instance of Cereal whose name is Corn Flakes, brand is Kellogg's, and fiber is 2. Call the add_fiber method until c1 has a fiber count of 5. 

.. activecode:: ee_ch13_042
   :tags: Classes/ImprovingourConstructor.rst, Classes/AddingOtherMethodstoourClass.rst, Classes/ConvertinganObjecttoaString.rst



   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(c1.__str__(), "Corn Flakes cereal is produced by Kellogg's and has 5 grams of fiber in every serving!", "Testing that c1 prints correctly and has the correct fiber count.")

   myTests().main()   

5. **Challenge** The class, ``Olympics``, is given and has two instance variables, country and medal, referencing a country and its corresponding medal count in the Rio Olympics. The list, ``L``, gives some countries and their medal counts. Create a list of instances from the given list and assign it to the variable ``instances``. Then, sort the instances based on medal count and then alphabetically by country name. The sorted medal count list should be assigned to the variable ``sort_medal`` and be a list of tuples displaying both the country name and medal count from highest medal count to lowest. The list sorted alphabetically should only display the country name and be assigned to the variable ``sort_alpha``. 

.. activecode:: ee_ch13_05
   :tags: Classes/sorting_instances.rst, Classes/InstancesasReturnValues.rst

   class Olympics():
       def __init__(self, country, medal):
           self.country = country
           self.medal = medal
        
       def sort_medal(self):
           return self.medal
   
       def sort_country(self):
           return self.country

   L = [("Italy", 28), ("China", 70), ("Australia", 29), ("United States", 121), ("Russia", 56), ("South Korea", 21), ("Venezuela", 3)]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFiveA(self):
         self.assertEqual(len(instances), 7, "Testing that instances is assigned to correct values")
      def testFiveB(self):
         self.assertEqual(sort_medal, [('United States', 121), ('China', 70), ('Russia', 56), ('Australia', 29), ('Italy', 28), ('South Korea', 21), ('Venezuela', 3)], "Testing if sort_medal is assigned to correct values")
      def testFiveC(self):
         self.assertEqual(sort_alpha, sorted(['Australia', 'China', 'Italy', 'Russia', 'South Korea', 'United States', 'Venezuela']), "Testing if sort_alpha is assigned to correct values")

   myTests().main()

5.1 **Challenge:** Provided is a class called called ``Music`` that has 3 instance variables, title, genre, and price. Provided is a list of tuples. Assign them to a new list and use the tuples to as parameters for instances of Music. Then, assign to the variable ``music_genre`` a sorted list of the instances' titles by genre a-z. Assign to the variable ``music_price`` a sorted list of the instances' titles by price, low to high. Hint: sorted won't return the str method, so you will need to specify the title some way.

.. activecode:: ee_ch14_051
   :tags: Classes/sorting_instances.rst, Classes/InstancesasReturnValues.rst

   class Music():
       def __init__(self, song_title, genre, price):
           self.title = song_title
           self.genre = genre
           self.price = price

       def genre_info(self):
           return self.genre

       def price_info(self):
           return self.price

       def title_info(self):
           return self.title

       def __str__(self):
           return "{}".format(self.title)

   lst_tuples = [("Broken Bones", "Alternative", 1.29), ("That Old Black Magic", "Jazz", .99), ("True Friends", "Rock", 1.19), ("Summer Vibe", "Pop", .67), ("Shoop", "Hip-Hop", 1.30)]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(music_genre, ['Broken Bones', 'Shoop', 'That Old Black Magic', 'Summer Vibe', 'True Friends'], "Testing that music_genre has the correct list assigned.")
      def testTwo(self):   
         self.assertEqual(music_price, ['Summer Vibe', 'That Old Black Magic', 'True Friends', 'Broken Bones', 'Shoop'], "Testing that music_price has the correct list assigned.")


   myTests().main()


5.2 **Challenge:** Below, we have provided a list of tuples. Use these to create a list of instances of the House class. Each instance should have three instance variables: color, rooms, and price. When an instance is printed, the user should see: "This is a [color] house with [rooms] rooms that costs [price] dollars." Save the list of instances as the variable ``houses``. Then, sort the list based on price, highest to lowest, and save this list as ``houses_by_price``. Finally, sort the list based on number of rooms, highest to lowest, and save this last as ``houses_by_rooms``. 

.. activecode:: ee_ch13_052
   :tags: Classes/sorting_instances.rst, Classes/InstancesasReturnValues.rst

   tups = [("blue", 2, 30000), ("white", 5, 10000), ("yellow", 8, 100000), ("green", 1, 8000), ("brown", 3, 400000), ("taupe", 4, 200000), ("orange", 6, 250000)]


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui): 

      def testA(self): 
         self.assertEqual(len(houses), 7, "Testing that houses has the correct number of instances in it.")

      def testB(self): 
         self.assertEqual(houses_by_price[0].price, 400000, "Testing that houses_by_price was created correctly.")
         self.assertEqual(houses_by_price[1].price, 250000, "Testing that houses_by_price was created correctly.")
         self.assertEqual(houses_by_price[-1].price, 8000, "Testing that houses_by_price was created correctly.")

      def testC(self): 
         self.assertEqual(houses_by_rooms[0].rooms, 8, "Testing that houses_by_rooms was created correctly.")
         self.assertEqual(houses_by_rooms[1].rooms, 6, "Testing that houses_by_rooms was created correctly.")
         self.assertEqual(houses_by_rooms[-1].rooms, 1, "Testing that houses_by_rooms was created correctly.")

   myTests().main()













​


