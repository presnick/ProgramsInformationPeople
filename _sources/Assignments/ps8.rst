:orphan:

..  Copyright (C) Paul Resnick, Jackie Cohen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Activities through 11/11
========================

* **Before class Monday 11/7:**

  * Read :ref:`Advanced Accumulation <list_comp_chap>` and try any activities in the listed sub-chapters

.. usageassignment::
  :subchapters: AdvancedAccumulation/intro, AdvancedAccumulation/map, AdvancedAccumulation/filter, AdvancedAccumulation/listcomp, AdvancedAccumulation/reduce, AdvancedAccumulation/zip
  :assignment_name: Prep 16
  :deadline: 2016-11-07 22:40
  :pct_required: 80
  :points: 50

* **Before class Wednesday 11/9:**

  * Read :ref:`Testing <test_cases_chap>` and try any activities in the listed sub-chapters
  * We strongly suggest you also try writing some of these Unit Test examples in your own code files!

.. usageassignment::
  :subchapters: Testing/intro-TestCases, Testing/Testingfunctions, Testing/Testingclasses
  :assignment_name: Prep 17
  :deadline: 2016-11-09 22:40
  :pct_required: 80
  :points: 50

* **Before Sunday 11/13 at 11:59 PM:**

  * Complete and submit your :ref:`Problem Set 8 <problem_set_8>`, and save an answer to your Demonstrate Understanding for this week (linked below).
  * Complete :ref:`Reading Response 9 <reading_response_9>`.

This Week's Reading Responses
-----------------------------

.. _reading_response_9:

.. external:: rr_9

  `Reading Response 9 <https://umich.instructure.com/courses/108426/assignments/139270>`_ on Canvas.


.. _problem_set_8:

Problem Set
-----------

Go `HERE to see the Problem Set 8 assignment <https://umich.instructure.com/courses/108426/assignments/139256>`_, where you can find the file you need to download and edit, and where you can submit your file for this assignment.

.. note::

	Note that each problem on this problem set has two parts: solving the problem, and writing Unit Tests for that problem that check that you have solved it per the instructions! 
	
	It may be easier to write the Unit Tests for each problem first, and then solve the problems themselves (this is known as test-driven development).

	You should include, as the third argument to each of your tests, a brief, clear English description of what the test is checking for! e.g. "Testing whether the first element of the list student_tups is type tuple".

.. note::

	Reminder: we do not debug code when grading, so we cannot grade code that does not run! Make sure your code runs before submitting it -- you should comment out any code that does not.


.. external:: ps_8_01
	
	**PROBLEM 1**

	We've provided a definition of a class Student, similar to one you may have seen in lecture. Do not change that code:

	.. sourcecode:: python

		class Student():
		    def __init__(this_Student, name, years_at_umich=1):
		        this_Student.name = name
		        this_Student.years_UM = years_at_umich
		        this_Student.bonus_points = random.randrange(1000)

		    def shout(this_Student, phrase_to_shout):
		        print phrase_to_shout  # print is for ppl!

		    def __str__(this_Student):
		        return "My name is {}, and I've been at UMich for about {} years.".format(this_Student.name,this_Student.years_UM)

		    def year_at_umich(this_Student):
		        return this_Student.years_UM

	You should define a subclass of ``Student``, ``Programming_Student``.

	* The ``Programming_Student`` class should have an instance variable called ``number_programs_written`` whose value gets passed into the Programming_Student constructor after the ``years_at_umich``. The default value for the ``number_programs_written`` instance variable should be 0.

	* The ``Programming_Student`` class should also have a method called ``write_programs``. The ``write_programs`` method accepts an optional parameter called ``progs``, which should be an integer representing the number of programs the Programming_Student will write. Its default value is ``1``. When the write_programs method is called on an instance of Programming_Student, the ``progs`` number should be added to the instance's ``number_programs_written``.

	* The ``Programming_Student`` class should also have a method called ``productivity``. The productivity method should return the average number of programs that the Programming_Student has written per year (that is, divide its ``number_programs_written`` by its ``years_UM``  -- using float division, not integer divison, so you can get a decimal in your answer).

	* When the ``shout`` method is called for the ``Programming_Student`` class, the phrase ``"Also, Python is pretty cool."`` should print after the phrase to shout. You should be calling the parent ``shout`` method to make this happen.

	* The printed representation of an instance of ``Programming_Student`` should look something like ``"My name is Julie, I've been at UMich for about 100 years, and I have written 90 programs while here."``, where **Julie**, **100**, and **90** are in the place of the instance variable values for each instance you create. Override the Student ``__str__`` method for the Programming_Student class to make that happen.

.. external:: ps_8_01_test

	Write unit tests in your file below your ``Programming_Student`` class definition that ensure that your code does what the instructions say. You should write at least 3 unit tests. 

	Hint: You'll need to create an instance of your Programming_Student class in order to test your code: see the **Testing Classes** section of the textbook!

	(You can include each test in the same subclass of ``unittest.TestCase``, or you can create multiple subclasses of ``unittest.TestCase``. However, each unique ``assert`` statement should be in its own method. See the bottom of the files of your ``506_ps7.py`` and ``506_ps6.py``, as well as the textbook chapters, for examples!) 

	Note that the ``unittest.main(verbosity=2)`` line of code provided at the end of your problem set file is what actually *runs* the tests you write.

.. external:: ps_8_02

	**PROBLEM 2**

	We've provided three lists for you in your code file, like so:

	.. sourcecode:: python

		# Provided code
		names = ["Albert", "Bisi", "Cai", "Dinesh", "Euijin"]
		seniority = [1, 5, 2, 4, 1]
		programs_written = [10, 500, 20, 131, 46]

	The following problems, through Problem 7, build on one another, so make sure you understand what is happening step by step.

	First, create a list of tuples, in which the first tuple in the list is the first value from each list: ``names``, ``seniority``, and ``programs_written``: ``("Albert", 1, 10)``, and the second tuple in the list is each of the second elements of these lists ``("Bisi", 5, 500)``, and so on. 

	Save that list in a variable called ``student_tups``. Do not hard-code it -- so, don't just type it out! 

	(**Hint to make this easier:** check out ``https://www.programsinformationpeople.org/runestone/static/506F16/AdvancedAccumulation/zip.html``)

.. external:: ps_8_02_test

	Write a unit test to check whether the list of tuples ``student_tups`` holds the correct value.

.. external:: ps_8_03

	**PROBLEM 3**

	Use a list comprehension with the ``student_tups`` list that you just created in order to create a list of ``Programming_Student`` instances. Save the list of ``Programming_Student`` instances in a variable called ``programmers``.

.. external:: ps_8_03_test

	Write at least 3 unit tests that check whether the ``programmers`` list is correct. Does it have the elements it is supposed to have? 

	Hints to help you decide: Is the first element of the list the correct type? Does it have the attributes it should have? Is the ``programmers`` list the correct length?

.. external:: ps_8_04

	**PROBLEM 4**

	Use the Python ``map`` function on the ``programmers`` list you just created, in order to create a list of numbers representing the **productivity** of each student. 

	Save the new list in a variable called ``productivities``. (The first couple of values should be the equivalent of ``10.0/1`` and ``500.0/5``...) 

	Be sure to make use of the ``productivity`` method that you defined for the ``Programming_Student`` class.

.. external:: ps_8_04_test

	Write a unit test to check whether the list of tuples ``productivities`` holds the correct value.

.. external:: ps_8_05

	**PROBLEM 5**

	Use a list comprehension on the list ``programmers`` that you created above, in order to create a list of tuples wherein each tuple has a student's name as the first element and the student's productivity value as the second element. 

	Save the list of tuples in a variable called ``names_and_productivities``. The first tuple should be ``("Albert", 10.0)`` and the second should be ``("Bisi", 100.0)``, and so on.

.. external:: ps_8_05_test

	Write a unit test that checks whether ``names_and_productivities`` holds the correct value.

.. external:: ps_8_06

	**PROBLEM 6**

	Use the Python ``filter`` function to select the subset of ``programmers`` instances who have names with 5 or more characters. Save the resulting list in a variable called ``long_names``.

.. external:: ps_8_06_test

	Write a unit test that checks whether ``long_names`` holds the correct value. (Hint: It should hold a list of ``Programming_Student`` instances... but it should not include every element of the ``programmers`` list!)

.. external:: ps_8_07

	**PROBLEM 7**

	Use a list comprehension to generate a list of strings: **just the names**  of the ``Programming_Student`` instances where the lengths of their names are longer than the number of years they've been at UM (i.e., ``["Albert", "Cai", "Dinesh", "Eujin"]``). Assign the result list to a variable called ``names_with_not_too_much_seniority``.

.. external:: ps_8_07_test

	Write a unit test that checks whether ``names_with_not_too_much_seniority`` holds the correct value.

.. external:: ps_8_08_test

	**PROBLEM 8**

	We have provided a function definition for you, called ``good_cards``. 

	It takes as input a list of integers. Each integer has a value between 1 and 10 (inclusive: each value could be 1, and it could be 10). You can think of the integers in the input list as representing cards with values 1-10.

	The function simulates a blackjack game (a type of poker game): the function is supposed to return an integer which represents a *count* of how many values ('cards') from the input list ``L`` can be accepted before the sum of the accepted values becomes greater than 21. 

	(In blackjack, if the sum of cards is over 21, the player is "busted" and loses that game. For those familiar with special Blackjack game rules, in this function, the integer value ``1`` should always count as just ``1``, not as ``11``. For those who do not know the game, you need only pay attention to the description of what this function ought to do to write good tests for it!) 

	If the list of all the values in the input list ``L`` do not add up to 21, the ``good_cards`` function should return the total length of the input list ``L``. Otherwise, the function should return the number of values in input list ``L`` it took to reach a sum of 21. The code we've written for the function is as shown here, also provided in your problem set Python file:

	.. sourcecode:: python

		def good_cards(L):
		    sum = 0
		    c = 0
		    to_return = []
		    for card in L:
		        sum += card
		        c += 1
		        if sum >= 21:
		            break
		    return c

.. mchoice:: ps_8_08_mc
   :answer_a: Return value tests
   :answer_b: Side effect tests
   :answer_c: Both
   :feedback_a: Yes! This function returns a value, so you'll want to check whether it returns the correct output given a variety of different inputs.
   :feedback_b: This function does not have an effect on anything outside its local scope, so you will not need to write any side-effect tests.
   :feedback_c: In this case, there's no need for side-effect tests. Usually this answer is true when you write tests for a class definition, but somewhat rarely for a function outside a class definition.
   :correct: a

   **Ungraded, but helpful for Problem 8:** To write unit tests for this function ``good_cards``, should you create return-value tests, side-effect tests, or both? 

.. external:: ps_8_08

    Finally, in your code file, write unit tests for the good_cards function. Make sure you consider edge cases. What if ``L`` does not have enough values in the list to get to 21, will the function work correctly? What if the sum of the values in ``L`` is exactly 21? What if it takes a lot of "cards" to get to 21? What if it takes very few values from the input list ``L`` to add up to 21? etc. 

    (You may assume that all values in the function's input list ``L`` will be in the range of 1 - 10 and will be integers; you do not need to test for that. Here, you should not write tests that deal with bad input to the ``good_cards`` function, only tests that check whether the function will work properly, per the description above, for a variety of different inputs.)

.. external:: ps8_dyu

    Complete this week's `Demonstrate Your Understanding <https://umich.instructure.com/courses/108426/assignments/139246>`_ assignment on Canvas.