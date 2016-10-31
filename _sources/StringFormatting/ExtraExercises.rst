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

1. Using string interpolation, fill out the parameters so that "I go to UM and I am in SI 106" is assigned to ``str1``.

.. activecode:: ee_interpolation_01
   :tags: StringFormatting/Interpolation.rst

   str1 = "I go to {} and I am in {}".format()
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(str1, "I go to UM and I am in SI 106", "Testing that str1 is assigned to correct value")

   myTests().main()


1.1 Using string interpolation, fill out the parameters so that 'This book teaches students python.' is assigned to ``info``.

.. activecode:: ee_interpolation_011
   :tags: StringFormatting/Interpolation.rst

   info = "This book {} students {}.".format()

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(info, "This book teaches students python.", "Testing that info has the correct value.")

   myTests().main()

1.2 Below, we have provided a list of words. Use string formatting to produce the following string: "My favorite animals are elephants, giraffes, and zebras." Save this string to the variable name ``animal_string``. 

.. activecode:: ee_interpolation_012
   :tags: StringFormatting/Interpolation.rst

   animals = ['elephants', 'giraffes', 'zebras']

   animal_string = 

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(animal_string, "My favorite animals are elephants, giraffes, and zebras.", "Testing that animal_string is correct.")

   myTests().main()

2. Use string formatting to complete the string given. The blanks should correspond to variable ``name`` and ``breed``.  

.. activecode:: ee_interpolation_02
   :tags: StringFormatting/Interpolation.rst

   name = "Oreo"
   breed = "poodle"
   str1 = "This is {}, he is a {}."
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(str1, "This is Oreo, he is a poodle.", "Testing that str1 is assigned to correct value")

   myTests().main()

2.1 Using string interpolation, assign the correct value to the variable ``names`` so that the value assigned to the variable ``sent`` is "Paul, Jackie, and Stephen have taught or are teaching this class."

.. activecode:: ee_interpolation_021
   :tags: StringFormatting/Interpolation.rst

   sent = "{}, {}, and {} have taught or are teaching this class.".format()

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sent, "Paul, Jackie, and Stephen have taught or are teaching this class.", "Testing that sent has the correct value.")
         self.assertEqual(names, ['Paul', 'Jackie', 'Stephen'], "Testing that names has the correct values assigned")

   myTests().main()

2.2 Below, we have created the variables ``course`` and ``school``. Use string formatting to produce the following string: "I'm enrolled in SI 106 here at University of Michigan." Save this string to the variable name ``final``. 

.. activecode:: ee_interpolation_022
   :tags: StringFormatting/Interpolation.rst

   course = "SI 106"
   school = "University of Michigan"

   final = 

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(final, "I'm enrolled in SI 106 here at University of Michigan.", "Testing that final is correct.")

   myTests().main() 


3. Provided is a list of tuples, the first is a country, the second is their medal count. Create a new list called ``medals`` using these tuples so that if the tuple was ('USA', 121), then what is added to medals is the string "USA won 121 medals". Do so using string interpolation.

.. activecode:: ee_interpolation_03
   :tags: StringFormatting/Interpolation.rst

   countries = [('Jamaica', 11), ('Malaysia',5), ('Japan', 41), ('Sweden', 11), ('Serbia', 8)]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(medals, ['Jamaica won 11 medals', 'Malaysia won 5 medals', 'Japan won 41 medals', 'Sweden won 11 medals', 'Serbia won 8 medals'], "Testing that medals is assigned to correct values")

   myTests().main()

3.1 Provided is a list of tuples, the first is a name, the second is a city. Create a new list called ``user_info`` using these tuples so that if the tuple was ('Ashley', 'Kalamazoo'), then what is added to user_info is the string "Ashley is from Kalamazoo". Do so using string interpolation.

.. activecode:: ee_interpolation_031
   :tags: StringFormatting/Interpolation.rst

   info = [('Sarah', 'Mattawan'), ("Grace", "Kalamazoo"), ('Mariana', "Sao Paulo"), ('Kevin', 'Melbourne'), ('Srishti', 'Dubai'), ('Kathleen', 'Bagota'), ('Ann', 'Excel')]


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(user_info, ['Sarah is from Mattawan', 'Grace is from Kalamazoo', 'Mariana is from Sao Paulo', 'Kevin is from Melbourne', 'Srishti is from Dubai', 'Kathleen is from Bagota', 'Ann is from Excel'], "Testing that user_info has the correct value.")
         
   myTests().main()

3.2 Below, we have provided a list of tuples that contain information about summer Olympic meets. Create a new list called ``olympics_info`` using these tuples so that if the tuple is ('2016', 'Rio de Janeiro, Brazil'), then what is added to ``olympics_info`` is the string: "The 2016 Olympics were held in Rio de Janeiro, Brazil." Do this by using string interpolation. 

.. activecode:: ee_interpolation_032
   :tags: StringFormatting/Interpolation.rst

   tups = [('2016', 'Rio de Janeiro, Brazil'), ('2012', 'London, Great Britain'), ('2008', 'Beijing, China'), ('2004', 'Athens, Greece'), ('2000', 'Sydney, Australia'), ('1996', 'Atlanta, Georgia, USA'), ('1992', 'Barcelona, Spain'), ('1988', 'Seoul, Korea')]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(olympics_info, ['The 2016 Olympics were held in Rio de Janeiro, Brazil.', 'The 2012 Olympics were held in London, Great Britain.', 'The 2008 Olympics were held in Beijing, China.', 'The 2004 Olympics were held in Athens, Greece.', 'The 2000 Olympics were held in Sydney, Australia.', 'The 1996 Olympics were held in Atlanta, Georgia, USA.', 'The 1992 Olympics were held in Barcelona, Spain.', 'The 1988 Olympics were held in Seoul, Korea.'], "Testing that olympics_info is correct.")

   myTests().main()  

4. Write a function called ``pokemon`` that takes in a list of an integer and string. The integer is the level of the trainer and the string is where the trainer plays. If the player is level five or below, they have the most rattatas. If they are between level 6 and 10, they have the most zubats. If they are higher than level 10, they have the most eevees. Return the string "I'm level __ and I caught a bunch of __ in the __!" where the first blank is the player level, the second is the pokemon, and the third is the location where they play. For instance, if the inputted list is [2, "city"], the returned string should be "I'm level 2 and I caught a bunch of rattatas in the city!" Do this using string interpolation.

.. activecode:: ee_interpolation_04
   :tags: StringFormatting/Interpolation.rst
      

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(pokemon([4, "suburbs"]), "I'm level 4 and I caught a bunch of rattatas in the suburbs!", "Testing that pokemon[4, 'suburbs'] returns 'I'm level 4 and I caught a bunch of rattatas in the suburbs!'.")
         self.assertEqual(pokemon([25, "field"]), "I'm level 25 and I caught a bunch of eevees in the field!", "Testing that pokemon[25, 'field'] returns 'I'm level 25 and I caught a bunch of eevees in the field!'.")
         self.assertEqual(pokemon([10, "city"]), "I'm level 10 and I caught a bunch of zubats in the city!", "Testing that pokemon[10, 'city'] returns 'I'm level 10 and I caught a bunch of zubats in the city!'.")

   myTests().main()

4.1 Write a function called ``data_mine`` that takes a tuple as input, and return a string using interpolation, depending on the second item in the tuple. The first item is a city name, the second is the weather condition. If the second item in the tuple has the value of 'rain', then it should also be cloudy. If the second item has the value of 'sun', then there should be blue skies. If the second item has the value of 'snow', then it should be cold. Return the string "In ___ there is ___ so it is ____." or "In ____ there is ___ so there are _____." (so for ('Maz', 'rain'), we would return "In Maz there is rain so it is cloudy" (the same goes for snow), while for ('Bieur', 'sun'), we would return "In Bieur there is sun so there are blue skies.")

.. activecode:: ee_interpolation_041
   :tags: StringFormatting/Interpolation.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(data_mine(('Iron Mountain', 'snow')), "In Iron Mountain there is snow so it is cold.", "Testing that data_mine has the correct return value with input ('Iron Mountain', 'snow').")
         self.assertEqual(data_mine(('Santa Clara', 'sun')), 'In Santa Clara there is sun so there are blue skies.', "Testing that data_mine has the correct return value with input ('Santa Clara', 'sun')")
         self.assertEqual(data_mine(('Seattle', 'rain')), "In Seattle there is rain so it is cloudy.", "Testing that data_mine has the correct return value with input ('Seattle', 'rain')")
         
   myTests().main()

4.2 Write a function called ``grades`` that takes in a list with two elements, the first being a string (a person's name) and the second being an integer (their grade on a test). If the grade is greater than or equal to 70, the function should return: "Congrats, [name], you passed the test with a [grade]!" If the grade is lower than 70, the function should return: "Sorry, [name], you failed the test with a [grade]."

.. activecode:: ee_interpolation_042
   :tags: StringFormatting/Interpolation.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(grades(["Jenny", 90]), "Congrats, Jenny, you passed the test with a 90!", "Testing the function grades on input ['Jenny', 90].")
         self.assertEqual(grades(["Tina", 70]), "Congrats, Tina, you passed the test with a 70!", "Testing the function grades on input ['Tina', 70].")
         self.assertEqual(grades(["Betty", 45]), "Sorry, Betty, you failed the test with a 45.", "Testing the function grades on input ['Betty', 45].")

   myTests().main()  

5. The list of tuples, ``order``, contains information about pizza orders. It contains information on whether or not the order is a pickup or delivery, how many pizzas were ordered, the kind of pizzas, and in how many minutes they need to be ready. Create a list called ``response`` that gives a response to each order. For a delivery, if the order input is ("delivery", 1, "cheese", 10), the response should be "Your 1 cheese pizza will be delivered in 10 minutes". If the order is a pickup, the response should be "Come pick up your 1 cheese pizza in 10 minutes". 

.. activecode:: ee_interpolation_05
   :tags: StringFormatting/Interpolation.rst

   order = [("delivery", 3, "pepperoni", 20), ("pickup", 4, "cheese", 10), ("pickup", 2, "combo", 5), ("delivery", 10, "cheese", 15), ("delivery", 1, "supreme", 60)]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFive(self):
         self.assertEqual(response, ['Your 3 pepperoni pizzas will be delivered in 20 minutes', 'Come pick up your 4 cheese pizzas in 10 minutes', 'Come pick up your 2 combo pizzas in 5 minutes', 'Your 10 cheese pizzas will be delievered in 15 minutes', 'Your 1 supreme pizzas will be delievered in 60 minutes'], "Testing if response is assigned to correct values")

   myTests().main()


5.1 Below, we have provided a list of tuples that contain information about customers' product reviews on Amazon: the product, its rating, and customer name. Write a function called ``feedback`` that takes a tuple as input and returns a message to the customer based on their review. If the customer rated their product as an 8 or higher, ``feedback`` should return the following string: "[name], we're happy to hear that you gave your new [product] a [rating] rating!" If the rating was below 8, ``feedback`` should return: "[name], we're sorry to hear that your new [product] was not excellent." Create a list called ``feedback_messages`` that contains a response to each customer below. 

.. activecode:: ee_interpolation_052
   :tags: StringFormatting/Interpolation.rst

   tups = [("Dyson vacuum", 9.1, "Sandy"), ("Keurig", 5.0, "Timmy"), ("SleepComfort mattress", 8.0, "Sam"), ("Michael Kors vest", 6.9, "Kate"), ("LG Dishwasher", 10.0, "Charles")]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(feedback_messages, ["Sandy, we're happy to hear that you gave your new Dyson vacuum a 9.1 rating!", "Timmy, we're sorry to hear that your new Keurig was not excellent.", "Sam, we're happy to hear that you gave your new SleepComfort mattress a 8 rating!", "Kate, we're sorry to hear that your new Michael Kors vest was not excellent.", "Charles, we're happy to hear that you gave your new LG Dishwasher a 10 rating!"], "Testing that feedback_messages is correct.")

   myTests().main()   

