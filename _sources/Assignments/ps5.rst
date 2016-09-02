:orphan:

..  Copyright (C) Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. assignment for problem set (make sure it has unix ones too)

.. assignments for lecture waivers

.. assignments for end of lecture exercise sets

.. assignments for reading responses

.. assignment for DYU

.. highlight:: python
    :linenothreshold: 500

Activities through 10/19
========================

You have the following graded activities:

* **Before Monday's class 10/10:**
    
  * Read :ref:`While loops<while_chap>`, and do the exercises in that chapter
  * *If you use a Windows computer,* read and do the installation in the (:ref:`instructions for installing git bash <install_git_bash>`). 
  * Read :ref:`Installing a text editor<text_editor_installation>` and the subsequent sections on installing and running python. Try to do the exercises and installations. You will address any installation problems you have (hopefully none!) in section this week. 

  * :ref:`Lecture 10 Waiver <lecture_10_waiver>`

.. usageassignment:: prep_10
    :chapters: IndefiniteIteration
    :subchapters: Installation/TextEditor
    :assignment_name: Prep 10
    :deadline: 2016-10-10 19:40:00
    :pct_required: 80
    :points: 50
  

* **By Tuesday 10/11 11:59 pm:**
    * Read *The Most Human Human*, Chapter 10, p.219-237.
    * Answer `Reading Response 6 <https://umich.instructure.com/courses/105657/assignments/131317>`_ on Canvas.

* **Before Wednesday's class 10/12:**
    
  * Read :ref:`Unix and the Command Line<unix_chapter>`, and try out the commands you learn -- in Terminal, if you use a mac, or Git Bash, if you use Windows.
  * Read `this tutorial on Unix pipes <http://www.ee.surrey.ac.uk/Teaching/Unix/unix3.html>`_ (you can ignore the ``who`` command in the tutorial) and `this tutorial on the Unix command grep <http://www.ee.surrey.ac.uk/Teaching/Unix/unix2.html>`_ (you can scroll down to it on that page).

  * :ref:`Lecture 11 Waiver <lecture_11_waiver>`

.. usageassignment:: prep_11
    :chapters: Unix
    :assignment_name: Prep 11
    :deadline: 2016-10-12 19:40:00
    :pct_required: 80
    :points: 50


* By Friday 10/14 at 6:30 PM:
   * Complete the :ref:`Unix Exercises for Problem Set 5 <problem_set_5_unix>`. (Half the problem set)
   * Save answers to the exercises in Problem Set 5: :ref:`Problem Set 5 <problem_set_5>` (the other half of the problem set)
   * Submit your **Demonstrate Understanding** assignment on Canvas

* **By Wednesday 10/19, after fall break:**
   * Be ready for the midterm exam, see syllabus.

   * Updated study materials will be announced via Canvas.

   * Suggested practice for making best use of the problem sets for review
      * Go through all the problem sets, looking at your answers and fixing them if they weren't correct.
      * Then make another pass through the problem sets. This time, don't look at your past answer or any solution set. Write new answers from scratch. See how quickly you can solve them. Make a note of any problems that take you a long time to solve.
      * Repeat as necessary. On later iterations of this process, only redo the problems that you did not solve immediately on the previous iteration.
  * There are practice problems in all Extra Exercises sections, and some additional ones at the bottom of this page. Some have solutions. They are *not* required, but may be helpful if you are looking for more study material. Try writing your answers out on paper and checking them here!

.. _reading_response_6:

This Week's Reading Responses
-----------------------------

.. external:: rr_6

  `Reading Response 6 <https://umich.instructure.com/courses/105657/assignments/131317>`_ on Canvas.

.. _problem_set_5:

Problem Set
-----------

.. datafile:: timely_file.txt
   :hide:

   Autumn is interchangeably known as fall in the US and Canada, and is one of the four temperate seasons. Autumn marks the transition from summer into winter.
   Some cultures regard the autumn equinox as mid autumn while others, with a longer temperature lag, treat it as the start of autumn then. 
   In North America, autumn starts with the September equinox, while it ends with the winter solstice. 
   (Wikipedia)



.. activecode:: ps_5_1
   :language: python

   **1.** Write code **that will keep printing what the user inputs over and over until the user enters the string "quit".**

   ~~~~
   # Write code here

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testCode(self):
         self.assertIn("print", self.getEditorText(), "Testing code. (Don't worry about actual and expected values)")
         self.assertIn("while", self.getEditorText(), "Testing code. (Don't worry about actual and expected values)")
         self.assertIn("raw_input", self.getEditorText(), "Testing code. (Don't worry about actual and expected values)")

   myTests().main()



.. activecode:: ps_5_2
   :available_files: timely_file.txt
   :language: python

   **2.** We've given you another data file in this problem. It's called ``timely_file.txt``. Write code to figure out which is the most common word in the file. Save the string that is most common word in the file in the variable ``abc``. (Hint: there was a problem on last week's problem set that is very similar to this one.)

   ~~~~
   # Write code here!
        
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testCode(self):
         self.assertNotIn("the", self.getEditorText(), "Testing code (Don't worry about actual and expected values)")

      def testOne(self):
         self.assertEqual(abc, 'the', "testing whether abc is set correctly.")

   myTests().main()


.. activecode:: ps_5_3
   :language: python

   **3.** Below is a function definition. **DO NOT** change it! 

   We have also provided some invocations of that function. Run those and see what they do.

   Below the comment provided in the code window, write a few calls to this function yourself, with whatever appropriate input you want.

   Finally, write a few sentences in comments in the code window that explain what's happening in this function called list_end_with_string. You should explain what happens if a list like ``l`` gets input into this function AND what happens if a list like ``b`` gets input into it. 

   Don't forget to run it and save!

   ~~~~
   # Function definition
   def list_end_with_string(new_list):
       if type(new_list[-1]) == type("hello"):
           return new_list
       new_list.append("the last element is a string no matter what now!")
       return new_list

   # Some function calls and lines that print out the results
   l = [3,46,6]
   b = [4,"hi",10,"12",12,123,"whoa!"]
   print list_end_with_string([1,2])
   print list_end_with_string(l)
   print list_end_with_string(b)

   # Now write a couple invocations of this function yourself below this line.


   # Write your comments here.

.. activecode:: ps_5_4
   :language: python

   **4.** Define a function ``is_prefix`` that takes two strings as inputs and returns the boolean value ``True`` if the first string is a prefix of the second string, but returns ``False`` otherwise.

   ~~~~   
   # Define your function here.


   # Here's a couple example function calls, printing the return value
   # to show you what it is.
   print is_prefix("He","Hello") # should print True
   print is_prefix("Hello","He") # should print False
   print is_prefix("Hi","Hello") # should print False
   print is_prefix("lo","Hello") # should print False
   print is_prefix("Hel","Hello") # should print True
   # Remember, these won't work at all until you have defined a function called is_prefix

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(is_prefix("Big", "Bigger"), True, "Testing whether 'Big' is a prefix of 'Bigger'")
         self.assertEqual(is_prefix("Bigger", "Big"), False, "Testing whether 'Bigger' is a prefix of 'Big'")
         self.assertEqual(is_prefix('ge', 'Bigger'), False, "Testing whether 'ge' is a prefix of 'Bigger'")
         self.assertEqual(is_prefix('Bigge', "Bigger"), True, "Testing whether 'Bigge' is a prefix of 'Bigger'")

   myTests().main()


.. activecode:: ps_5_9
   :available_files: timely_file.txt
   :language: python

   **5.** Define a python function ``grep`` that works just like the unix command ``grep``. Your function should take two inputs, a string and a filename. It should return a list of all the lines in the file that contain the string, and only the lines in the file that contain the string.

   ~~~~
   # Write code here!

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         def solgrep(a, b):
            lines = open(b, 'r').readlines()
            acc = []
            for l in lines:
               if a in l:
                  acc.append(l)
            return acc
         self.assertEqual(grep('autumn', 'timely_file.txt'), solgrep('autumn', 'timely_file.txt'), "testing whether grep('autumn', 'timely_file.txt') returns the right two lines.")
         self.assertEqual(grep('fool', 'timely_file.txt'), solgrep('fool', 'timely_file.txt'), "Testing whether grep('fool', 'timely_file.txt') correctly returns an empty list.")
             
   myTests().main()

.. activecode:: ps_5_6
   :language: python

   **6.** Write code that repeatedly asks the user to input numbers. Keep going until the sum of the numbers is 21 or more. Print out the total.
   ~~~~
   # Write your code here!


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testCode(self):
         self.assertIn("print", self.getEditorText(), "Testing code. (Don't worry about actual and expected values)")
         self.assertIn("while", self.getEditorText(), "Testing code. (Don't worry about actual and expected values)")
         self.assertIn("+", self.getEditorText(), "Testing code. (Don't worry about actual and expected values)")
         self.assertIn("raw_input", self.getEditorText(), "Testing code. (Don't worry about actual and expected values)")

   myTests().main()

.. external:: ps5_dyu

   Complete the `Demonstrate Your Understanding <https://umich.instructure.com/courses/105657/assignments/131288>`_ assignment on Canvas.


Practice Problems: Earlier Semester Material
--------------------------------------------

.. activecode:: rv_1_1
   :language: python
   
   How many characters are in string ``s``? Write code to print the answer.

   How many vowels are in string ``s``? Write code to print the answer.

   How many characters are in each element of list ``lp``? Write code to print the length (number of characters) of each element of the list on a separate line. (Do NOT write 8+ lines of code to do this.)

   The output you should get is:

   ::

      5
      13
      11
      12
      3
      12
      11
      6
   
   ~~~~
   s = "supercalifragilisticexpialidocious"

   lp = ["hello","arachnophobia","lamplighter","inspirations","ice","amalgamation","programming","Python"]
  

.. activecode:: rv_1_2
   :language: python

   What is the value if you add 5 to the integer in ``ic``?

   Add 14 to each element of the list ``dcm`` and print out the result from each computation.

   The output you get should be:

   ::

      23
      18
      81
      103
      98338
      37
      48
      81
      103
      48
      70
      81
      104
      3256
      9907
      19  

   ~~~~  
   ic = 93252759253293024

   dcm = [9, 4, 67, 89, 98324, 23, 34, 67, 89, 34, 56, 67, 90, 3242, 9893, 5]
   

.. activecode:: rv_1_3
   :language: python

   What is the last character of the string value in the variable ``pl``? Find it and print it. This should work no matter what string value ``pl`` has.

   What is the last character of each element in the list ``plts``? Print the last character of each element in the list on a separate line. HINT: You should NOT have to count the length of any of these strings manually/by yourself.

   ~~~~
   pl = "keyboard smashing: sdgahgkslghgisaoghdwkltewighigohdjdslkfjisdoghkshdlfkdjgdshglsdkfdsgkldhfkdlsfhdsklghdskgdlhgsdklghdsgkdslghdskglsdgkhdskfls"

   plts = ["sdsagdsal","sdadfsfsk","dsgsafsal","tomorrow","cooperative","sdgadtx","289,670,452","!)?+)_="]
       

   # Your output should be:
   # l
   # k
   # l
   # w
   # e
   # x
   # 2
   # =


.. activecode:: rv_1_4

   bz = "elementary, my dear watson"
   # Write code to print the fifth character of string bz.
   # Your output should be:
   # e

   # Write code to print the seventh character of string bz.
   # Your output should be:
   # t


.. activecode:: rv_1_5
   :language: python

   Write code to print out the string "Why hello, Irene" using the variable ``nm``.

   Write code to print "Nice to meet you," in front of each element in list ``hlt`` on a separate line. e.g. ``Nice to meet you, mycroft`` and ``Nice to meet you, Lestrade``

   ~~~~
   nm = "Irene"

   hlt = ['mycroft','Lestrade','gregson','sherlock','Joan','john','holmes','mrs hudson']
 

.. activecode:: rv_1_6
   :language: python

   Write code to print the type of the value in the variable ``z``. Before you do so, think: what type is the value in the variable ``z``?
    
   Do the same for the variable ``ab``. 

   ~~~~
   z = True

   ab = 45.6


.. activecode:: rv_1_7
   :language: python

   Write code to print the length of the list ``fancy_tomatoes``.

   Write code to print out each element of the list ``fancy_tomatoes`` on a separate line. (You can do this in just 2 lines of code!)

   Now write code to print out the type of each element of the list fancy_tomatoes on a separate line.

   ~~~~
   fancy_tomatoes = ["hello", 6, 4.24, 8, 20, "newspaper", True, "goodbye", "False", False, 5967834, "6578.31"]

.. activecode:: rv_1_8
   :language: python

   The following code runs, but not the way we expect it to. **You want to print out the first character of each string in the list of strings.** So the following output should print out:

   ::

      h
      g
      l
      4
      6

   Instead, you'll see something different when you run the code. Go through it carefully, understand what is happening, and then fix the code so that the output above appears. Good practice: explain to someone else (or yourself) why exactly it is working incorrectly (semantic errors!) and what is happening on each line, and then fix it.

   ~~~~
   list_of_strings = ["hello","goodbye","lampshade","45","63"]
   for i in list_of_strings:
       if i in list_of_strings:
           print list_of_strings[0]



Functions Practice Problems
---------------------------

We strongly suggest that you try to do the problems yourself before looking at the solutions (which are heavily commented)


.. tabbed:: func_review_1

   .. tab:: Problem

      .. activecode:: fr_1
         :language: python

         Define (and write an invocation of) a function called ``get_vowels`` which takes an **input** of a string and **returns the total number of vowels in the string**.
 
         ~~~~
         # Write your code here!


         # Here's a sample function call.
         print get_vowels("Hello all") # This should print: 3

   .. tab:: Solution

      .. activecode:: fr_1a

         def get_vowels(s):
             vowels = "aeiou"
             total = 0
             for v in vowels:
                 total += s.count(v)
             return total

         print get_vowels("Hello all")


.. tabbed:: func_review_2

   .. tab:: Problem

      .. activecode:: fr_2
         :language: python

         Define (and call) a function called ``sum_a_list`` which **takes any list of integers** and **returns the sum of all integers in the list**.

         ~~~~
         # Write your code here!


         # Here's a sample function call.
         print sum_a_list([1,4,7,5]) # this should print: 17

         # Extra practice:
         # how would you change this function just a LITTLE
         # so that the function could also take a string of digits
         # and return the sum of all those digits.
         # (Hint: to do this, you only have to type 5 more characters.)

   .. tab:: Solution

      .. activecode:: fr_2a
         :language: python

         Define (and call) a function called ``sum_a_list`` which **takes any list of integers** and **returns the sum of all integers in the list**.

         ~~~~
         def sum_a_list(lt): # function definition statement with one parameter
             tot = 0 # intiialize accumulator to 0
             for i in lt: # iterate over the list that is passed in to the function
                 tot = tot + i # each time you get to a new integer in the list, add that integer to the accumulator
             return tot # the for loop is over, so outdent and return the accumulator from the function

         print sum_a_list([1,4,7,5]) # call the function, and print out the result with a print statement

         # Here's the version of the function that will work
         #   for EITHER a list of integers or a string of digits
         def sum_a_list_or_digitstring(lt):
             tot = 0
             for i in lt:
                 tot = tot + int(i)
             return tot

         print sum_a_list_or_digitstring("1475")


.. tabbed:: func_review_3

   .. tab:: Problem

      .. activecode:: fr_3
         :language: python

         Define (and call!) a function called ``common_word`` that **takes a string** and **prints a tuple** of **the most commonly used word in the string** and **the number of times that word is used**. (If there's more than one word that's used most frequently, the function should **print** all of those words.)

         ~~~~
         # Write your code here!


         # Here's a sample function call.
         common_word("hello hello hello is what they said to the class!") # should print: hello


         # For extra practice: you've done something like this before --
         # how would you change this function to print the LONGEST word in the string?

   .. tab:: Solution

      .. activecode:: fr_3a
         :language: python

         Define (and call!) a function called ``common_word`` that **takes a string** and **prints a tuple** of **the most commonly used word in the string** and **the number of times that word is used**. (If there's more than one word that's used most frequently, the function should **print** all of those words.)

         ~~~~
         def common_word(s):
             d = {}
             sp = s.split() # split my string by whitespace, so into 'words'
             for w in sp:
                 if w in d:
                     d[w] = d[w] + 1
                 else:
                     d[w] = 1
             kys = d.keys() # get all the keys from the dict you built, in a list
             most_common = kys[0] # start at the beginning of the list -- this is the most common so far!
             for k in d: # go through the keys in the dictionary
                 if d[k] > d[most_common]: # if the value of the key is bigger than the value of the most common key SO FAR, then you have a new most common key so far
                     most_common = k # so reassign the most_common key
             for ky in d: # now that we know the value of the most common key, go through the keys of the dictionary again
                 if d[ky] == d[most_common]: # for every key that has the same value as the most common one
                     print ky, d[ky] # print the key and its value
             # note that we do NOT return anything here!
             # because we asked to print stuff out

         common_word("hello hello hello is what they said to the class!") # should print: hello

         # Think further: what would happen if you put a return statement where that print statement is? why wouldn't that work?


.. tabbed:: func_review_4
   
   .. tab:: Problem

      .. activecode:: fr_4
         :language: python

          Define (and call!) a function called ``smallest_value_name`` that **takes a dictionary** with key-value pairs of names and integer values, like this: ``{"Nick": 56, "Paul":73, "Jackie":42}``, and **returns the name associated with the *lowest integer value**. (So in the case of that example dictionary, the function should return ``Jackie``.)

         ~~~~
         # Write your code here!

         # Here's a sample call
         df = {"Nick": 56, "Paul":73, "Jackie":42}
         print smallest_value_name(df) # should print: Jackie

   .. tab:: Solution

      .. activecode:: fr_4a
         :language: python

          Define (and call!) a function called ``smallest_value_name`` that **takes a dictionary** with key-value pairs of names and integer values, like this: ``{"Nick": 56, "Paul":73, "Jackie":42}``, and **returns the name associated with the *lowest integer value**. (So in the case of that example dictionary, the function should return ``Jackie``.)

         ~~~~
         # Here's one solution
         def smallest_value_name(d):
             kys = d.keys() # returns a list of the keys in the dictionary d
             m = kys[0] # start off examining the first key in the list
             for k in kys: # for each key in the list of keys
                 if d[k] < d[m]: # if the value associated with that key is smaller than the value associated with the key saved in the variable m (the smallest so far)
                     m = k # then reassign m so it has the same value as this new key, k
             return m # when the loop is over, m contains the key that has the smallest value, so return that from the function!

         # Here's another solution
         def smallest_val_name_diff(d):
             its = d.items() # returns a list of tuples (key, value) in dictionary d and stores it in its
             tn = its[0]
             for t in its:
                 if t[1] < tn[1]:
                     tn = t
             return tn[0]

         # Sample calls of these solution functions
         d_new = {"Nick": 42, "Paul":73, "Jackie":57}
         print smallest_value_name(d_new) # should print Nick

         print smallest_val_name_diff(d_new)
         # should print Nick
