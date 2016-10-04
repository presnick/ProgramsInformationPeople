:orphan:

..  Copyright (C) Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

* **Before class Monday 10/10:**

  * Read something

.. usageassignment::
	:subchapters: Unix/CommandPrompt, Unix/FoldersAndPaths, Unix/DirectoriesAndCopying, Unix/lessCommand
  :assignment_name: Prep 10
  :deadline: 2016-10-10 21:40
  :pct_required: 80
  :points: 50

* **Before Tuesday 10/11 at 11:59 PM:**

  * Complete :ref:`Reading Response 5<reading_response_5>`.

* **Before Wednesday's class, 10/12:**

  * Read something
  * Read just one section of the Unit Testing chapter: LINK. **We will *not* expect you to know this material yet.** You should just be aware that you will see this material in your provided problem set files, you should not change it, and you'll have a basic idea of what it is doing.

.. usageassignment::
	:subchapters: Unix/CommandPrompt, Unix/FoldersAndPaths, Unix/DirectoriesAndCopying, Unix/lessCommand
  :assignment_name: Prep 11
  :deadline: 2016-10-12 21:40
  :pct_required: 80
  :points: 50

* **Before Sunday 10/16 at 11:59 PM:**

  * Complete all of :ref:`Problem Set 5<problem_set_5>`and the Demonstrate Your Understanding assignment for this week.  

.. note::

	Starting this week, your problem sets will be completed in ``.py`` files that you will download from Canvas and edit to add your answers. You will test them and work on them by running them via the command prompt, as you practiced last week. 

	You will submit your final files in Canvas assignments. However, the instructions for each problem on the assignment will be found in the textbook, as usual. You will need to reference the textbook for the instructions for each problem, and in the files we provide you, we will provide whatever code (if any) that we intend you to start with, beneath comments e.g. ``## [PROBLEM 1]``.

	**Please make sure that you include the "ps#", e.g. ``ps5`` in your problem set file name when you submit it.** (Even better, don't change the file name at all!) That will make the instructional team's lives much easier.


This Week's Reading Responses
-----------------------------

.. _reading_response_6:

.. external:: rr_6

  `Reading Response 6 <linkhere.link>`_ on Canvas.


.. _problem_set_5:

Problem Set
-----------

To find the file, and submit your final assignment on Canvas, go `HERE <linkhere.linkhere>`_.

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

    If you have never played Scrabble before, `here <linkhere.link>`_ is an explanation of what it is. (You do not need that information to solve this problem. All you need to know is that each letter is associated with a number of points, and you want to find the ten words that are associated with the largest point totals.)

    **HINT:** In the textbook section on Accumulating Results from a Dictionary, there is code that computes the scrabble score for the entire text of "A Study in Scarlet". You may want to adapt that.

.. external:: ps_5_5

    5. Define a function called ``grep_in_python``: it should take as input: a string whose default value is the empty string, and a list of strings. It should return a list of only the strings in the list input which include the string input. 

.. external:: ps_5_6

		6. Define a function ``sort_nested_lists`` that accepts as input a list of lists of integers, e.g. ``[[2,3],[45,100,2],[536],[103,2,8]]``. It should return a sorted version of that list, sorted by the sum of the integers in each sub-list. For example, if that list were the function's input, the return value should be ``[[536],[45,100,2],[103,2,8][2,3]]``. 

		**Suggestion:** It's a good idea to come up with some sample "test cases" to help yourself work through this, in addition to the tests we have provided in your code file. Come up with sample lists where it's easy to figure out what the correct sorting is, and make invocations to your function using that input, and print out the results. If you get different output than you expect, trace through the process to figure out where it might have gone wrong. Writing out an English plan for this and translating it into code bit by bit may also be a good idea.

.. external:: ps5_dyu

    Complete this week's `Demonstrate Your Understanding <linkhere.link>`_ assignment on Canvas.