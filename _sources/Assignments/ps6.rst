:orphan:

..  Copyright (C) Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. highlight:: python
    :linenothreshold: 500


Activities through 10/28
========================

You have the following graded activities:

* **Before Monday's class 10/24:**
    * Read :ref:`Optional and Keyword Parameters<optional_params_chap>`, and try the exercises in that chapter

.. usageassignment::
    :subchapters: OptionalAndKeywordParameters/OptionalParameters, OptionalAndKeywordParameters/KeywordParameters
    :assignment_name: Prep 12
    :deadline: 2016-10-24 19:40
    :pct_required: 80
    :points: 50

* **By Tuesday 10/25 11:59 pm:**
    * Read `Tutorial on unix diff <http://www.computerhope.com/unix/udiff.htm>`_ (This will help you understand the section of "The Most Human Human" below)
    * Read *The Most Human Human*, Chapter 10, p.237-259.
    * Answer `Reading Response 7 <https://umich.instructure.com/courses/105657/assignments/131318>`_ on Canvas.

    * :ref:`Lecture 12 Challenge Exercises <lecture_12_waiver>`


* **Before Wednesday's class 10/26:**
   * Read :ref:`Tuples<tuples_chap>`, and try the exercises in that chapter
   * Read :ref:`Nested Data Structures and Nested Iteration<nested_chap>`, and try the exercises in that chapter

   * Challenge problems: TBA. No lecture waiver for this lecture. Everyone will get credit. But we strongly encourage attendance for this one.

.. usageassignment::
    :subchapters: Tuples/Tuples, Tuples/TuplePacking, Tuples/TuplesasReturnValues, Tuples/TupleAssignmentwithunpacking, Tuples/UnpackingDictionaryItems, NestedData/ListswithComplexItems, NestedData/NestedDictionaries, NestedData/NestedIteration, NestedData/DebuggingNestedData
    :assignment_name: Prep 13
    :deadline: 2016-10-26 19:40
    :pct_required: 80
    :points: 50


* **By Friday 10/28 at 6:30 PM:**
   * Save answers to the exercises in Problem Set 6: :ref:`Problem Set 6 <problem_set_6>`, including submitting your result for the last question in the **Problem Set 6 Unix Problems** assignment on Canvas!
   * Submit your **Demonstrate Your Understanding** assignment on Canvas (linked in problem set) 

.. _reading_response_7:

This Week's Reading Responses
-----------------------------

.. external:: rr_7

    `Reading Response 7 <https://umich.instructure.com/courses/105657/assignments/131318>`_ on Canvas.


Problem Set
-----------

.. _problem_set_6:


.. activecode:: ps_6_1
   :language: python

   **1.** Use a for loop to print the second element of each tuple in the list ``new_tuple_list``.

   ~~~~
   new_tuple_list = [(1,2),(4, "umbrella"),("chair","hello"),("soda",56.2)]

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testCode(self):
         self.assertIn("2\numbrella\nhello\n56.2", self.getOutput(), "Testing output. (Don't worry about actual and expected values)")

   myTests().main()


.. activecode:: ps_6_2
   :language: python

   **2.** Write three assignment statements with function calls to the function ``give_greeting``:

      * one that will return the string ``Hello, SI106!!!``
      * one that will return the string ``Hello, world!!!``
      * and one that will return the string ``Hey, everybody!``

   You must write only the ``print`` command and function invocations of ``give_greeting`` to earn full credit on this problem.

   You can see the function definition in the code below, but that's only so you can understand exactly what the code is doing, so you can choose how to invoke this function. Feel free to make comments to help yourself understand, but otherwise DO NOT change the function definition code! **HINT:** calling the function with different inputs and printing the results, to see what happens, may be helpful! Make sure your final answer prints out all three of the strings listed above.

   ~~~~
   def give_greeting(greet_word="Hello",name="SI106",num_exclam=3):
       final_string = greet_word + ", " + name + "!"*num_exclam
       return final_string

   #### DO NOT change the function definition above this line (OK to add comments)

   # Write your three print statements with function calls below

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testCode(self):
         print "\n----The following tests are to ensure that you are not hard-coding the values.\n"
         self.assertNotIn("Hello, SI106!!!", self.getEditorText(), "Testing to see if you've put Hello, SI106!!! in your code to hard-code.")
         self.assertNotIn("Hello, world!!!", self.getEditorText(), "Testing to see if you've put Hello, world!!! in your code to hard-code.")
         self.assertNotIn("Hey, everybody!", self.getEditorText(), "Testing code. (Don't worry about actual and expected values)")
         self.assertIn("print", self.getEditorText(), "Testing to see if you've put Hey, everybody! in your code to hard-code.")
      def testOutput(self):
         self.assertIn("Hello, SI106!!!", self.getOutput(), "Testing output. (Don't worry about actual and expected values)")
         self.assertIn("Hello, world!!!", self.getOutput(), "Testing output. (Don't worry about actual and expected values)")
         self.assertIn("Hey, everybody!", self.getOutput(), "Testing output. (Don't worry about actual and expected values)")

   myTests().main()


.. activecode:: ps_6_3
   :language: python

   **3.** Define a function called ``mult_both`` whose input is two integers, whose default parameter values are the integers 3 and 4. The function's return value should be the two input integers multiplied together.

   ~~~~
   # Write your code here

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testCode(self):
         self.assertIn("3", self.getEditorText(), "Testing code. (Don't worry about actual and expected output)")
         self.assertIn("4", self.getEditorText(), "Testing code. (Don't worry about actual and expected output)")

      def testOne(self):
         self.assertEqual(mult_both(), 12, "Testing whether your function works as expected (calling the function mult_both)")
         self.assertEqual(mult_both(5,10), 50, "Testing whether your function works as expected (calling the function mult_both)")

   myTests().main()


.. activecode:: ps_6_4
   :language: python

   **4.** You can get data from Facebook that has nested structures which represent posts, or users, or various other types of things on Facebook. We won't put any of our actual Facebook group data on this textbook, because the textbook is publicly available on the internet, but here's a structure that is almost exactly the same as the real thing, with fake data.

   Notice that the stuff in the variable ``fb_data`` is basically a big nested dictionary, with dictionaries and lists, strings and integers, inside it as keys and values. 

   (Later in the course we'll learn how to get this kind of thing directly FROM facebook, and then it will be a bit more complicated and have real information from our Facebook group.)

   **FIRST,** look through the data structure saved in the variable ``fb_data`` to get a sense for it. 

   Here are some questions to consider. We won't grade your answers to these questions, but we suggest that you write them in the code as comments. They may help you think through this big nested data structure. You can test your answers using print statements. e.g. ``print type(fb_data["data"])``
      
   * What type is the structure saved in the variable ``fb_data``?
   * What type does the expression ``fb_data["data"]`` evaluate to?
   * What about ``fb_data["data"][1]``?
   * What about ``fb_data["data"][0]["from"]``?
   * What about ``fb_data["data"][0]["id"]``?

   Write a line of code to assign the value of the first message (``"This problem might..."`` from the big ``fb_data`` data structure to a variable called ``first_message``. Do not hard code your answer! (So, write it in terms of ``fb_data``, so that it would work with any content stored in the variable ``fb_data`` which has the same structure as that of what we gave you.)

   Write a second line of code to assign the value of the name of the second person who posted (``"John Smythe"``) to a variable called ``second_name``. Do not hard code your answer!

   ~~~~
   fb_data = {
      "data": [
         {
         "id": "2253324325325123432madeup", 
         "from": {
         "id": "23243152523425madeup", 
         "name": "Jane Smith"
         }, 
         "to": {
            "data": [
               {
                  "name": "Your Facebook Group", 
                  "id": "432542543635453245madeup"
               }
            ]
         }, 
         "message": "This problem might use the accumulation pattern, like many problems do", 
         "type": "status", 
         "created_time": "2014-10-03T02:07:19+0000", 
         "updated_time": "2014-10-03T02:07:19+0000"
         }, 
           
         {
         "id": "2359739457974250975madeup", 
         "from": {
         "id": "4363684063madeup", 
         "name": "John Smythe"
         }, 
         "to": {
            "data": [
               {
                  "name": "Your Facebook Group", 
                  "id": "432542543635453245madeup"
               }
            ]
         }, 
         "message": "Here is a fun link about programming", 
         "type": "status", 
         "created_time": "2014-10-02T20:12:28+0000", 
         "updated_time": "2014-10-02T20:12:28+0000"
      }]
   }




   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testCode(self):
         self.assertNotIn("This problem might use the accumulation pattern, like many problems do", self.getEditorText()[1058:], "Testing code. (Don't worry about expected and actual output)")
         self.assertNotIn("John Smythe", self.getEditorText()[1058:], "Testing code. (Don't worry about expected and actual output")

      def testOne(self):
         self.assertEqual(first_message, fb_data['data'][0]['message'], "testing whether first_message was set correctly")
      def testTwo(self):
         self.assertEqual(second_name, fb_data['data'][1]['from']['name'], "testing whether second_name was set correctly")

   myTests().main()


.. activecode:: ps_6_hangman_base
   :language: python

   **5.** In the next few questions, you’ll build components and then a complete program that lets people play Hangman. Below is an image from the middle of a game...

   .. image:: Figures/HangmanSample.JPG

   See the flow chart below for a better understanding of what's happening in the code for the Hangman game overall.
 
   .. image:: Figures/HangmanFlowchart.jpg

   Your first task is just to understand the logic of the program, by matching up elements of the flow chart above with elements of the code below. In later problems, you'll fill in a few details that aren't fully implemented here.  

   For this question, write which lines of code go with which lines of the flow chart box, by answering the questions in comments at the bottom of this activecode box. 

   .. note::

      You may find it helpful to run this program in order to understand it. It will tell you feedback about your last guess, but won't tell you where the correct letters were or how much health you have, and it won't stop if you guess all the letters, so you can't *really* play with this version of the code. Allowing the game to do those things is what you'll do in later problems!

   ~~~~
   def blanked(word, guesses):
       return "blanked word"

   def health_prompt(x, y):
       return "health prompt"

   def game_state_prompt(txt ="Nothing", h = 6, m_h = 6, word = "HELLO", guesses = ""):
       res = "\n" + txt + "\n"
       res = res + health_prompt(h, m_h) + "\n"
       if guesses != "":
           res = res + "Guesses so far: " + guesses.upper() + "\n"
       else:
           res = res + "No guesses so far" + "\n"
       res = res + "Word: " + blanked(word, guesses) + "\n"

       return(res)

   def main():
       max_health = 3
       health = max_health
       secret_word = raw_input("What's the word to guess? (Don't let the player see it!)")
       secret_word = secret_word.upper() # everything in all capitals to avoid confusion
       guesses_so_far = ""
       game_over = False

       feedback = "let's get started"

       # Now interactively ask the user to guess
       while not game_over:
           prompt = game_state_prompt(feedback, health, max_health, secret_word, guesses_so_far)
           next_guess = raw_input(prompt)
           next_guess = next_guess.upper()
           feedback = ""
           if len(next_guess) != 1:
               feedback = "I only understand single letter guesses. Please try again."
           elif next_guess in guesses_so_far:
               feedback = "You already guessed that"
           else:
               guesses_so_far = guesses_so_far + next_guess
               if next_guess in secret_word:
                   if blanked(secret_word, guesses_so_far) == secret_word:
                       feedback = "Congratulations"
                       game_over = True
                   else:
                       feedback = "Yes, that letter is in the word"
               else: # next_guess is not in the word secret_word
                   feedback = "Sorry, " + next_guess + " is not in the word."
                   health = health - 1
                   if health <= 0:
                       feedback = " Waah, waah, waah. Game over."
                       game_over= True
    
       print(feedback)
       print("The word was..." + secret_word)

   import sys #don't worry about this line; you'll understand it next week 
   sys.setExecutionLimit(60000)     # let the game take up to a minute, 60 * 1000 milliseconds
   main()

.. activecode:: ps_6_5

   Answer the questions in comments below. (The answers should be a number that corresponds to a line of code in the Hangman game code above!)
   ~~~~

   #What line(s) of code in the above code window do what's mentioned in the flowchart's Box 1? 


   #What line(s) of code do what's mentioned in Box 2?


   #What line(s) of code do what's mentioned in Box 3?

 
   #What line(s) of code do what's mentioned in Box 4?


   #What line(s) of code do what's mentioned in Box 5?


   #What line(s) of code do what's mentioned in Box 6?


   #What line(s) of code do what's mentioned in Box 7?


   #What line(s) of code do what's mentioned in Box 8?


   #What line(s) of code do what's mentioned in Box 9?


   #What line(s) of code do what's mentioned in Box 10?


   #What line(s) of code do what's mentioned in Box 11?


.. activecode:: ps_6_6
   :language: python

   **6.** The next task you have is to create a correct version of the ``blanked`` function. It should take 2 inputs: a word, and a string of the letters that have been guessed already. 

   It should return a string with the same number of characters as the word, but with the UNrevealed characters replaced by an underscore (a ``_``). 

   **HINT:** Iterate through the letters in the word, accumulating characters as you go. If you try to iterate through the guesses, it's harder.

   ~~~~       
   # Sample calls to this function
   # (Remember, these won't work until you define the function blanked)
   print blanked("hello", "elj")
   #should output _ell_
   print blanked("almost","amsvr")
   # should output a_m_s_ 


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(blanked('hello', 'elj'), "_ell_", "testing blanking of hello when e,l, and j have been guessed.")
         self.assertEqual(blanked('hello', ''), '_____', "testing blanking of hello when nothing has been guessed.")
         self.assertEqual(blanked('ground', 'rn'), '_r__n_', "testing blanking of ground when r and n have been guessed.")
         self.assertEqual(blanked('almost', 'vrnalmqpost'), 'almost', "testing blanking of almost when all the letters have been guessed.")

   myTests().main()


.. activecode:: ps_6_7
   :language: python

   **7.** Now you have to create a good version of the ``health_prompt`` function: 

   Define a function called ``health_prompt``. The first parameter should be the current health the player has (an integer), and the second parameter should be the maximum health a player can have (an integer). 

   The function should return a string with ``+`` signs for the current health, and ``-`` signs for the health that has been lost so far.

   ~~~~
   # Define your function here.




   # Sample invocations of the function.

   print health_prompt(3, 7)
   #this statement should produce the output
   # +++----

   print health_prompt(0, 4)
   #this statement should produce the output
   # ----

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(health_prompt(3,7), "+++----", "Testing health_prompt(3,7)")
         self.assertEqual(health_prompt(0,4), "----", "Testing health_prompt(0,4)")
         self.assertEqual(health_prompt(5,5), "+++++", "Testing health_prompt(5,5)")

   myTests().main()


.. external:: problem_set_6_8

   You have all the pieces of a fully functioning hangman program! Now you can put together a program on your own computer to play Hangman.

   In the below code window is all of the code for the hangman program, *except* for the two functions you just defined in problems 6 and 7. (It does not include the special lines allowing it to run in the textbook, which won't work on your native machine, and it does not have those function definitions, so this code will not run as expected! It's just provided here for you to copy.)

   Copy your two function definitions, from the last two problems, into a *Python file* on your computer, just like ``prog1.py`` from last week, except much more complicated a program. Save that file as ``hangman.py``.

   Then copy all the code in the box below into that file, too, underneat the function definitions you just copied in.

   Finally, make one more change to the program: add a little bit of code so that after you enter the secret word to guess, print 27 new empty lines, such that the secret word will be pushed up out of your screen and the person who guesses the word will not be able to see it.

   Save this Python program, and run it using the command line: ``cd`` to the correct directory where you saved the file, and then type ``python hangman.py``, as you learned last week.

   **Submit** your python file called hangman.py AND a screenshot of you successfully running the code and playing the game to `Problem 6 Unix Exercises <https://umich.instructure.com/courses/105657/assignments/151663>`_ on Canvas.

   .. sourcecode:: python
     
      def game_state_prompt(txt ="Nothing", h = 6, m_h = 6, word = "HELLO", guesses = ""):
          res = "\n" + txt + "\n"
          res = res + health_prompt(h, m_h) + "\n"
          if guesses != "":
              res = res + "Guesses so far: " + guesses.upper() + "\n"
          else:
              res = res + "No guesses so far" + "\n"
          res = res + "Word: " + blanked(word, guesses) + "\n"
   
          return(res)

      def main():
          max_health = 3
          health = max_health
          secret_word = raw_input("What's the word to guess? (Don't let the player see it!)")
          secret_word = secret_word.upper() # everything in all capitals to avoid confusion
          guesses_so_far = ""
          game_over = False

          feedback = "let's get started"

          # Now interactively ask the user to guess
          while not game_over:
              prompt = game_state_prompt(feedback, health, max_health, secret_word, guesses_so_far)
              next_guess = raw_input(prompt)
              next_guess = next_guess.upper()
              feedback = ""
              if len(next_guess) != 1:
                  feedback = "I only understand single letter guesses. Please try again."
              elif next_guess in guesses_so_far:
                  feedback = "You already guessed that"
              else:
                  guesses_so_far = guesses_so_far + next_guess
                  if next_guess in secret_word:
                      if blanked(secret_word, guesses_so_far) == secret_word:
                          feedback = "Congratulations"
                          game_over = True
                      else:
                          feedback = "Yes, that letter is in the word"
                  else: # next_guess is not in the word secret_word
                      feedback = "Sorry, " + next_guess + " is not in the word."
                      health = health - 1
                      if health <= 0:
                          feedback = " Waah, waah, waah. Game over."
                          game_over= True

          print(feedback)
          print("The word was..." + secret_word)

      main()


.. external:: ps6_dyu

    Complete this week's `Demonstrate Your Understanding <https://umich.instructure.com/courses/105657/assignments/131289>`_ assignment on Canvas.
