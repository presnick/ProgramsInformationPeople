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

1. Using a while loop, create a list ``numbers`` that contains the numbers 0 through 35. Your while loop should initialize a counter variable to 0. On each iteration, the loop should append the current value of the counter to the list and the counter should increase by 1. The while loop should stop when the counter is greater than 35. 

.. activecode:: ee_07_01
   :tags: IndefiniteIteration/ThewhileStatement.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(numbers, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], "Testing that numbers is assigned to correct values")

   myTests().main()



1.1 Using a while loop, create a list called ``L`` that contains the numbers 0 to 10. (i.e.: Your while loop should initialize a counter variable to 0. On each iteration, the loop should append the current value of the counter variable to ``L`` and then increase the counter by 1. The while loop should stop once the counter variable is greater than 10.)

.. activecode:: ee_ch7_011
   :tags: IndefiniteIteration/ThewhileStatement.rst


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(L, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Testing that L was created correctly.")

   myTests().main()

1.2 Using a while loop, create a list called ``nums`` that contains the numbers 0 though 20. (i.e: your while looop should initialize a counter variable on 0. During each iteration, the loop should append the current value of the counter variable to ``nums`` and then increase the counter by 1. The while loop should stop once the counter variable is greater than 20)

.. activecode:: ee_ch07_012
   :tags: IndefiniteIteration/ThewhileStatement.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(nums, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],"Testing that nums has been assigned the correct elements")

   myTests().main()

2. Create a while loop that initializes a counter at 0 and will run until the counter reaches 50. If the value of the counter is divisible by 10, append the value to the list, ``tens``.  

.. activecode:: ee_ch07_02
   :tags: IndefiniteIteration/ThewhileStatement.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwo(self):
         self.assertEqual(tens, [0, 10, 20, 30, 40, 50], "Testing that tens is assigned to correct values.")

   myTests().main()

2.1 Use a while loop to iterate through the numbers 0 through 35. If a number is divisible by 3, it should be appended to a list called ``three_nums``. 

.. activecode:: ee_ch7_021
   :tags: IndefiniteIteration/ThewhileStatement.rst


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(three_nums, [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33], "Testing that three_nums was created correctly.")

   myTests().main()

2.2 Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called ``eve_nums``.

.. activecode:: ee_ch07_022
   :tags: IndefiniteIteration/ThewhileStatement.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(eve_nums, [0,2,4,6,8,10,12,14], "Testing that eve_nums has been assigned the correct elements")

   myTests().main()

3. Write a function, ``sublist``, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).

.. activecode:: ee_ch07_03
   :tags: IndefiniteIteration/listenerLoop.rst
      
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testThree(self):
         self.assertEqual(sublist([1, 2, 3, 4, 5, 6, 7, 8]), [1, 2, 3, 4], "Testing that sublist([1, 2, 3, 4, 5, 6, 7, 8]) returns [1, 2, 3, 4]")
         self.assertEqual(sublist([5]), [], "Testing that sublist([5]) returns []")
         self.assertEqual(sublist([8, 6, 5]), [8, 6], "Testing that sublist([8, 6, 5]) returns [8, 6]")

   myTests().main()

3.1 Write a function called ``stop_at_four`` that iterates through a list of numbers. Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list. 

.. activecode:: ee_ch7_031
   :tags: IndefiniteIteration/listenerLoop.rst

   def stop_at_four():



   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(stop_at_four([0, 9, 4.5, 1, 7, 4, 8, 9, 3]), [0, 9, 4.5, 1, 7], "Testing the function stop_at_four on the input [0, 9, 4.5, 1, 7, 4, 8, 9, 3].")
         self.assertEqual(stop_at_four([4, 1, 2, 8]), [], "Testing the function stop_at_four on the input [4, 1, 2, 8].")
         self.assertEqual(stop_at_four([4]), [], "Testing the function stop_at_four on the input [4].")

   myTests().main()  

3.2 Write a function called ``check_nums`` that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.

.. activecode:: ee_ch07_032
   :tags: IndefiniteIteration/listenerLoop.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(check_nums([0,2,4,9,2,3,6,8,12,14,7,9,10,8,3]), [0,2,4,9,2,3,6,8,12,14], "Testing that check_nums stops on the correct postion with input [0,2,4,9,2,3,6,8,12,14,7,9,10,8,3]")
         self.assertEqual(check_nums([9,302,4,62,78,97,10,7,8,23,53,1]), [9,302,4,62,78,97,10], "Testing that check_nums stops on the correct position with input [9,302,4,62,78,97,10,7,8,23,53,1]")
         self.assertEqual(check_nums([7,8,3,2,4,51]), [], "Testing that check_nums stops on the correct position with input [7,8,3,2,4,51]")

   myTests().main()



4. Write a function, ``sublist``, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string "STOP" (it should not contain the string "STOP").

.. activecode:: ee_ch07_04
   :tags: IndefiniteIteration/listenerLoop.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(sublist(["bob", "joe", "lucy", "STOP", "carol", "james"]), ["bob", "joe", "lucy"], "Testing that sublist(['bob', 'joe', 'lucy', 'STOP', 'carol', 'james']) returns ['bob', 'joe', 'lucy']")
         self.assertEqual(sublist(["STOP"]), [], "Testing that sublist(['STOP']) returns []")
         self.assertEqual(sublist(["jackie", "paul", "STOP"]), ["jackie", "paul"], "Testing that sublist(['jackie', 'paul', 'STOP']) returns ['jackie', 'paul']")

   myTests().main()

4.1 Write a function called ``stop_at_z`` that iterates through a list of strings. Using a while loop, append each letter to a new list until the string that appears is "z". The function should return the new list. 

.. activecode:: ee_ch7_041
   :tags: IndefiniteIteration/listenerLoop.rst

   def stop_at_z():



   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(stop_at_z(['c', 'b', 'd', 'zebra', 'h', 'r', 'z', 'm', 'a', 'k']), ['c', 'b', 'd', 'zebra', 'h', 'r'], "Testing the function stop_at_z on the input ['c', 'b', 'd', 'zebra', 'h', 'r', 'z', 'm', 'a', 'k'].")
         self.assertEqual(stop_at_z(['zoo', 'zika', 'ozzie', 'pizzazz', 'z', 'pizza', 'zap', 'haze']), ['zoo', 'zika', 'ozzie', 'pizzazz'], "Testing the function stop_at_four on the input ['zoo', 'zika', 'ozzie', 'pizzazz', 'z', 'pizza', 'zap', 'haze'].")
         self.assertEqual(stop_at_z(['z']), [], "Testing the function stop_at_four on the input ['z'].")

   myTests().main() 

5. Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable ``sum2``. Once complete, sum2 should equal sum1.

.. activecode:: ee_ch07_05
   :tags: IndefiniteIteration/ThewhileStatement.rst

   sum1 = 0

   lst = [65, 78, 21, 33]

   for x in lst:
       sum1 = sum1 + x

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFive(self):
         self.assertEqual(sum2, 197, "Testing that sum2 is assigned to correct value.")

   myTests().main()

5.1 Below, we've provided a for loop that sums all the elements of ``list1``. Write code that accomplishes the same task, but instead uses a while loop. Assign the accumulator variable to the name ``accum``. 

.. activecode:: ee_ch7_051
   :tags: IndefiniteIteration/ThewhileStatement.rst

   list1 = [8, 3, 4, 5, 6, 7, 9]

   tot = 0
   for elem in list1: 
       tot = tot + elem

   
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(accum, 42, "Testing that accum has the correct value.")

   myTests().main() 


6. **Challenge:** Write a function called ``beginning`` that takes a list as input and contains a while loop that only stops once the element of the list is the string 'bye'. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If "bye" is the 5th element, the first 4 are returned.) *If you want to make this even more of a challenge, do this without slicing*

.. activecode:: ee_ch07_061
   :tags: IndefiniteIteration/listenerLoop.rst

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):


      def testOne(self):
         self.assertEqual(beginning(['water', 'phone', 'home', 'chapstick', 'market', 'headphones', 'bye', 'stickie notes', 'snapchat', 'facebook', 'social media']), ['water', 'phone', 'home', 'chapstick', 'market', 'headphones'], "Testing that beginning returns the correct list on input ['water', 'phone', 'home', 'chapstick', 'market', 'headphones', 'bye', 'stickie notes', 'snapchat', 'facebook', 'social media']")
         self.assertEqual(beginning(['bye', 'no', 'yes', 'maybe', 'sorta']), [], "Testing that beginning returns the correct list on input ['bye', 'no', 'yes', 'maybe', 'sorta']")
         self.assertEqual(beginning(['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup', 'see yah', 'toodel loo', 'night', 'until later', 'peace', 'bye', 'good-bye', 'g night']),['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup'] , "Testing that beginning returns the correct list on input ['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup', 'see yah', 'toodel loo', 'night', 'until later', 'peace', 'bye', 'good-bye', 'g night']")

   myTests().main()

