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


Activities through 11/4
=======================

* **Before Monday's class 10/31:**
    * Read :ref:`Sorting and anonymous functions<sort_chap>` and try the exercises in the sections listed below.
    * Read the chapter about the ``pip`` module and installation (almost the same for Windows and Mac, one small difference, which you'll see in the chapter). If you have trouble, check out :ref:`Native Interpreter Gotchas<gotchas_chap>`.
    * Read the single listed subsection about Unit Testing. (You will learn more about Unit Testing later in this course. For now, you just need to be familiar with the idea and the output, because this is your first week submitting a problem set that you run completely on your computer. We will discuss this further in lecture!)

* **Before Tuesday 11/1 11:59 PM:**
    * **Reading Response 8 deadline has been extended until Sunday Nov 6 at 11:59 PM, same as the problem set**

.. usageassignment::
  :subchapters: Sort/intro-SortingwithSortandSorted, Sort/Optionalreverseparameter, Sort/Optionalkeyparameter, Sort/Anonymousfunctionswithlambdaexpressions, Sort/SortingaDictionary, Sort/StableSorting, PythonModules/intro-ModulesandGettingHelp, PythonModules/Therandommodule, Installation/pip, Testing/intro-TestCases
  :assignment_name: Prep 14
  :deadline: 2016-10-31 21:40
  :pct_required: 80
  :points: 50

* **Before Wednesday's class 11/2:**
    * Read the below listed sections about REST APIs, unicode, and how the internet works, and try any exercises in those sections.
    * Read this brief snippet about `Unix curl <https://en.wikipedia.org/wiki/CURL#Examples_of_cURL_use_from_command_line>`_  commands. 


.. usageassignment::
  :subchapters: Requests/intro, Requests/fetching_a_page, Requests/how_the_Internet_works, Requests/urls, Requests/http, Requests/requests_details, RESTAPIs/intro, RESTAPIs/RequestURLs, RESTAPIs/DebugURLs, RESTAPIs/jsonlib, RESTAPIs/unicode, RESTAPIs/requestsCookbook
  :assignment_name: Prep 15
  :deadline: 2016-11-02 21:40
  :pct_required: 80
  :points: 50

* **By Friday 11/04 at 6:30 PM:**
   * Complete Problem Set 7: :ref:`Problem Set 7 <problem_set_7>` per the instructions below, and submit your ``106_ps7.py`` file on Canvas. (Grace period until Sunday 11/6 at 11:59 PM.)
   * Submit your **Demonstrate Your Understanding** assignment on Canvas (linked in problem set) 
   * **NOTE:** This problem set is the first one you will complete entirely on your computer and submit via Canvas. You need only submit your completed file. **Make sure that "ps7" is in the file name. Otherwise we can't grade it!** 

* **By Sunday 11/06 at 11:59 PM:**
  * Complete `RR 8 <https://umich.instructure.com/courses/105657/assignments/131319>`_ on Canvas.

.. note::

    **We do not give points for problem set code that does not run!** Just like in the textbook, we grade your code by running it, and we will not fix anything in the middle of your code to get it to run. You should check to be absolutely sure your problem set runs before submitting it.

.. note::

    Starting this week, your problem sets will be completed in ``.py`` files that you will download from Canvas and edit to add your answers. You will test them and work on them by running them via the command prompt, as you practiced last week and the week before. 

    Note that the test output will look different now -- you won't have the nice box with colors that you have in the textbook. However, you will still have the same information and more power to see what is being tested.

    **You will submit your final files in Canvas assignments.** However, the instructions for each problem on the assignment will be found in the textbook, as usual. You will need to reference the textbook for the instructions for each problem, and in the files we provide you, we will provide whatever code (if any) that we intend you to start with, beneath comments e.g. ``## [PROBLEM 1]``.

    Your problem set grades, once they are complete, will appear in the textbook progress page, just like your other problem sets.



This Week's Reading Responses
-----------------------------

.. _reading_response_8:

.. external:: rr_8

  `Reading Response 8 <https://umich.instructure.com/courses/105657/assignments/131319>`_ on Canvas.

.. _problem_set_7:

Problem Set
-----------

To find the file for your problem set, and to submit your assignment on Canvas, go `HERE <https://umich.instructure.com/courses/105657/assignments/131299>`_.

.. external:: ps_7_1

    1. Write code to sort the list ``fall_list`` in reverse alphabetical order. Assign the result of the sorted list to the variable ``sorted_fall_list``.

.. external:: ps_7_2

    2. First, write code to sort the list ``food_amounts`` by the key ``sugar_grams``, from lowest to highest. Assign that sorted list to the variable ``sorted_sugar``. 

    Next, write code to sort the list ``food_amounts`` by the value of the key ``carbohydrate`` minus the value of the key ``fiber`` in each one, from lowest difference to highest. Assign this sorted list to a variable ``raw_carb_sort``.

.. external:: ps_7_3

    3. Use the ``curl`` Unix command to download the file ``words.txt``, like so: ``curl http://www.puzzlers.org/pub/wordlists/ospd.txt > words.txt``. Make sure to do so in the same directory where you have saved this ``ps5.py`` file.

    There are 19 3-letter words in the Scrabble dictionary provided in the ``words.txt`` file which contain the letter 'z'. Write code to generate a list of them. That list should be sorted in *reverse* alphabetical order (i.e. ``'zoo'`` should be first and ``'adz'`` should be last). Save that list in a variable ``short_z_words``.

    **NOTE:** to get rid of the blank line character at the end of each line in the file, use the ``.strip()`` string method.

.. external:: ps_7_4

    4. Write code to generate a list of the 10 highest-scoring words from the Scrabble dictionary that contain the letter 'z'. Save it in the variable ``best_z_words``. You may assume there are no bonuses that double or triple letter values or entire words. The dictionary saved in ``letter_values`` contains the Scrabble score information: its keys are letters, and its values are the scores associated with those letters.

    If you have never played Scrabble before, `here is an explanation <https://en.wikipedia.org/wiki/Scrabble>`_ of what it is. (You do not need that information to solve this problem. All you need to know is that each letter is associated with a number of points, and you want to find the ten words that are associated with the largest point totals.)

    **HINT:** In the textbook section on Accumulating Results from a Dictionary, there is code that computes the scrabble score for the entire text of "A Study in Scarlet". You may want to adapt that.

.. external:: ps_7_5

    5. We have provided a nested list in the variable ``nl``. Write code to accumulate a list containing the second (as humans count) element of each sub-list and save it in a variable ``second_elems``.

.. external:: ps_7_6

    6. Define a function ``convert_nums``. The function should accept an integer as input, representing a number of hours. It should return a tuple of that number converted to minutes (* 60), and then that number converted to seconds (* 3600). For example, if ``1`` were input into the function, the return value of that invocation should be the tuple ``60, 3600``.

.. external:: ps_7_7

    7. Define a function ``sort_nested_lists`` that accepts as input a list of lists of integers, e.g. ``[[2,3],[45,100,2],[536],[103,2,8]]``. It should return a sorted version of that list, sorted by the sum of the integers in each sub-list. For example, if that list were the function's input, the return value should be ``[[2,3],[103,2,8],[45,100,2],[536]]``. 

    **Suggestion:** It's a good idea to come up with some sample "test cases" to help yourself work through this, in addition to the tests we have provided in your code file. Come up with sample lists where it's easy to figure out what the correct sorting is, and make invocations to your function using that input, and print out the results. If you get different output than you expect, trace through the process to figure out where it might have gone wrong. Writing out an English plan for this and translating it into code bit by bit may also be a good idea.


.. external:: ps7_dyu

    Complete this week's `Demonstrate Your Understanding <https://umich.instructure.com/courses/105657/assignments/131290>`_ assignment on Canvas.
