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

1. The class, ``Pokemon``, is provided below and describes a Pokemon and its leveling and evolving characteristics. An instance of the class is one pokemon that you create. ``Grass_Pokemon`` is a subclass that inherits from ``Pokemon`` but changes some aspects, for instance, the boost values are different. For the subclass ``Grass_Pokemon``, add another method called ``action`` that returns the string "[name of pokemon] knows a lot of different moves!". Call an instance of this class with the name as "Belle". Assign this instance to the variable ``p1``.

.. activecode:: ee_inheritance_01
   :tags:Inheritance/inheritVarsAndMethods.rst

   class Pokemon():
       attack = 12
       defense = 10
       health = 15
    
       def __init__(self, name, level = 5):
           self.name = name
           self.p_type = "Normal"
           self.level = level
       
       def train(self):
           self.update()
           self.attack_up()
           self.defense_up()
           self.health_up()
           self.level = self.level + 1
           if self.level%self.evolve == 0:
               return self.level, "Evolved!"
           else:
               return self.level
    
       def attack_up(self):
           self.attack = self.attack + self.attack_boost
           return self.attack
    
       def defense_up(self):
           self.defense = self.defense + self.defense_boost
           return self.defense
    
       def health_up(self):
           self.health = self.health + self.health_boost
           return self.health

       def update(self):
           self.health_boost = 5
           self.attack_boost = 3
           self.defense_boost = 2
           self.evolve = 10
        
       def __str__(self):
           self.update()
           return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

   class Grass_Pokemon(Pokemon):
       attack = 15
       defense = 14
       health = 12
    
       def update(self):
           self.health_boost = 6
           self.attack_boost = 2
           self.defense_boost = 3
           self.evolve = 12
        
       def moves(self):
           self.p_moves = ["razor leaf", "synthesis", "petal dance"]


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOneA(self):
         self.assertEqual(p1.action(), "Belle knows a lot of different moves!", "Testing that action method is correct and p1 assigned to correct value")
      
   myTests().main()

1.1 Provided is a class called Trainer, which is based off the pokemon games. An instance of the Trainer class is one pokemon that you create. The WaterPokemon class inherits from Trainer and changes the pokemon a bit, stats change once they are trained for instance. Add a new method called ``show_moves`` to WaterPokemon that gives them the moves "Waterfall", "Water Gun", "Surf", and "Fog" and prints out to the user the moves, and returns a list of the moves. Store the moves in a variable called ``moves``. To test, create an instance of WaterPokemon and assign it to the variable ``tester``. The parameters of the pokemon are up to you.

.. activecode:: ee_inheritance_011
   :tags: Inheritance/inheritVarsAndMethods.rst


   class Trainer():
       attack = 10
       defense = 12
       health = 10

       def __init__(self, pokemon_name, level = 5):
           self.pokemon_name = pokemon_name
           self.p_type = "Normal"
           self.level = level
           self.health_boost = 4
           self.attack_boost = 2
           self.defense_boost = 3

       def __str__(self):
           return "Pokemon name: {}, Type: {}, Level: {}".format(self.pokemon_name, self.p_type, self.level)

       def train(self):
           self.Attack_up()
           self.Defense_up()
           self.health_up()
           if (self.level + 1 % 15) == 0:
               print "{} Evolved!".format(self.pokemon_name)
           self.level += 1
           return self.level

       def Attack_up(self):
           self.attack = self.attack + self.attack_boost
           return self.attack

       def Defense_up(self):
           self.defense += self.defense_boost
           return self.defense

       def health_up(self):
           self.health += self.health_boost
           return self.health

   # Do not change the parent class

   class WaterPokemon(Trainer):
    
       def update(self):
           self.health_boost = 5
           self.attack_boost = 3
           self.defense_boost = 2
    
       def actions(self):
           print "{} can do a bunch of things!".format(self.pokemon_name)
        
       def train(self):
           self.update()
           self.Attack_up()
           self.Defense_up()
           self.health_up()
           if (self.level + 1) % 20 == 0:
               print "{} Evolved!".format(self.pokemon_name)
           self.level += 1
           return self.level

   #write your instance below here.




   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(tester.moves), sorted(['Waterfall', 'Water Gun', 'Surf', 'Fog']), "Testing that the method moves is set up correctly.")

   myTests().main()

2. The attack strength for grass Pokemon does not change until they reach level 10. At level 10 and up, their attack strength increases by the attack_boost amount when they level. Modify the ``Grass_Pokemon`` class to reflect this change. To test, create an instance of the class with the name as "Bulby". Assign the instance to the variable ``p2``. Then, train the Pokemon until it reaches level 10.

.. activecode:: ee_inheritance_02
   :tags:Inheritance/inheritVarsAndMethods.rst,Inheritance/OverrideMethods.rst

   class Pokemon():
       attack = 12
       defense = 10
       health = 15
    
       def __init__(self, name, level = 5):
           self.name = name
           self.p_type = "Normal"
           self.level = level
       
       def train(self):
           self.update()
           self.attack_up()
           self.defense_up()
           self.health_up()
           self.level = self.level + 1
           if self.level%self.evolve == 0:
               return self.level, "Evolved!"
           else:
               return self.level
    
       def attack_up(self):
           self.attack = self.attack + self.attack_boost
           return self.attack
    
       def defense_up(self):
           self.defense = self.defense + self.defense_boost
           return self.defense
    
       def health_up(self):
           self.health = self.health + self.health_boost
           return self.health

       def update(self):
           self.health_boost = 5
           self.attack_boost = 3
           self.defense_boost = 2
           self.evolve = 10
        
       def __str__(self):
           return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

   class Grass_Pokemon(Pokemon):
       attack = 15
       defense = 14
       health = 12
    
       def update(self):
           self.health_boost = 6
           self.attack_boost = 2
           self.defense_boost = 3
           self.evolve = 12
           self.p_type = "Grass"
        
       def moves(self):
           self.p_moves = ["razor leaf", "synthesis", "petal dance"]
           

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOneA(self):
         self.assertEqual(p2.__str__(), "Pokemon name: Bulby, Type: Grass, Level: 5", "Testing that p2 is assigned to correct value.")
      def testOneB(self):
         self.assertEqual(p2.attack_up(), 17, "Testing that attack value is assigned to correct value at level 10.")
      
   myTests().main()

2.1 Provided is the same Trainer class. Write code in the subclass WaterPokemon so that the type of the pokemon now reflects the more specific class it belongs to, in this case it should be "Water". This should be accomplished in one line of code. Create another instance of the WaterPokemon class with an initial level of 18 and assign it to the variable ``water_type``. Invoke the train method twice to level up your pokemon.

.. activecode:: ee_inheritance_021
   :tags: Inheritance/inheritVarsAndMethods.rst


   class Trainer():
       attack = 10
       defense = 12
       health = 10

       def __init__(self, pokemon_name, level = 5):
           self.pokemon_name = pokemon_name
           self.p_type = "Normal"
           self.level = level
           self.health_boost = 4
           self.attack_boost = 2
           self.defense_boost = 3

       def __str__(self):
           return "Pokemon name: {}, Type: {}, Level: {}".format(self.pokemon_name, self.p_type, self.level)

       def train(self):
           self.Attack_up()
           self.Defense_up()
           self.health_up()
           if (self.level + 1 % 15) == 0:
               print "{} Evolved!".format(self.pokemon_name)
           self.level += 1
           return self.level

       def Attack_up(self):
           self.attack = self.attack + self.attack_boost
           return self.attack

       def Defense_up(self):
           self.defense += self.defense_boost
           return self.defense

       def health_up(self):
           self.health += self.health_boost
           return self.health

   # Do not change the parent class

   class WaterPokemon(Trainer):
    
       def update(self):
           self.health_boost = 5
           self.attack_boost = 3
           self.defense_boost = 2
    
       def actions(self):
           print "{} can do a bunch of things!".format(self.pokemon_name)
        
       def train(self):
           self.update()
           self.Attack_up()
           self.Defense_up()
           self.health_up()
           if (self.level + 1) % 20 == 0:
               print "{} Evolved!".format(self.pokemon_name)
           self.level += 1
           return self.level

   #write your instance below here.




   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(water_type.p_type, "Water", "Testing that the attribute p_type is now 'Water'.")
         self.assertEqual(water_type.level, 20, "Testing that water_type's level is now 20.")

   myTests().main()


3. Create a new subclass for ghost type Pokemon called ``Ghost``. It should inherit from the Pokemon parent class. The starting attack value for ghost pokemon is 15, defense value is 12, and health remains the same at 15. In addition, the ghost class should also have an additional variable called ``item`` that will either have the value "Yes" or "No". If the pokemon has an item, they are able to gain XP faster so they will level every 8 levels. If they do not have an item, they gain XP much slower and evolve every 20 levels at level 20, 40, etc. In addition, they gain a 3 health, 4 attack, and 3 defense boost when they level. Also remember to update the p_type to "Ghost". Create two instances of the class with the first name as "Ghastly" and it does have an item. Assign this instance to the variable ``g1``. The second should be named "Drifloon" and it does not have an item. Assign the second instance to the variable ``g2``.Train both "Ghastly" and "Drifloon" two times.

.. activecode:: ee_inheritance_03
   :tags:Inheritance/inheritVarsAndMethods.rst,Inheritance/OverrideMethods.rst,Inheritance/InvokingSuperMethods.rst

   class Pokemon():
       attack = 12
       defense = 10
       health = 15
    
       def __init__(self, name, level = 5):
           self.name = name
           self.p_type = "Normal"
           self.level = level
       
       def train(self):
           self.update()
           self.attack_up()
           self.defense_up()
           self.health_up()
           self.level = self.level + 1
           if self.level%self.evolve == 0:
               return self.level, "Evolved!"
           else:
               return self.level
    
       def attack_up(self):
           self.attack = self.attack + self.attack_boost
           return self.attack
    
       def defense_up(self):
           self.defense = self.defense + self.defense_boost
           return self.defense
    
       def health_up(self):
           self.health = self.health + self.health_boost
           return self.health

       def update(self):
           self.health_boost = 5
           self.attack_boost = 3
           self.defense_boost = 2
           self.evolve = 10
        
       def __str__(self):
           return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

   class Grass_Pokemon(Pokemon):
       attack = 15
       defense = 14
       health = 12
    
       def update(self):
           self.health_boost = 6
           self.attack_boost = 2
           self.defense_boost = 3
           self.evolve = 12
           self.p_type = "Grass"
        
       def moves(self):
           self.p_moves = ["razor leaf", "synthesis", "petal dance"]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOneA(self):
         self.assertEqual(g1.__str__(), "Pokemon name: Ghastly, Type: Ghost, Level: 7", "Testing that g1 is assigned to correct value.")
      def testOneB(self):
         self.assertEqual(g2.__str__(), "Pokemon name: Drifloon, Type: Ghost, Level: 7", "Testing that g2 is assigned to correct value.")
      def testOneC(self):
         self.assertEqual(g1.train(), (8, "Evolved!"), "Testing that g1 evolves at level 8.")
      def testOneD(self):
         self.assertEqual(g2.train(), 8, "Testing that g2 does not evolve at level 8.")
      
   myTests().main()

3.1 Create a new subclass called ``PsychicPokemon`` that inherits from the Trainer class. It should keep the same attack, defense, and health stats, but it should have an additional stat called ``special_attack`` that should be initializd at 3 and boost by 2 whenever the attack is also boosted. Additionally, the pokemon should be the type "Psychic", and they evolve every 15 levels still. Create an instance of the PsychicPokemon class that is at level 14 and assign them to the variable ``psychic``. Train your pokemon twice. Note: there should be an easy way to do the train method in your new subclass since it doesn't change which level it evolves at. It should only take 3 lines to set up.

.. activecode:: ee_inheritance_031
   :tags: Inheritance/InvokingSuperMethods.rst, Inheritance/inheritVarsAndMethods.rst, Inheritance/OverrideMethods.rst


   class Trainer():
       attack = 10
       defense = 12
       health = 10

       def __init__(self, pokemon_name, level = 5):
           self.pokemon_name = pokemon_name
           self.p_type = "Normal"
           self.level = level
           self.health_boost = 4
           self.attack_boost = 2
           self.defense_boost = 3

       def __str__(self):
           return "Pokemon name: {}, Type: {}, Level: {}".format(self.pokemon_name, self.p_type, self.level)

       def train(self):
           self.Attack_up()
           self.Defense_up()
           self.health_up()
           if (self.level + 1 % 15) == 0:
               print "{} Evolved!".format(self.pokemon_name)
           self.level += 1
           return self.level

       def Attack_up(self):
           self.attack = self.attack + self.attack_boost
           return self.attack

       def Defense_up(self):
           self.defense += self.defense_boost
           return self.defense

       def health_up(self):
           self.health += self.health_boost
           return self.health

   # Do not change the parent class

   class WaterPokemon(Trainer):
    
       def update(self):
           self.health_boost = 5
           self.attack_boost = 3
           self.defense_boost = 2
    
       def actions(self):
           print "{} can do a bunch of things!".format(self.pokemon_name)
        
       def train(self):
           self.update()
           self.Attack_up()
           self.Defense_up()
           self.health_up()
           if (self.level + 1) % 20 == 0:
               print "{} Evolved!".format(self.pokemon_name)
           self.level += 1
           return self.level

   




   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(psychic.p_type, "Psychic", "Testing that the attribute p_type is now 'Psychic'.")
         self.assertEqual(psychic.level, 16, "Testing that psychic's level is now 16.")
         self.assertEqual(psychic.special_attack, 7, "Testing that psychic's special_attack was created properly")

   myTests().main()

4. Create another subclass called ``GrassBug_Pokemon`` that inherits from the Grass subclass. Everything will remain the same as the grass pokemon, however, the moves method will change. In addition to all the grass moves from the Grass subclass, Grass and Bug pokemon also have an additional three moves added to the list, p_moves: "poison sting", "stun spore", and "acid". Call the moves method from the Grass subclass in the moves method of the new ``GrassBug_Pokemon`` sub class and add the additional moves. 

.. activecode:: ee_inheritance_04
   :tags:Inheritance/inheritVarsAndMethods.rst,Inheritance/InvokingSuperMethods.rst,Inheritance/OverrideMethods.rst

   class Pokemon():
       attack = 12
       defense = 10
       health = 15
    
       def __init__(self, name, level = 5):
           self.name = name
           self.p_type = "Normal"
           self.level = level
       
       def train(self):
           self.update()
           self.attack_up()
           self.defense_up()
           self.health_up()
           self.level = self.level + 1
           if self.level%self.evolve == 0:
               return self.level, "Evolved!"
           else:
               return self.level
    
       def attack_up(self):
           self.attack = self.attack + self.attack_boost
           return self.attack
    
       def defense_up(self):
           self.defense = self.defense + self.defense_boost
           return self.defense
    
       def health_up(self):
           self.health = self.health + self.health_boost
           return self.health

       def update(self):
           self.health_boost = 5
           self.attack_boost = 3
           self.defense_boost = 2
           self.evolve = 10
        
       def __str__(self):
           return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

   class Grass_Pokemon(Pokemon):
       attack = 15
       defense = 14
       health = 12
    
       def update(self):
           self.health_boost = 6
           self.attack_boost = 2
           self.defense_boost = 3
           self.evolve = 12
           self.p_type = "Grass"
        
       def moves(self):
           self.p_moves = ["razor leaf", "synthesis", "petal dance"]
        
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOneA(self):
         self.assertEqual(GrassBug_Pokemon("Buggy").moves(), ['razor leaf', 'synthesis', 'petal dance', 'poison sting', 'stun spore', 'acid'], "Testing that g1 is assigned to correct value.")
     
   myTests().main()

4.1 Create a new subclass called WaterBugPokemon, which inherits from the WaterPokemon class. The new type should be "Water/Bug" and you should add bug type pokemon moves: X-Scissor, Struggle, Megahorn, and Bug Bite. Create an instance of the new subclass and assign it to the variable ``twoType``. Train your pokemon once. 

.. activecode:: ee_inheritance_041
   :tags: Inheritance/InvokingSuperMethods.rst, Inheritance/inheritVarsAndMethods.rst, Inheritance/OverrideMethods.rst


   class Trainer():
       attack = 10
       defense = 12
       health = 10

       def __init__(self, pokemon_name, level = 5):
           self.pokemon_name = pokemon_name
           self.p_type = "Normal"
           self.level = level
           self.health_boost = 4
           self.attack_boost = 2
           self.defense_boost = 3

       def __str__(self):
           return "Pokemon name: {}, Type: {}, Level: {}".format(self.pokemon_name, self.p_type, self.level)

       def train(self):
           self.Attack_up()
           self.Defense_up()
           self.health_up()
           if (self.level + 1 % 15) == 0:
               print "{} Evolved!".format(self.pokemon_name)
           self.level += 1
           return self.level

       def Attack_up(self):
           self.attack = self.attack + self.attack_boost
           return self.attack

       def Defense_up(self):
           self.defense += self.defense_boost
           return self.defense

       def health_up(self):
           self.health += self.health_boost
           return self.health

   # Do not change the parent class

   class WaterPokemon(Trainer):
    
       def update(self):
           self.health_boost = 5
           self.attack_boost = 3
           self.defense_boost = 2
    
       def actions(self):
           print "{} can do a bunch of things!".format(self.pokemon_name)
        
       def train(self):
           self.update()
           self.update()
           self.Attack_up()
           self.Defense_up()
           self.health_up()
           if (self.level + 1) % 20 == 0:
               print "{} Evolved!".format(self.pokemon_name)
           self.level += 1
           return self.level

       def possible_moves(self):
           self.moves = ["Waterfall", 'Water Gun', 'Surf', 'Fog']
           return self.moves

   




   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
      twoType.possible_moves()

      def testOne(self):
         self.assertEqual(twoType.p_type, "Water/Bug", "Testing that the attribute p_type is now 'Water/Bug'.")
         self.assertEqual(sorted(twoType.moves), sorted(["Waterfall", 'Water Gun', 'Surf', 'Fog', 'X-Scissor', 'Bug Bite', 'Struggle', 'Megahorn']), "Testing that twoType's moves were created properly")

   myTests().main()


5. Along with the Pokemon parent class, we have also provided several subclasses. Write another method in the parent class that will be inherited by the subclasses called ``opponent`` that will show which type of pokemon the current type is weak against and strong against. For instance, if the p_type of the subclass is grass, fire will be assigned to the variable ``weak`` and water will be assigned to the variable ``strong``. Grass is weak against fire, but strong against water. Ghost is weak against dark but strong against psychic. Fire is weak against water but strong against grass. Finally, flying is weak against electric but strong against fighting.

.. activecode:: ee_inheritance_05
   :tags:Inheritance/inheritVarsAndMethods.rst

   class Pokemon():
       attack = 12
       defense = 10
       health = 15
    
       def __init__(self, name,level = 5):
           self.name = name
           self.p_type = "Normal"
           self.level = level
           self.weak = "Normal"
           self.strong = "Normal"
    
       def train(self):
           self.update()
           self.attack_up()
           self.defense_up()
           self.health_up()
           self.level = self.level + 1
           if self.level%self.evolve == 0:
               return self.level, "Evolved!"
           else:
               return self.level
    
       def attack_up(self):
           self.attack = self.attack + self.attack_boost
           return self.attack
    
       def defense_up(self):
           self.defense = self.defense + self.defense_boost
           return self.defense
    
       def health_up(self):
           self.health = self.health + self.health_boost
           return self.health

       def update(self):
           self.health_boost = 5
           self.attack_boost = 3
           self.defense_boost = 2
           self.evolve = 10
        
       def __str__(self):
           self.update()
           return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

       def opponent(self):
           self.update()
           if self.p_type == "Grass":
               self.weak = "fire"
               self.strong = "water"
           elif self.p_type == "Ghost":
               self.weak = "dark"
               self.strong = "psychic"
           elif self.p_type == "Fire":
               self.weak = "water"
               self.strong = "grass"
           elif self.p_type == "Flying":
               self.weak = "electric"
               self.strong = "fighting"
           return self.weak, self.strong
    
   class Grass_Pokemon(Pokemon):
       attack = 15
       defense = 14
       health = 12
    
       def update(self):
           self.health_boost = 6
           self.attack_boost = 2
           self.defense_boost = 3
           self.evolve = 12
           self.p_type = "Grass"
    
   class Ghost_Pokemon(Pokemon):
        
       def update(self):
           self.health_boost = 3
           self.attack_boost = 4
           self.defense_boost = 3
           self.p_type = "Ghost"
        
   class Fire_Pokemon(Pokemon):
        
       def update(self):
           Pokemon.update(self)
           self.p_type = "Fire"

   class Flying_Pokemon(Pokemon):
       def update(self):
           Pokemon.update(self)
           self.p_type = "Flying"
  
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOneA(self):
         self.assertEqual(Grass_Pokemon("Buggy").opponent(), ("fire", "water"), "Testing that Grass weak and strong are assigned to correct values.")
      def testOneB(self):
         self.assertEqual(Fire_Pokemon("Buggy").opponent(), ("water", "grass"), "Testing that Fire weak and strong are assigned to correct values.")
      def testOneC(self):
         self.assertEqual(Ghost_Pokemon("Buggy").opponent(), ("dark", "psychic"), "Testing that Ghost weak and strong are assigned to correct values.")
      def testOneD(self):
         self.assertEqual(Flying_Pokemon("Buggy").opponent(), ("electric", "fighting"), "Testing that Flying weak and strong are assigned to correct values.")

   myTests().main()


5.1 Provided is the Trainer class as well as four subclasses, 5 different types of pokemon in total. Create a method in the Parent class Trainer  called ``strengths`` that returns a list of all the types that an instance of the class is strong against. For example, an instance of the WaterPokemon class, whose type is water, will be strong against Fire, Normal, Bug, and Ice and will return a list containing these types as strings. Normal types are strong against: Ice, Water, Fire, Bug, and Normal. Water types are strong against: Fire, Normal, Bug, and Ice. Ice types are strong against: Normal and Bug. Bug types are strong against: Normal, Water, Ice, and Bug. Fire types are strong against: Normal, Ice, and Bug. Create this method so that it can be inherited without changes by all subclasses. Create instances for each class, Trainer assigned to ``trainer_test``, WaterPokemon assigned to ``water_test``, IcePokemon assigned to ``ice_test``, BugPokemon assigned to ``bug_test``, and FirePokemone assigned to ``fire_test``.

.. activecode:: ee_inheritance_051
   :tags: Inheritance/inheritVarsAndMethods.rst


   class Trainer():
       attack = 10
       defense = 12
       health = 10

       def __init__(self, pokemon_name, level = 5):
           self.pokemon_name = pokemon_name
           self.p_type = "Normal"
           self.level = level
           self.health_boost = 4
           self.attack_boost = 2
           self.defense_boost = 3

       def __str__(self):
           return "Pokemon name: {}, Type: {}, Level: {}".format(self.pokemon_name, self.p_type, self.level)

       def train(self):
           self.Attack_up()
           self.Defense_up()
           self.health_up()
           if (self.level + 1 % 15) == 0:
               print "{} Evolved!".format(self.pokemon_name)
           self.level += 1
           return self.level

       def Attack_up(self):
           self.attack = self.attack + self.attack_boost
           return self.attack

       def Defense_up(self):
           self.defense += self.defense_boost
           return self.defense

       def health_up(self):
           self.health += self.health_boost
           return self.health


   class WaterPokemon(Trainer):
    
       def update(self):
           self.p_type = "Water"

   class IcePokemon(Trainer):

       def update(self):
           self.p_type = "Ice"
   
   class BugPokemon(Trainer):
       def update(self):
           self.p_type = "Bug"

   class FirePokemon(Trainer):
       def update(self):
           self.p_type = "Fire"




   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
      water_test.update()
      ice_test.update()
      fire_test.update()
      bug_test.update()
      trainer_test.strengths()
      water_test.strengths()
      ice_test.strengths()
      fire_test.strengths()
      bug_test.strengths()

      def testOne(self):
         self.assertEqual(sorted(trainer_test.strengths()), sorted(['Ice', 'Water', 'Fire', 'Bug', 'Normal']), "Testing the return value for Trainer.strengths()")
         self.assertEqual(sorted(water_test.strengths()), sorted(['Fire', 'Normal', 'Bug', 'Ice']), "Testing the return value for WaterPokemon.strengths()")
         self.assertEqual(sorted(ice_test.strengths()), sorted(['Normal', 'Bug']), "Testing the return value for IcePokemon.strengths()")
         self.assertEqual(sorted(fire_test.strengths()), sorted(['Normal', 'Ice', 'Bug']), "Testing the return value for FirePokemon.strengths()")
         self.assertEqual(sorted(bug_test.strengths()), sorted(['Normal', 'Water', 'Ice', 'Bug']), "Testing the return value for BugPokemon.strengths()")

   myTests().main()

​


