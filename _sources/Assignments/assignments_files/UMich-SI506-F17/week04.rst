:orphan:

..  Copyright (C) Jackie Cohen, Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


Activities: Week 4
==================

* **Before Monday's class:**

  * Review :ref:`Functions<functions_chap>` (not graded, but recommended)
  * Read :ref:`Optional and Keyword Parameters<optional_params_chap>`


* **Before Wednesday's class:**

  * Read :ref:`Tuples<tuples_chap>`
  * Read the :ref:`Unix<unix_chapter>` chapter and try the exercises in that chapter on your computer
  * Read `this tutorial on Unix pipes <http://www.ee.surrey.ac.uk/Teaching/Unix/unix3.html>`_ (you can ignore the ``who`` command in the tutorial) and `this tutorial on the Unix command grep <http://www.ee.surrey.ac.uk/Teaching/Unix/unix2.html>`_ (you can scroll down to it on that page).
  * Read :ref:`Installing a text editor<text_editor_installation>` section for background, and make sure you have a text editor installed. (You can leave the rest of the installation chapter aside; it may contain some outdated information!) We recommend `Atom <https://atom.io/>`_, which is only available for Mac, or `Sublime Text <https://www.sublimetext.com/>`_, which is available for Windows OR Mac. **Microsoft Word or NotePad will not work for programs! You must install a Text Editor program that works for writing Python code.**
  * Read the `Python installation instructions <https://umich.instructure.com/courses/172984/assignments/329369>`_ on Canvas.


* **Before Sunday 2/05 at 11:59 PM:**

  * Complete all of the below :ref:`Problem Set 4<problem_set_4>` and the Demonstrate Your Understanding assignment for this week.
  * Complete the :ref:`Unix Exercises<problem_set_4_unix>` and submit screenshots to Canvas. Clicking that link will bring you to the instructions.


.. note::

  Note that your problem set 4 this week is only worth **500 points**. There are installation exercises and file system exercises ("Unix Exercises") that will supply the remaining 500 points for this week's 1000.

.. datafile:: timely_file.txt
   :hide:

   Autumn is interchangeably known as fall in the US and Canada, and is one of the four temperate seasons. Autumn marks the transition from summer into winter.
   Some cultures regard the autumn equinox as mid autumn while others, with a longer temperature lag, treat it as the start of autumn then. 
   In North America, autumn starts with the September equinox, while it ends with the winter solstice. 
   (Wikipedia)


Problem Set
-----------
.. _problem_set_4:

.. activecode:: ps_4_01
   :available_files: timely_file.txt
   :language: python
   :autograde: unittest

   **1.** We've given you another data file in this problem. It's called ``timely_file.txt``. Write code to figure out which is the most common word in the file. Save the string that is most common word in the file in the variable ``abc``. (Hint: you had a problem quite similar to this one in PS3!)

   ~~~~
   # Write code here!
        
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testCode(self):
         self.assertNotIn("= 'the'", self.getEditorText(), "Testing code input (Don't worry about actual and expected values)")
         self.assertIn("open",self.getEditorText(),"Testing that you have probably opened the file (Don't worry about actual and expected values)")

      def testOne(self):
         self.assertEqual(abc, 'the', "testing whether abc is set correctly.")

   myTests().main()

In the next few questions, you’ll build components and then a complete program that lets people play Hangman.

Below is an image from the middle of a game...

.. image:: Figures/HangmanSample.JPG

Your first task is just to understand the logic of the program, by matching up elements of the flow chart above with elements of the code below. In later problems, you'll fill in a few details that aren't fully implemented here.  

You may find it helpful to run this program in order to understand it. It will tell you feedback about your last guess, but won't tell you where the correct letters were or how much health you have in the game, and it won't stop if you guess all the letters, so you can't *really* play with this version of the code here. (It can also go on for a very long time, until you exceed the time limit in the code window, unless you cancel it yourself.) Allowing the game to do those things (manage health, show you the word you've guessed so far) comes from code you will write in later problems!

.. activecode:: ps_4_hangman_code
  :hidecode:

  This is the base code for a Hangman game, without some of the important useful functionality. (If you have never played Hangman, you can go to ``https://en.wikipedia.org/wiki/Hangman_(game)`` for an explanation of what it is.)
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
  main() # invoke the main() game function

See the flow chart below for a better understanding of what's happening in the code for the Hangman game overall. Your first task is just to understand the logic of the program, by matching up elements of the flow chart above with single numeric lines of the code below (which line of code corresponds to the box?). Answer in comments, below. **Each answer should be no more than 2 numbers that represent lines of code. Each question can be answered with 1 or 2 line numbers!**

In later problems, you'll fill in a few details that aren't fully implemented in the code above.
 
.. image:: Figures/HangmanFlowchart.jpg

.. activecode:: ps_4_02

   # What line(s) of code in the above code window do what's mentioned in the flowchart's Box 1? 

   # What line(s) of code do what's mentioned in Box 2?

   #What line(s) of code do what's mentioned in Box 3?
 
   # What line(s) of code do what's mentioned in Box 4?

   # What line(s) of code do what's mentioned in Box 5?

   # What line(s) of code do what's mentioned in Box 6?

   # What line(s) of code do what's mentioned in Box 7?

   # What line(s) of code do what's mentioned in Box 8?

   # What line(s) of code do what's mentioned in Box 9?

   # What line(s) of code do what's mentioned in Box 10?

   # What line(s) of code do what's mentioned in Box 11?


.. activecode:: ps_4_03
   :language: python
   :autograde: unittest

   **3.** The next task you have is to create a correct version of the ``blanked`` function. It should take 2 inputs: a word, and a string of the letters that have been guessed already. 

   It should return a string with the same number of characters as the word, but with the UNrevealed characters replaced by an underscore (a ``_``). 

   **HINT:** Iterate through the letters in the word, accumulating characters as you go. If you try to iterate through the guesses, it's harder.

   ~~~~   
   # Define your function here.


   # Sample calls to this function
   # (Remember, these won't work until you define the function blanked)
   print(blanked("hello", "elj"))
   #should output _ell_
   print(blanked("almost","amsvr"))
   # should output a_m_s_ 


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(blanked('hello', 'elj'), "_ell_", "testing blanking of hello when e,l, and j have been guessed.")
      def testTwo(self):
         self.assertEqual(blanked('hello', ''), '_____', "testing blanking of hello when nothing has been guessed.")
      def testThree(self):
         self.assertEqual(blanked('ground', 'rn'), '_r__n_', "testing blanking of ground when r and n have been guessed.")
      def testFour(self):
         self.assertEqual(blanked('almost', 'vrnalmqpost'), 'almost', "testing blanking of almost when all the letters have been guessed.")

   myTests().main()

.. activecode:: ps_4_04
    :autograde: unittest

    **4.** Now you have to create a good version of the ``health_prompt`` function: Define a function called ``health_prompt``. The first parameter should be the current health the player has (an integer), and the second parameter should be the maximum health a player can have (an integer). The function should return a string with ``+`` signs for the current health, and ``-`` signs for the health that has been lost so far.
    ~~~~
    # Define your function here.




    # Sample invocations of the function.

    print(health_prompt(3, 7))
    #this statement should produce the output
    #health: +++----

    print(health_prompt(0, 4))
    #this statement should produce the output
    #health: ----

    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(health_prompt(3,7), "+++----", "Testing health_prompt(3,7)")
      def testTwo(self):
         self.assertEqual(health_prompt(0,4), "----", "Testing health_prompt(0,4)")
      def testThree(self):
         self.assertEqual(health_prompt(5,5), "+++++", "Testing health_prompt(5,5)")

    myTests().main()

In class, you'll see these things all put together. Soon, you'll put these together yourself and run your completed hangman program on your own computer, instead of in the textbook.





.. _problem_set_4_unix:

Problem Set 4: Unix Exercises
-----------------------------

For each step of the Unix part of this problem set, please take a screenshot that shows us the command(s) you typed and the results. Save the screenshots as ``step1.jpg`` (or ``.png``), ``step2.jpg``, etc. Upload them all to `the Unix Exercises <https://umich.instructure.com/courses/172984/assignments/329372>`_ assignment on Canvas.

Following the Unix exercises, there are a few Activecode windows and directions for Python exercises which comprise the second part of this problem set.

----------

.. external:: problem_set_4_unix_1

    1. Open the text editor you installed: Sublime Text. You will be creating and saving 4 different files to your ``Desktop``. 

    **In the first file,** put the following:

    .. sourcecode:: python

        print("hello world")

    Save the file as ``prog1.py``. You've now saved a Python program on your computer.



    **In the second file,** put the following:

    .. sourcecode:: python

        def greeting(x):
            return "hello " + x

        print(greeting("there"))

    Save this file as ``prog2.py``.
    


    **In the third file,** put the following:

    :: 

        this is a file
        it has 
        multiple
        lines

    Save this as ``unix_test_text.txt``.


    **In the fourth file,** put the following:

    ::

        here is another file
        what a wonderful
        story this is

    Save this file as ``another_text.txt``.

    No need to take a screenshot of the file saving since you need them for the rest of the exercises, but if it's not working or is confusing, let staff know right away so we can help.

.. external:: problem_set_4_unix_2

    2. Open your Command Prompt program -- Terminal or Git Bash. ``cd`` to your ``Desktop``, as you saw in the chapter. Then type ``ls``. You should see a list of all file names on your Desktop, including the files you just saved in step 1. If you have any directories saved in your Desktop, you'll also see those names, of course. Take a screenshot that shows this worked for you.

.. external:: problem_set_4_unix_3

    3. You now want to make a new directory called ``new_class_programs`` in your ``Desktop``, and copy ``prog1.py`` and ``prog2.py`` into it. (Note that files will NOT disappear from your desktop when you've completed this step. There should be a copy of each file in both places.) 

    Use Unix commands to do this, and take a screenshot of the commands you use + evidence they worked. (Hint: using commands like ``cd`` and ``ls`` and ``pwd`` can help you check what you've done when you're creating directories and copying files around! It will also be useful to remind yourself of what ``mkdir`` and ``cp`` do.) 

    There is more than one perfectly reasonable way to complete this exercise, but all ways use a similar set of Unix commands.

.. external:: problem_set_4_unix_4
    
    4. Now, you want to create a new directory *inside* the ``new_class_programs`` directory, called ``text_files``, and copy both ``unix_test_text.txt`` and ``another_text.txt`` into *that* folder. Use Unix commands to do this. 

    When you've completed that, change directories to be inside that folder in your command prompt, and use the ``pwd`` command to show the full path of your location. (It should look *something like* this: ``/Users/Jackie/Desktop/new_class_programs/text_files``)

    Take a screenshot showing that these things worked for you. Your screenshot should show the command you typed + evidence it worked.

.. external:: problem_set_4_unix_5

    5. You want to see what content is inside each of your files. Use a unix command to view the content of ``prog2.py`` before you open it. Take a screenshot to show that this worked.

.. external:: problem_set_4_unix_6

    6. You want to concatenate the 2 text files inside the ``text_files`` folder together, and save the result in a file called ``big_story.txt``, which should also be inside that directory. Use unix commands to do this. (Hint: You'll probably need more than 1 typed in the same line.)

.. external:: problem_set_4_unix_7

    7. You now want to see a list of all the files and/or directories inside your ``new_class_programs`` folder whose names include ``text``. Use Unix commands to do this. (Hint: You'll need pipe (``|``) and ``grep``, and ``ls``.)

.. external:: problem_set_4_unix_8

    8. Now that you have a bunch of practice with the unix command prompt, it's time to run Python natively on your computer. You've saved 2 Python files that are in your ``~/Desktop/new_class_programs`` directory. Go there in your command prompt, and run ``prog2.py`` by typing ``python prog2.py`` at the prompt. Take a screenshot of what happens. 

    (Feel free to also play around -- you know a lot of programming now, and you can run it all on your computer, but it will look a little bit different in the command prompt than it did in the textbook.)

.. note::

    You may find/know about another way to run your python program directly from Sublime Text or Atom. We have found that this will not work for everything you need to do throughout the semester. Therefore, it's very important that you learn how to run your python programs from the unix command prompt, including figuring out how to connect to the right directory with the unix ``cd`` command. You will only get credit for these unix problems if your screenshots show that you ran the programs from the unix command prompt.

.. note::

  **This above is very important for the rest of the semester.** Starting with Problem Set 5, ALL of your problem sets will be turned in via Canvas, and you will be writing code in a text editor and running it on your own computer. If you have any trouble running Python natively (on your computer), let an instructor know *right away.*
