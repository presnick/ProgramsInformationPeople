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

1. Write a function called ``str_mult`` that takes in a required string parameter and an optional integer parameter. The default value for the integer parameter should be 3. The function will return the string multiplied by the integer parameter. 

.. activecode:: ee_Opt_Params_01
   :tags: OptionalAndKeywordParameters/OptionalParameters.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(str_mult("ha"), "hahaha", "Testing that str_mult('ha') returns 'hahaha'")
         self.assertEqual(str_mult("ha", 10), "hahahahahahahahahaha", "Testing that str_mult('ha') returns 'hahahahahahahahahaha'")
         self.assertEqual(str_mult("ha", 0), "", "Testing that str_mult('ha', 0) returns ''")

   myTests().main()


1.1 Define a function called ``multiply``. It should have one required parameter, a string. It should also have one optional parameter, an integer, named ``mult_int``, with a default value of 10. The function should return the string multiplied by the integer. (i.e.: Given inputs "Hello", mult_int=3, the function should return "HelloHelloHello")

.. activecode:: ee_optparams_011
   :tags: OptionalAndKeywordParameters/OptionalParameters.rst

   def multiply():

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(multiply("Hello", mult_int = 3), "HelloHelloHello", "Testing the function multiply on inputs 'Hello', 3.")
         self.assertEqual(multiply("Goodbye"), "GoodbyeGoodbyeGoodbyeGoodbyeGoodbyeGoodbyeGoodbyeGoodbyeGoodbyeGoodbye", "Testing the function mulitply on input 'Goodbye'.")

   myTests().main()

1.2 Create a function called ``mult`` that has two parameters, the first is required and should be an integer, the second is an optional parameter that can either be a number or a string but whose default is 6. The function should return the first parameter multiplied by the second.

.. activecode:: ee_opt_params_012
   :tags: OptionalAndKeywordParameters/OptionalParameters.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(mult(2), 12, "Testing that mult returns the correct value on input (2)")
         self.assertEqual(mult(5,3), 15, "Testing that mult returns the correct value on input (3,5)")
         self.assertEqual(mult(4,"hello"), "hellohellohellohello", "testing that mult returns the correct value on input (4, 'hello'")

   myTests().main()

2. The following function, ``greeting``, does not work. Please fix the code so that it runs without error. This only requires one change in the definition of the function.

.. activecode:: ee_Opt_Params_02
   :tags: OptionalAndKeywordParameters/KeywordParameters.rst

   def greeting(greeting = "Hello ", name, excl = "!"):
       return greeting + name + excl
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwo(self):
         self.assertEqual(greeting("Bob"), "Hello Bob!", "Testing that greeting('Bob') returns 'Hello Bob!'.")
         self.assertEqual(greeting(""), "Hello !", "Testing that greeting('') return 'Hello !'.")

   myTests().main()

2.1 Below is a function, ``sum``, that does not work. Change the function definition so the code works. The function should still have a required parameter, intx, and an optional parameter, intz with a defualt value of 5. 

.. activecode:: ee_optparams_021
   :tags: OptionalAndKeywordParameters/OptionalParameters.rst

   def sum(intz=5, intx):
       return intz + intx

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sum(8, intz = 2), 10, "Testing the function sum on inputs 8, 2.")
         self.assertEqual(sum(12), 17, "Testing the function sum on input 12.")

   myTests().main()

2.2 Currently the function is supposed to take 1 required parameter, and 2 optional parameters, however the code doesn't work. Fix the code so that it passes the test. This should only require changing one line of code.   

.. activecode:: ee_opt_params_022
   :tags: OptionalAndKeywordParameters/OptionalParameters.rst

   def waste(var = "Water", mar, marble = "type"):
       final_string = var + " " + marble + " " + mar
       return final_string

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(waste("Pokemon"), "Water type Pokemon", "Testing that waste returns the correct string on input 'Pokemon'")

   myTests().main()

3. Write a function, ``test``, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value "False". If the boolean parameter is False, the function should return "None".

.. activecode:: ee_Opt_Params_03
   :tags: OptionalAndKeywordParameters/OptionalParameters.rst
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testThree(self):
         self.assertEqual(test(2), 3, "Testing that test(2) returns 3")
         self.assertEqual(test(4, False), False, "Testing that test(4, False) returns False")
         self.assertEqual(test(5, dict1 = {5:4, 2:1}), 4, "Testing that test(5, dict1 = {5:4, 2:1}) returns 4")

   myTests().main()

3.1 Define a function called ``nums`` that has three parameters. The first parameter, an integer, should be required. A second parameter named ``mult_int`` should be optional with a default value of 5. The final parameter, ``switch``, should also be optional with a default value of False. The function should multiply the two integers together, and if switch is True, should change the sign of the product before returning it. 

.. activecode:: ee_optparams_031
   :tags: OptionalAndKeywordParameters/KeywordParameters.rst

   def nums():

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(nums(5), 25, "Testing the function nums on input 5.")
         self.assertEqual(nums(2, mult_int = 4), 8, "Testing the function nums on inputs 2, mult_int = 4.")
         self.assertEqual(nums(3, switch = True), -15, "Testing the function nums on inputs 3, switch = True.")
         self.assertEqual(nums(4, mult_int = 3, switch = True), -12, "Testing the function nums on inputs 4, mult_int = 3, switch = True.")
         self.assertEqual(nums(0, switch = True), 0, "Testing the function nums on inputs 0, switch = True.")

   myTests().main()  

3.2 Write a function called ``checkingIfIn`` that takes three parameters, the first is a required parameter that should be a string, the second is an optional parameter called ``direction`` with a default of True, the third is an optional parameter called ``d`` that is a default of {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. Write the function so that when the second parameter is True, it checks to see if the first parameter is a key in the third parameter and if it is, return True, otherwise return False. If the second paramter is False, then it checks to see if the first parameter is not a key of the third. If it's not a key, return True, and if it is, return False.

.. activecode:: ee_opt_params_032
   :tags: OptionalAndKeywordParameters/KeywordParameters.rst, OptionalAndKeywordParameters/OptionalParameters.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(checkingIfIn('grapes'), True, "Testing that checkingIfIn returns the correct boolean on input 'grapes'")
         self.assertEqual(checkingIfIn('carrots'), False, "Testing that checkingIfIn returns the correct boolean on input 'carrots'")
         self.assertEqual(checkingIfIn('grapes', False), False, "Testing that checkingIfIn returns the correct boolean on input ('grapes', False)")
         self.assertEqual(checkingIfIn('carrots', False), True, "Testing that checkingIfIn returns the correct boolean on input ('carrots', False)")
         self.assertEqual(checkingIfIn('grapes', d = {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1}), False, "Testing that checkingIfIn returns the correct boolean on input ('grapes', d = {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})")
         self.assertEqual(checkingIfIn('peas', d = {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1}), True, "Testing that checkingIfIn returns the correct boolean on input ('peas', d = {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})")
         self.assertEqual(checkingIfIn('peas', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1}), False, "Testing that checkingIfIn returns the correct boolean on input ('peas', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})")
         self.assertEqual(checkingIfIn('apples', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1}), True, "Testing that checkingIfIn returns the correct boolean on input ('apples', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})")

   myTests().main()

4. Write a function called ``math``, that takes in three parameters: two numbers and an optional string with the default value "add". If the string value is add, the function should add the two integers. If the string value is "subtract", subtract the second integer from the first integer. If the value is "multiply", multiply the integers and if the value is "divide", divide the first integer by the second integer.

.. activecode:: ee_Opt_Params_04
   :tags: OptionalAndKeywordParameters/OptionalParameters.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(math(1,2), 3, "Testing that math(1,2) returns 3")
         self.assertEqual(math(12,2, "divide"), 6, "Testing that math(12,2, 'divide') returns 6")
         self.assertEqual(math(0, 2, "multiply"), 0, "Testing that math(0, 2, 'multiply') returns 0")
         self.assertEqual(math(0, 7, "subtract"), -7, "Testing that math(0, 7, 'subtract') returns -7")

   myTests().main()

4.1 Define a function called ``connect`` that takes two inputs. The first, a required parameter, should be a list of strings. The second, an optional parameter named ``connector``, should have a default value of "_" but can take any string as input. The function should return one long string that contains all the original strings concatenated together, joined by the connector string.

.. activecode:: ee_optparams_041
   :tags: OptionalAndKeywordParameters/OptionalParameters.rst

   def connect():

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(connect(["hi", "bye", "yo"]), "hi_bye_yo", "Testing the function connect on input ['hi', 'bye', 'yo'].")
         self.assertEqual(connect(["a", "b", "c"], connector = "--"), "a--b--c", "Testing the function connect on inputs ['a', 'b', 'c'], connector = '--'.")
         self.assertEqual(connect(["x", "y", "z"], connector = "1234"), "x1234y1234z", "Testing the function connect on inputs ['x', 'y', 'z'], connector = '1234'.")
         self.assertEqual(connect([]), '', "Testing the function connect on input [].")
         self.assertEqual(connect(["solo"]), "solo", "Testing the function connect on input ['solo'].")


   myTests().main() 

4.2 Write a function called ``together`` that takes three parameters, the first is a required parameter that is a number (integer or float), the second is a required parameter that is a string, and the third is an optional parameter whose default is " ". What is returned is the first parameter, concatenated with the second, using the third.

.. activecode:: ee_opt_params_042
   :tags: OptionalAndKeywordParameters/OptionalParameters.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(together(12, 'cats'), '12 cats', "Testing that together returns the correct string on input (12, 'cats')")
         self.assertEqual(together(17.3, 'birthday cakes'), '17.3 birthday cakes', "Testing that together returns the correct string on input (17.3, 'birthday cakes')")
         self.assertEqual(together(3, 'dogs', ': '), '3: dogs', "Testing that together returns the correct string on input (3, 'dogs', ': ')")
         self.assertEqual(together(493.3, 'beans', ' lima '), '493.3 lima beans', "Testing that together returns the correct string on input (493.3, 'beans', 'lima')")

   myTests().main()   

5. Given is below is the function ``test`` from earlier with some modifications. Correctly call the function indicated by the comments below. 

.. activecode:: ee_Opt_Params_05
   :tags: OptionalAndKeywordParameters/KeywordParameters.rst

   def test(int1, dict1, boolean = True):
       if boolean == True:
           for x in dict1:
               if int1 in dict1:
                   return True
               else:
                   return False
       else:
           return "Bool is false"

   #Call the function with the correct parameters so that the function returns "Bool is false". Save the output to the variable ``output``.



   #Call the function with the correct parameters so that the function returns False. Save the output to the variable ``output2``. 


   #Now, call the function with parameters such that output will be True. Save the output to the variable ``output3``. 


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(output, "Bool is false", "Testing that output is assigned to correct value.")
      def testTwo(self):
         self.assertEqual(output2, False, "Testing that output is assigned to correct value.")
      def testThree(self):
         self.assertEqual(output3, True, "Testing that output is assigned to correct value.")

   myTests().main()

5.1 Below, we've provided the function ``nums`` that you previously defined. You must pass the correct inputs into the function so that it returns the values listed in the ActiveCode window. **Note:** You should only pass positive integers into the function (i.e.: If asked to produce a negative output, do so by using the switch argument!)

.. activecode:: ee_optparams_051
   :tags: OptionalAndKeywordParameters/KeywordParameters.rst

   def nums(int1, mult_int=5, switch=False):
       if switch == False: 
           return int1 * mult_int
       if switch == True: 
           return (int1 * mult_int) * -1

   # Below, make the function return the value 10, and save it to the variable name output1


   # Below, make the function return the value -12, and save it to the variable name output2


   # Below, make the function return the value -25, and save it to the variable name output3


   # Below, make the function return the value -5, and save it to the variable name output4


   # Below, make the function return the value 56, and save it to the variable name output5


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(output1, 10, "Testing that output1 was assigned correctly.")
      def testTwo(self):
         self.assertEqual(output2, -12, "Testing that output2 was assigned correctly.")
      def testThree(self):
         self.assertEqual(output3, -25, "Testing that output3 was assigned correctly.")
      def testFour(self):
         self.assertEqual(output4, -5, "Testing that output4 was assigned correctly.")
      def testFive(self):
         self.assertEqual(output5, 56, "Testing that output5 was assigned correctly.")

   myTests().main() 

5.2 We have provided the fuction from earlier, checkingIfIn with slight variation so that if the first parameter is in the third, then it returns the value. Follow the instructions in the active code window for specific variable assignmemts. 

.. activecode:: ee_opt_params_052
   :tags: OptionalAndKeywordParameters/KeywordParameters.rst, OptionalAndKeywordParameters/OptionalParameters.rst

   def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
       if direction == True:
           if a in d:
               return d[a]
           else:
               return False
       else:
           if a not in d:
               return True
           else:
               return d[a]

   # Call the function so that it returns False and assign that function call to the variable c_false

   # Call the fucntion so that it returns True and assign it to the variable c_true

   # Call the function so that the value of fruit is assigned to the variable fruit_ans

   # Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(c_false, False, "Testing that c_false has the correct value")
      def testTwo(self):
         self.assertEqual(c_true, True, "Testing that c_true has the correct value")
      def testThree(self):
         self.assertEqual(fruit_ans, 19, "Testing that fruit_ans has the correct value")
      def testFour(self):
         self.assertEqual(param_check, 8, "Testing that param_check has the correct value")
         

   myTests().main()


