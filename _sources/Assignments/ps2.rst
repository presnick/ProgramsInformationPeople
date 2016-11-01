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

Activities through 9/23
=======================

You have the following graded activities:

* **By Sunday 9/18 at 11:59 pm:** 
    
  * Read chapter 2 of The Most Human Human and answer `RR 3 <https://umich.instructure.com/courses/108426/assignments/139264>`_ .

* **Before class Monday 9/19:**

  * Read :ref:`Conditionals <conditionals_chap>`
  * Read :ref:`File Input/Output <files_chap>`
  * Read :ref:`Dictionaries<dictionaries_chap>`
  * Read about :ref:`Understanding Code <understand_code_chap>`
  * Try the exercises included within each chapter section below for lecture prep. (The exercises listed under **Exercises** and **Extra Exercises** are optional practice!)

.. usageassignment::
    :subchapters: Selection/ConditionalExecutionBinarySelection, Selection/OmittingtheelseClauseUnarySelection, Selection/Nestedconditionals, Selection/Chainedconditionals, Files/intro-WorkingwithDataFiles, Files/FindingaFileonyourDisk, Files/ReadingaFile, Files/AlternativeFileReadingMethods, Files/Iteratingoverlinesinafile, Files/FilesRecipe, Files/WritingTextFiles, Dictionaries/intro-Dictionaries, Dictionaries/Dictionaryoperations, Dictionaries/Dictionarymethods, Dictionaries/Aliasingandcopying, BuildingAProgram/UnderstandingCode
    :assignment_name: Prep 04
    :deadline: 2016-09-30 04:00
    :pct_required: 80
    :points: 50


* **Before Wednesday's class 9/21:**

  * Read :ref:`Accumulating results in dictionaries<dictionary_accum_chap>`, and try the exercises in that chapter (You may want to refresh yourself on :ref:`Dictionaries<dictionaries_chap>`)
  * Read another part of :ref:`Building A Program<build_program_chap>`

.. usageassignment::
    :subchapters: BuildingAProgram/TheStrategy, DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary, DictionaryAccumulation/AccumulatingResultsFromaDictionary, DictionaryAccumulation/AccumulatingaMaximumValue, DictionaryAccumulation/AccumulatingtheBestKey
    :assignment_name: Prep 05
    :deadline: 2016-09-30 04:00
    :pct_required: 70
    :points: 50

* By **Friday 9/23 at 6:30PM**, save answers to the exercises in **Problem Set 2**:

  * Complete each of the problem set problems.
  * Submit your Demonstrate Your Understanding assignment (linked in the problem set).
  * Note that you have a grace period for the problem set and DYU submissions until Sunday 9/25 at 11:59 PM. 

This Week's Reading Responses
-----------------------------

.. _reading_response_3:

.. external:: rr_3
    
    `Reading Response 3 <https://umich.instructure.com/courses/105657/assignments/131314>`_ on Canvas.

.. _problem_set_2:

Problem Set
-----------

**Instructions:** Write the code you want to save in the provided boxes, and click **save & run** for each one. The last code you have saved for each one by the deadline is what will be graded.


Problem Set
-----------

**Instructions:** Write the code you want to save in the provided boxes, and click **run** for each one, which will save what is in the code window. The last code you have saved for each one by the deadline is what will be graded.

.. datafile::  about_programming.txt
   :hide:

   Computer programming (often shortened to programming) is a process that leads from an
   original formulation of a computing problem to executable programs. It involves
   activities such as analysis, understanding, and generically solving such problems
   resulting in an algorithm, verification of requirements of the algorithm including its
   correctness and its resource consumption, implementation (or coding) of the algorithm in
   a target programming language, testing, debugging, and maintaining the source code,
   implementation of the build system and management of derived artefacts such as machine
   code of computer programs. The algorithm is often only represented in human-parseable
   form and reasoned about using logic. Source code is written in one or more programming
   languages (such as C++, C#, Java, Python, Smalltalk, JavaScript, etc.). The purpose of
   programming is to find a sequence of instructions that will automate performing a
   specific task or solve a given problem. The process of programming thus often requires
   expertise in many different subjects, including knowledge of the application domain,
   specialized algorithms and formal logic.
   Within software engineering, programming (the implementation) is regarded as one phase in a software development process. There is an on-going debate on the extent to which
   the writing of programs is an art form, a craft, or an engineering discipline. In
   general, good programming is considered to be the measured application of all three,
   with the goal of producing an efficient and evolvable software solution (the criteria
   for "efficient" and "evolvable" vary considerably). The discipline differs from many
   other technical professions in that programmers, in general, do not need to be licensed
   or pass any standardized (or governmentally regulated) certification tests in order to
   call themselves "programmers" or even "software engineers." Because the discipline
   covers many areas, which may or may not include critical applications, it is debatable
   whether licensing is required for the profession as a whole. In most cases, the
   discipline is self-governed by the entities which require the programming, and sometimes
   very strict environments are defined (e.g. United States Air Force use of AdaCore and
   security clearance). However, representing oneself as a "professional software engineer"
   without a license from an accredited institution is illegal in many parts of the world.

.. activecode:: ps_2_1
   :language: python
   :available_files: about_programming.txt
   :autograde: unittest
   :hidecode:

   **1.** Write code to open the file ``about_programming.txt`` which has been provided for you in this problem set, and assign the **number of lines** in the file to the variable ``file_lines_num``.
   ~~~~
   # Write your code here.

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

    def testOne(self):
       self.assertIn('open', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")
       self.assertEqual(file_lines_num,len(open("about_programming.txt","r").readlines()), "Testing to see that file_lines_num has been set to the number of lines in the file.")

   myTests().main()

.. activecode:: ps_2_2
   :language: python
   :autograde: unittest
   :hidecode:

   **2.** The program below doesn't always work as intended. Try uncommenting different lines setting the initial value of x. Tests will run at the end of your code, and you will get diagnostic error messages. 

   Fix the code so that it passes the test for each different value of x. So when the first line is uncommented, and when the second line, third line, and fourth line are each uncommented, you should always pass the test.

   (HINT: you don't have to make a big change.)
   ~~~~ 
   #x = 25
   #x = 15
   #x = 5
   #x = -10

   if x > 20:
     y = "yes"
   if x > 10:
     y = "no"
   if x < 0:
     y = "maybe"
   else:
     y = "unknown"

   print "y is " + str(y)

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

     def testOne(self):
         print("No tests for the comment, of course -- we can only test stored values!\n")
         if x == 25:
             self.assertEqual(y, "yes", "test when x is 25: y should be 'yes'")
         elif x == 15:
             self.assertEqual(y, 'no', "test when x is 15: y should be 'no'")
         elif x == 5:
             self.assertEqual(y, 'unknown', "test when x is 5: y should be 'unknown'")
         elif x == -10:
             self.assertEqual(y, 'maybe', "test when x is -10: y should be 'maybe'")
         else:
             print "No tests when value of x is %s" % (x)

   myTests().main()

.. activecode:: ps_2_3
   :language: python
   :autograde: unittest
   :hidecode:


   **3.** How many characters are in each element of list ``lp``? Write code to print the length (number of characters) of each element of the list, on a separate line. (Do not write 8+ lines of code to do this. Use a for loop.)

   The output you get should be:

   :: 

     5
     13
     11
     12
     3
     12
     11
     6 

   Then, write code to print out each element of list ``lp`` *only if* the length of the element is an even number. Use iteration (a for loop).
   ~~~~
   lp = ["hello","arachnophobia","lamplighter","inspirations","ice","amalgamation","programming","Python"]
   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

     def test_output(self):
         self.assertIn('for', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")
     def test_outputA(self):
         self.assertIn("5\n13\n11\n12\n3\n12\n11\n6", self.getOutput(), "Testing output (Don't worry about actual and expected values).")
     def test_outputB(self):
         self.assertIn("inspirations\namalgamation\nPython", self.getOutput(), "Testing output (Don't worry about actual and expected values).")

   myTests().main()

.. activecode:: ps_2_4
   :language: python
   :autograde: unittest
   :hidecode:

   **4.** Write code to count the number of strings in list ``items`` that have the character ``w`` in it. Assign that number to the variable ``acc_num``. 

   HINT 1: Use the accumulation pattern! 

   HINT 2: the ``in`` operator checks whether a substring is present in a string.
   ~~~~
   items = ["whirring", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

     def testOne(self):
         self.assertIn(' in ', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")
         self.assertEqual(acc_num, 3, "Testing that acc_num has been set to the number of strings that have 'w' in them.")

   myTests().main()

.. activecode:: ps_2_5
   :language: python
   :autograde: unittest
   :hidecode:

   **5.** Below is a dictionary ``diction`` with two key-value pairs inside it. The string ``"python"`` is one of its keys. Using dictionary mechanics, print out the value of the key ``"python"``.
   ~~~~
   diction = {"python":"you are awesome","autumn":100}

   # Write your code here.

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

     def testOne(self):
         self.assertIn('you are awesome', self.getOutput(), "Testing your code (Don't worry about actual and expected values).")

   myTests().main()

.. activecode:: ps_2_6
   :language: python
   :autograde: unittest
   :hidecode:

   **6.** Here's another dictionary, ``nd``. Write code to print out each key-value pair in it, one key and its value on each line. Your output should look somewhat like this (remember, the order may be different!):

   ::

     autumn spring
     4 seasons
     23 345
     well spring

   **Hint:** Printing things with a comma, e.g. ``print "hello", "everyone"`` will print out those things on the same line with  a space in between them: ``hello everyone``.

   Then, write code to increase the value of key ``"23"`` by 5. Your code should work no matter what the value of the key ``"23"`` is, as long as its value is an integer.

   Finally, write code to print the value of the key ``"well"``. Your code should work no matter what the value of the key "well" is.
   ~~~~
   nd = {"autumn":"spring", "well":"spring", "4":"seasons","23":345}
   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

    def testOne(self):
       self.assertEqual(nd["23"], 350, "Testing that the value associated with the key '23' is 350")
       self.assertIn("autumn spring", self.getOutput(), "Testing output (Don't worry about actual and expected values).") 
       self.assertIn("well spring", self.getOutput(), "Testing output (Don't worry about actual and expected values).")
       self.assertIn("4 seasons", self.getOutput(), "Testing output (Don't worry about actual and expected values).")
       self.assertIn("23 345", self.getOutput(), "Testing output (Don't worry about actual and expected values).")

   myTests().main()

.. activecode:: ps_2_7
   :language: python
   :autograde: unittest
   :hidecode:

   **7.** Below is an empty dictionary saved in the variable ``nums``, and a list saved in the variable ``num_words``. Use iteration and dictionary mechanics to add each element of ``num_words`` as a key in the dictionary ``nums``. Each key should have the value ``0``. The dictionary should end up looking something like this when you print it out (remember, you can't be sure of the order): ``{"two":0,"three":0,"four":0,"eight":0,"seventeen":0,"not_a_number":0}``
   ~~~~
   nums = {}
   num_words = ["two","three","four","seventeen","eight","not_a_number"]
   # Write your code here.

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

    def testOne(self):
       self.assertEqual(nums["two"], 0, "Testing that the key 'two' has been assigned the value of 0.")
       self.assertEqual(type(nums["seventeen"]), type(3), "Testing that the key 'seventeen' has been assigned a value whose type is an integer.")
       self.assertEqual(sorted(nums), sorted({"two": 0, "three": 0, "four": 0, "eight": 0, "seventeen": 0, "not_a_number": 0}), "Testing that the contents of nums is accurate.")

    def testOneA(self):
       self.assertIn('for', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")

   myTests().main()

.. activecode:: ps_2_8
   :language: python
   :autograde: unittest
   :hidecode:


   **8.** Given the string ``s`` in the code below, write code to figure out what the most common word in the string is and assign that to the variable ``abc``. (Do not hard-code the right answer.) Hint: dictionary mechanics will be useful here.
   ~~~~
   s = "Number of slams in an old screen door depends upon how loud you shut it, the count of slices in a bread depends how thin you cut it, and amount 'o good inside a day depends on how well you live 'em. All depends, all depends, all depends on what's around ya."

   # Write your code here.

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

    def testOne(self):
       self.assertEqual(abc, 'depends', "testing whether abc is set correctly")

    def testOneA(self):
       self.assertIn('for', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")

   myTests().main()




.. external:: ps2_dyu

    Submit your `Demonstrate Your Understanding <https://umich.instructure.com/courses/108426/assignments/139240>`_ for this week on Canvas.