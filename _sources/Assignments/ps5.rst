:orphan:

..  Copyright (C) Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Activities through 10/19 (through Fall Break)
=============================================

* **Before class Monday 10/10:**

  * Read :ref:`Tuples <tuples_chap>` and try exercises in the sections listed below
  * Read :ref:`Nested Data and Nested Iteration<nested_chap>` and try exercises in sections listed below
  * Read just the :ref:`introduction to Unit Testing<test_cases_chap>`. (We will discuss this on Monday in lecture! You do *not* have to read the rest of this chapter beyond the introductory section; it addreses material we have not learned yet in this course. We will focus in more depth on that material later in the semester. But this week is the first time you will see the code for Unit Tests, so we will teach you how to understand the output you get from them when you run problem sets on your own computer.)

.. usageassignment::
  :subchapters: Testing/intro-TestCases, Tuples/Tuples, Tuples/TuplePacking, Tuples/TuplesasReturnValues, Tuples/TupleAssignmentwithunpacking, Tuples/UnpackingDictionaryItems, NestedData/ListswithComplexItems, NestedData/NestedDictionaries, NestedData/NestedIteration, NestedData/DebuggingNestedData
  :assignment_name: Prep 10
  :deadline: 2016-10-10 21:40
  :pct_required: 80
  :points: 50


* **Before Tuesday 10/11 at 11:59 PM:**

  * Complete :ref:`Reading Response 6<reading_response_6>`.

* **Before Wednesday's class, 10/12:**

  * Read :ref:`Sorting<sort_chap>` and try the exercises in the sections listed below.
  * Read about `Unix diff <http://www.computerhope.com/unix/udiff.htm>`_ and `Unix curl <https://en.wikipedia.org/wiki/CURL#Examples_of_cURL_use_from_command_line>`_ commands. 
  * NOTE: The latter link about ``curl`` is just one small section of a Wikipedia article that will help you understand what is happening when you use the Unix ``curl`` command. We will unpack this further later on!

.. usageassignment::
  :subchapters: Sort/intro-SortingwithSortandSorted, Sort/Optionalreverseparameter, Sort/Optionalkeyparameter, Sort/Anonymousfunctionswithlambdaexpressions, Sort/SortingaDictionary, Sort/StableSorting
  :assignment_name: Prep 11
  :deadline: 2016-10-12 21:40
  :pct_required: 80
  :points: 50

* **Before Sunday 10/16 at 11:59 PM:**

  * Complete all of :ref:`Problem Set 5 <problem_set_5>` and the Demonstrate Your Understanding assignment for this week.  

* **Note that your midterm is during class time on Wednesday, October 19, in Angell Hall.** See syllabus. We strongly suggest that you look through all Extra Exercises and do practice problems to prepare. Announcements will follow. 

.. note::

	Starting this week, your problem sets will be completed in ``.py`` files that you will download from Canvas and edit to add your answers. You will test them and work on them by running them via the command prompt, as you practiced last week. 

	Note that the test output will look different now -- you won't have the nice box with colors that you have in the textbook. However, you will still have the same information and more power to see what is being tested.

	**You will submit your final files in Canvas assignments.** However, the instructions for each problem on the assignment will be found in the textbook, as usual. You will need to reference the textbook for the instructions for each problem, and in the files we provide you, we will provide whatever code (if any) that we intend you to start with, beneath comments e.g. ``## [PROBLEM 1]``.

	Your problem set grades, once they are complete, will appear in the textbook progress page, just like your other problem sets.

	**Please make sure that you include the "ps#", e.g. ``ps5`` in your problem set file name when you submit it.** (Even better, don't change the file name at all!) That will make the instructional team's lives much easier.


This Week's Reading Responses
-----------------------------

.. _reading_response_6:

.. external:: rr_6

  `Reading Response 6 <https://umich.instructure.com/courses/108426/assignments/139267>`_ on Canvas.


.. _problem_set_5:

Problem Set
-----------

To find the file for your problem set, and to submit your assignment on Canvas, go `HERE <https://umich.instructure.com/courses/108426/assignments/183945>`_.

.. external:: ps_5_1

    1. Write code to sort the list ``fall_list`` in reverse alphabetical order. Assign the result of the sorted list to the variable ``sorted_fall_list``.

.. external:: ps_5_2

    2. First, write code to sort the list ``food_amounts`` by the key ``sugar_grams``, from lowest to highest. Assign that sorted list to the variable ``sorted_sugar``. 

    Next, write code to sort the list ``food_amounts`` by the value of the key ``carbohydrate`` minus the value of the key ``fiber`` in each one, from lowest difference to highest. Assign this sorted list to a variable ``raw_carb_sort``.

.. external:: ps_5_3

    3. Use the ``curl`` Unix command to download the file ``words.txt``, like so: ``curl http://www.puzzlers.org/pub/wordlists/ospd.txt > words.txt``. Make sure to do so in the same directory where you have saved this ``ps5.py`` file.

    There are 19 3-letter words in the Scrabble dictionary provided in the ``words.txt`` file which contain the letter 'z'. Write code to generate a list of them. That list should be sorted in *reverse* alphabetical order (i.e. ``'zoo'`` should be first and ``'adz'`` should be last). Save that list in a variable ``short_z_words``.

    **NOTE:** to get rid of the blank line character at the end of each line in the file, use the ``.strip()`` string method.

.. external:: ps_5_4

    4. Write code to generate a list of the 10 highest-scoring words from the Scrabble dictionary that contain the letter 'z'. Save it in the variable ``best_z_words``. You may assume there are no bonuses that double or triple letter values or entire words. The dictionary saved in ``letter_values`` contains the Scrabble score information: its keys are letters, and its values are the scores associated with those letters.

    If you have never played Scrabble before, `here is an explanation <https://en.wikipedia.org/wiki/Scrabble>`_ of what it is. (You do not need that information to solve this problem. All you need to know is that each letter is associated with a number of points, and you want to find the ten words that are associated with the largest point totals.)

    **HINT:** In the textbook section on Accumulating Results from a Dictionary, there is code that computes the scrabble score for the entire text of "A Study in Scarlet". You may want to adapt that.

.. external:: ps_5_5

		5. We have provided a nested list in the variable ``nl``. Write code to accumulate a list containing the second (as humans count) element of each sub-list and save it in a variable ``second_elems``.

.. external:: ps_5_6

		6. Define a function ``convert_nums``. The function should accept an integer as input, representing a number of hours. It should return a tuple of that number converted to minutes (* 60), and then that number converted to seconds (* 3600). For example, if ``1`` were input into the function, the return value of that invocation should be the tuple ``60, 3600``.

.. external:: ps_5_7

		7.  We've provided a complex nested dictionary saved in the variable ``fb_data``. This is a lot like real data you'll get from Facebook (but a little bit simpler, and fake data). 

		Here we've also provided some questions to help you. We will not grade, or expect you to write, answers to these questions, but we suggest you think about them and write them in comments to practice understanding this big nested data structure. Test your predictions using print statements in the code file! Questions:

		- What type is the structure saved in the variable ``fb_data``?
		- What about ``fb_data["data"][1]``?
		- What about ``fb_data["data"][0]["from"]``?
		- What about ``fb_data["data"][0]["id"]``?

		Now, write a line of code to assign the value of the first message ("This problem might...") from the big ``fb_data`` data structure to a variable called ``first_message``. (Do not hard-code your answer! That means, write it in terms of fb_data, so that it would work with any content stored in the variable ``fb_data`` that has the same structure as that of the one we gave you.)

		Then write a second line of code to assign the value of the name of the second person who posted ("John Smythe") to a variable called ``second_name``. Do not hard code your answer!

.. external:: ps_5_8

		6. Define a function ``sort_nested_lists`` that accepts as input a list of lists of integers, e.g. ``[[2,3],[45,100,2],[536],[103,2,8]]``. It should return a sorted version of that list, sorted by the sum of the integers in each sub-list. For example, if that list were the function's input, the return value should be ``[[2,3],[103,2,8],[45,100,2],[536]]``. 

		**Suggestion:** It's a good idea to come up with some sample "test cases" to help yourself work through this, in addition to the tests we have provided in your code file. Come up with sample lists where it's easy to figure out what the correct sorting is, and make invocations to your function using that input, and print out the results. If you get different output than you expect, trace through the process to figure out where it might have gone wrong. Writing out an English plan for this and translating it into code bit by bit may also be a good idea.



.. external:: ps5_dyu

    Complete this week's `Demonstrate Your Understanding <https://umich.instructure.com/courses/108426/assignments/139243>`_ assignment on Canvas.