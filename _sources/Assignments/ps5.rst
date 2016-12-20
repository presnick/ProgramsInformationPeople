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

Activities through 10/19 (through Fall Break)
=============================================

You have the following graded activities:

* **Before Monday's class 10/10:**
    
  * Read :ref:`While loops<while_chap>`, and do the exercises in that chapter
  * *If you use a Windows computer,* read and do the installation in the (:ref:`instructions for installing git bash <install_git_bash>`). 
  * Read :ref:`Installing a text editor<text_editor_installation>` and the subsequent sections on installing and running python. Try to do the exercises and installations. You will address any installation problems you have (hopefully none! Fingers crossed) in section this week. 

  * :ref:`Lecture 10 Waiver <lecture_10_waiver>`

.. usageassignment::
    :subchapters: IndefiniteIteration/intro-indefiniteiteration, IndefiniteIteration/ThewhileStatement, IndefiniteIteration/listenerLoop, Installation/TextEditor
    :assignment_name: Prep 10
    :deadline: 2016-10-10 19:40
    :pct_required: 80
    :points: 50
  
* **By Tuesday 10/11 11:59 pm:**
    * Read *The Most Human Human*, Chapter 10, p.219-237.
    * Answer `Reading Response 6 <https://umich.instructure.com/courses/105657/assignments/131317>`_ on Canvas.

* **Before Wednesday's class 10/12:**
    
  * Read :ref:`Unix and the Command Line<unix_chapter>`, and try out the commands you learn -- in Terminal, if you use a mac, or Git Bash, if you use Windows.
  * Read `this tutorial on Unix pipes <http://www.ee.surrey.ac.uk/Teaching/Unix/unix3.html>`_ (you can ignore the ``who`` command in the tutorial) and `this tutorial on the Unix command grep <http://www.ee.surrey.ac.uk/Teaching/Unix/unix2.html>`_ (you can scroll down to it on that page).

  * **now with a new text box you need to complete before lecture** :ref:`Lecture 11 Waiver <lecture_11_waiver>`

.. usageassignment::
    :subchapters: Unix/CommandPrompt, Unix/FoldersAndPaths, Unix/DirectoriesAndCopying, Unix/lessCommand
    :assignment_name: Prep 11
    :deadline: 2016-10-12 19:40
    :pct_required: 80
    :points: 50


* By Friday 10/14 at 6:30 PM:
   * Save answers to the code exercises in Problem Set 5: :ref:`Problem Set 5 <problem_set_5>` (Half of the problem set, which is just like the usual ones, but shorter)
   * Complete the :ref:`Unix Exercises for Problem Set 5 <problem_set_5_unix>`. (Half the problem set, which you will also find at the botton of this page)
   
   * Submit your **Demonstrate Understanding** assignment on Canvas

* **By Wednesday 10/19, after fall break:**
   * Be ready for the midterm exam, see syllabus.

   * Updated study materials will be announced via Canvas.

   * Suggested practice for making best use of the problem sets for review
      * Go through all the problem sets, looking at your answers and fixing them if they weren't correct.
      * Then make another pass through the problem sets. This time, don't look at your past answer or any solution set. Write new answers from scratch. See how quickly you can solve them. Make a note of any problems that take you a long time to solve.
      * Repeat as necessary. On later iterations of this process, only redo the problems that you did not solve immediately on the previous iteration.

   * There are practice problems in all chapters under ExtraExercises, and some additional ones at the bottom of this page. Some have solutions. They are *not* required, but may be helpful if you are looking for more study material. Try writing your answers out on paper and checking them here!

.. _reading_response_6:

This Week's Reading Responses
-----------------------------

.. external:: rr_6

  `Reading Response 6 <https://umich.instructure.com/courses/105657/assignments/131317>`_ on Canvas.

.. _problem_set_5:

Problem Set
-----------

**Problem Set 5 is in DRAFT form. You may save answers to the problems and try them out, but until we remove this notification, we cannot guarantee there will not be small changes. It will not change dramatically.**


.. datafile:: timely_file.txt
   :hide:

   Autumn is interchangeably known as fall in the US and Canada, and is one of the four temperate seasons. Autumn marks the transition from summer into winter.
   Some cultures regard the autumn equinox as mid autumn while others, with a longer temperature lag, treat it as the start of autumn then. 
   In North America, autumn starts with the September equinox, while it ends with the winter solstice. 
   (Wikipedia)

**IMPORTANT:** The first half of the problem set is to be done on your own computer, with Unix commands. You can find it :ref:`right here <problem_set_5_unix>`, below.

We are going to begin to move toward executing Python programs on your own computers after the midterm! If you have *installation* problems, we want to resolve them soon, but first and foremost, you should concentrate on the concepts this week, and on understanding Unix commands.

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
   :autograde: unittest

   **2.** We've given you another data file in this problem. It's called ``timely_file.txt``. Write code to figure out which is the most common word in the file. Do not hard code! Save the string that is most common word in the file in the variable ``abc``. (Hint: there was a problem on last week's problem set that is very similar to this one.)

   ~~~~
   # Write code here!
        
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(abc, 'the', "testing whether abc is set correctly.")

   myTests().main()


.. activecode:: ps_5_3
   :language: python
   :autograde: unittest

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
   :autograde: unittest

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
   class myTests(TestCaseGui):
   from unittest.gui import TestCaseGui

         def testOne(self):
            self.assertEqual(is_prefix("Big", "Bigger"), True, "Testing whether 'Big' is a prefix of 'Bigger'")
            self.assertEqual(is_prefix("Bigger", "Big"), False, "Testing whether 'Bigger' is a prefix of 'Big'")
            self.assertEqual(is_prefix('ge', 'Bigger'), False, "Testing whether 'ge' is a prefix of 'Bigger'")
            self.assertEqual(is_prefix('Bigge', "Bigger"), True, "Testing whether 'Bigge' is a prefix of 'Bigger'")
            self.assertEqual(is_prefix('rid', 'Bridge'), False, "Testing whether 'rid' is a prefix of 'Bridge")
            self.assertEqual(is_prefix('Bridge', 'Bridge'), True, "Testing whether 'Bridge' is a prefix of 'Bridge'")
            
   myTests().main()


.. activecode:: ps_5_9
   :available_files: timely_file.txt
   :language: python
   :autograde: unittest

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


.. _problem_set_5_unix:

**Now, the second part of Problem Set 5!** At the end of this part of the problem set, you will run a Python program on your computer for the first time in this course. The other Unix commands you have learned will be very useful when you start programming entirely on your own computer, writing programs in a text editor, rather than programming in the browser, on our textbook, and are closely connected to the processes you use when you run a Python program on your computer. They will help you be able to not just run Python programs, but deal comfortably with your computer's file system while you do that.

**This is part of your Problem Set 5. It is graded. The other part is writing Python code, in Activecode windows, above.**

For each step of this assignment, please take a screenshot that shows us the command(s) you typed and the results. Save the screenshots as ``step1.jpg`` (or ``.png``), ``step2.jpg``, etc. Upload them all to `the PS 5 Unix Exercises <https://umich.instructure.com/courses/105657/assignments/139051>`_ assignment on Canvas.

----------

.. external:: problem_set_5_unix_1

    1. Open the text editor you installed: Sublime Text. You will be creating and saving 4 different files to your ``Desktop``. 

    **In the first file,** put the following:

    .. sourcecode:: python

        print "hello world"

    Save the file as ``prog1.py``. You've now saved a Python program on your computer!



    **In the second file,** put the following:

    .. sourcecode:: python

        def greeting(x):
            return "hello " + x

        print greeting("there")

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

.. external:: problem_set_5_unix_2

    2. Open your Command Prompt program -- Terminal or Git Bash. ``cd`` to your ``Desktop``, as you saw in the chapter. Then type ``ls``. You should see a list of all file names on your Desktop, including the files you just saved in step 1. If you have any directories saved in your Desktop, you'll also see those names, of course. Take a screenshot that shows this worked for you.

.. external:: problem_set_5_unix_3

    3. You now want to make a new directory called ``new_class_programs`` in your ``Desktop``, and copy ``prog1.py`` and ``prog2.py`` into it. (Note that files will NOT disappear from your desktop when you've completed this step. There should be a copy of each file in both places.) 

    Use Unix commands to do this, and take a screenshot of the commands you use + evidence they worked. (Hint: using commands like ``cd`` and ``ls`` and ``pwd`` can help you check what you've done when you're creating directories and copying files around! It will also be useful to remind yourself of what ``mkdir`` and ``cp`` do.) 

    There is more than one perfectly reasonable way to complete this exercise, but all ways use a similar set of Unix commands.

.. external:: problem_set_5_unix_4
    
    4. Now, you want to create a new directory *inside* the ``new_class_programs`` directory, called ``text_files``, and copy both ``unix_test_text.txt`` and ``another_text.txt`` into *that* folder. Use Unix commands to do this. 

    When you've completed that, change directories to be inside that folder in your command prompt, and use the ``pwd`` command to show the full path of your location. (It should look *something like* this: ``/Users/Jackie/Desktop/new_class_programs/text_files``)

    Take a screenshot showing that these things worked for you. Your screenshot should show the command you typed + evidence it worked.

.. external:: problem_set_5_unix_5

    5. You want to see what content is inside each of your files. Use a unix command to view the content of ``prog2.py`` before you open it. Take a screenshot to show that this worked.

.. external:: problem_set_5_unix_6

    6. You want to concatenate the 2 text files inside the ``text_files`` folder together, and save the result in a file called ``big_story.txt``, which should also be inside that directory. Use unix commands to do this. (Hint: You'll probably need more than 1 typed in the same line.)

.. external:: problem_set_5_unix_7

    7. You now want to see a list of all the files and/or directories inside your ``new_class_programs`` folder whose names include ``text``. Use Unix commands to do this. (Hint: You'll need pipe (``|``) and ``grep``, and ``ls``.)

.. external:: problem_set_5_unix_8

    8. Now that you have a bunch of practice with the unix command prompt, it's time to run Python natively on your computer. You've saved 2 Python files that are in your ``~/Desktop/new_class_programs`` directory. Go there in your command prompt, and run ``prog2.py`` by typing ``python prog2.py`` at the prompt. Take a screenshot of what happens. 

    (Feel free to also play around -- you know a lot of programming now, and you can run it all on your computer, but it will look a little bit different in the command prompt than it did in the textbook.)

.. note::

    You may discover another way to run your python program directly from Sublime Text. We have found that this will not work for everything you need to do throughout the semester. Therefore, it's very important that you learn how to run your python programs from the unix command prompt, including figuring out how to connect to the right directory with the unix ``cd`` command. You will only get credit for these unix problems if your screenshots show that you ran the programs from the unix command prompt.


**This is very important for the rest of the semester. Starting with Problem Set 7, ALL of your problem set will be turned in via Canvas, and you will be writing code in a text editor and running it on your own computer. If you have any trouble running Python natively (on your computer), let an instructor know *right away*.**


You're done with the Unix part of the problem set. Again, `here <https://umich.instructure.com/courses/105657/assignments/139051>`_ is the Canvas assignment for submitting your screenshots. 


.. external:: ps5_dyu

   Complete the `Demonstrate Your Understanding <https://umich.instructure.com/courses/105657/assignments/131288>`_ assignment on Canvas.




