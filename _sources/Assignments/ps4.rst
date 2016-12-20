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

Activities through 10/7
=======================

You have the following graded activities:

* **Before Monday's class, 10/3:**

  * Read :ref:`Accumulating results in dictionaries<dictionary_accum_chap>`, and try the following exercises in that chapter (You may want to refresh yourself on :ref:`Dictionaries<dictionaries_chap>`)

  * Read :ref:`Strategy for building programs <build_program_chap>`

  * :ref:`Lecture 8 Waiver <lecture_8_waiver>`

.. usageassignment::
    :subchapters: BuildingAProgram/TheStrategy, DictionaryAccumulation/intro-AccumulatingMultipleResultsInaDictionary, DictionaryAccumulation/AccumulatingResultsFromaDictionary, DictionaryAccumulation/AccumulatingaMaximumValue, DictionaryAccumulation/AccumulatingtheBestKey
    :assignment_name: Prep 08
    :deadline: 2016-10-03 19:40
    :pct_required: 80
    :points: 50

  
* **By Tuesday 10/4 11:59 pm:**

  * Read chapter 5 of The Most Human Human and answer `Reading Response 5 <https://umich.instructure.com/courses/105657/assignments/131316>`_ on Canvas.

* **Before Wednesday's class, 10/5:**

  * Read :ref:`Defining Functions<functions_chap>`, and try the following exercises in that chapter

  * :ref:`Lecture 9 Waiver<lecture_9_waiver>`
  
.. usageassignment::
    :subchapters: Functions/FunctionDefinitions,Functions/FunctionInvocation,Functions/FunctionParameters,Functions/Returningavaluefromafunction,Functions/Afunctionthataccumulates,Functions/DecodingaFunction,Functions/MethodInvocations,Functions/Variablesandparametersarelocal,Functions/GlobalVariables,Functions/Functionscancallotherfunctions,Functions/FlowofExecutionSummary,Functions/Printvs.return,Functions/PassingMutableObjects,Functions/SideEffects
    :assignment_name: Prep 09
    :deadline: 2016-10-05 19:40
    :pct_required: 80
    :points: 50


* **By Friday, 10/7 at 6:30 pm:**
  
  * Save answers to each of the exercises in :ref:`Problem Set 4 <problem_set_4>` and  submit your **Demonstrate Understanding** assignment to Canvas

  * Note that you have a grace period for the PSet and DYU until Sunday 10/9 at 5:00 PM

.. _reading_response_5:

This Week's Reading Responses
-----------------------------

.. external:: rr_5

  `Reading Response 5 <https://umich.instructure.com/courses/105657/assignments/131316>`_ on Canvas.  


.. _problem_set_4:

Problem Set
-----------

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

**Instructions:** Write the code you want to save in the provided boxes, and click **save** for each one. The last code you have saved for each one by the deadline is what will be graded.

**Note:** Remember, passing tests for a problem (``Pass``) does not ensure that the problem is 100% correct -- we can only test some things, to provide feedback as you go. Passing tests is necessary, but not always sufficient (enough to guarantee 100%).

.. activecode:: ps_4_01
       :language: python

       **1.** Old McDonald had a farm. He records the animals on his farm in a dictionary called ``animals``.
     
       Write code to look up the number of chickens that Old McDonald recorded and assign it to the variable ``num_chickens``.

       Write code to add the key-value pair ``"yak":3`` to the ``animals`` dictionary.

       Write code to increase the value for the key ``"dogs"`` in the ``animals`` dictionary by 1. Do not hard code values -- this code should work no matter what the original value associated with key ``"dogs"`` is. You can assume that this key already exists in the dictionary. 
       ~~~~
       animals = {'cows': 2, 'chickens': 8, 'pigs': 4, 'mice': 72, 'cats': 9,'dogs': 1}
       =====

       from unittest.gui import TestCaseGui

       class myTests(TestCaseGui):

           def testOne(self):
               self.assertEqual(num_chickens, animals['chickens'], "Testing that num_chickens has been assigned the value of the key 'chickens'")
           def testTwo(self):
               self.assertEqual(animals['yak'], 3, "Testing to see that 'yak' is a key in the dictionary animals with the correct value")
           def testThree(self):
               self.assertEqual(animals['dogs'], 2, "Testing that the value of 'dogs' is now 2 in the dictionary animals")

       myTests().main()


.. activecode:: ps_4_02
       :language: python

       **2.** Here's another dictionary, ``nd``. Write code to print out each key-value pair in it, one key and its value on each line. Your output should look somewhat like this (remember, the order may be different!):

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


.. activecode:: ps_4_03
       :language: python
       :available_files: about_programming.txt

       **3.** We've included the same file in this problem set that we included in the last problem set -- ``about_programming.txt``. Write code to open the file and print out each line in the file that has the string ``program`` in it. (Note that each line with the string ``program`` in it should only print out once, even if the string ``program`` occurs in it more than once.) Then, write code (or edit the code that you already wrote!) to accumulate a list of the lines in the file that include the string ``program``. Save that list in a variable ``program_lines``.
       ~~~~
       # Write your code here!
       =====

       from unittest.gui import TestCaseGui

       class myTests(TestCaseGui):

          def testOne(self):
             tmp = []
             for l in open("about_programming.txt").readlines():
                if "program" in l:
                   tmp.append(l)
             self.assertEqual(program_lines, tmp, "Testing that program_lines is a list of lines that contain the string 'program'")

          def testOneA(self):
              self.assertIn('open', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")
              self.assertIn('other technical professions in that programmers, in general, do not need to be licensed', self.getOutput(), "Testing output (Don't worry about actual and expected values).")

       myTests().main()

.. activecode:: ps_4_04
       :language: python

       **4.** Below is an empty dictionary saved in the variable ``nums``, and a list saved in the variable ``num_words``. Use iteration and dictionary mechanics to add each element of ``num_words`` as a key in the dictionary ``nums``. Each key should have the value ``0``. The dictionary should end up looking something like this when you print it out (remember, you can't be sure of the order): ``{"two":0,"three":0,"four":0,"eight":0,"seventeen":0,"not_a_number":0}``
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

.. activecode:: ps_4_05
       :language: python

       **5.** Given the string ``s`` in the code below, write code to figure out what the most common word in the string is and assign that to the variable ``abc``. (Do not hard-code the right answer.) Hint: dictionary mechanics will be useful here.
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

.. activecode:: ps_4_06
       :language: python

       **6.** Take a look at the code below. The function ``subtract_five`` is supposed to take one integer as input and return that integer minus 5. You'll get an error if you run it as is. Change the function so it works and passes the test!
       ~~~~
       def subtract_five(inp):
           print inp - 5
           return None

       y = subtract_five(9) - 6

       =====

       from unittest.gui import TestCaseGui

       class myTests(TestCaseGui):

          def testOne(self):
             self.assertEqual(y, -2, "Testing if y is -2")

       myTests().main()

.. activecode:: ps_4_07
       :language: python

       **7.** Define a function called ``change_amounts`` that takes one integer as input. If the input is larger than 10, it should return the input + 5. If the input is smaller than or equal to 10, it should return the input + 2.
       ~~~~ 
       # We've started you off with the first line...
       def change_amounts(num_here):
           pass # delete this line and put in your own code for the body of the function.

       =====

       from unittest.gui import TestCaseGui

       class myTests(TestCaseGui):

          def testOne(self):
             self.assertEqual(change_amounts(9), 11, "Testing if change_amounts(9) equals 11")
             self.assertEqual(change_amounts(12), 17, "Testing if change_amounts(12) equals 17")

       myTests().main()


.. activecode:: ps_4_08
       :language: python

       **8.** Here's another bit of code that generates an error. Think about what's going on with the code below that causes a problem. Why does it cause an error? Write a comment explaining why an error occurs. Then change line 5 to print out the result of an expression that invokes the function ``change_amounts`` and evaluates to ``7``. (So line 5 should be a print statement whose result is printing the integer ``7``.)
       ~~~~
       def change_amounts(yp):
           n = yp - 4
           return n * 7

       print yp

       ====

       from unittest.gui import TestCaseGui

       class myTests(TestCaseGui):

           def test_output(self):
               self.assertIn("7", self.getOutput(), "Testing output (Don't worry about actual and expected values).")

       myTests().main()

.. external:: ps4_dyu

       Complete this week's `Demonstrate Your Understanding <https://umich.instructure.com/courses/105657/assignments/131287>`_ on Canvas.