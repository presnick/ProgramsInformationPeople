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

  * Read chapter 2 of The Most Human Human and answer `Reading Response 3 <https://umich.instructure.com/courses/105657/assignments/131314>`_ .

* **Before class Monday 9/19:**

  * Read :ref:`Sequences <sequences_chap>`, and try exercises in that chapter. (You should try all the exercises **in the Sequences** sections that are listed below**. There are also additional exercises for practice! You may try these any time and we may discuss them in lecture. They may help you understand the material better! You do *not* need to do them for Lecture Prep.)

  * **To get credit for lecture attendance for Monday's lecture** (thus making attendance at Monday's lecture optional), complete the :ref:`Lecture 4 Waiver <lecture_4_waiver>` *before* Monday's lecture and pass all of the tests. (We encourage you to try these, regardless!)

.. usageassignment:: 
  :subchapters: Sequences/intro-Sequences, Sequences/OperationsonStrings, Sequences/IndexOperatorWorkingwiththeCharactersofaString, Sequences/OperationsandStrings, Sequences/StringMethods, Sequences/Length, Sequences/TheSliceOperator, Sequences/StringsareImmutable, Sequences/Theinandnotinoperators, Sequences/Characterclassification, Sequences/Lists, Sequences/ListValues, Sequences/ListLength, Sequences/AccessingElements, Sequences/ListMembership, Sequences/ConcatenationandRepetition, Sequences/ListSlices, Sequences/ListsareMutable, Sequences/ListDeletion, Sequences/ObjectsandReferences, Sequences/Aliasing, Sequences/CloningLists, Sequences/ListMethods, Sequences/AppendversusConcatenate, Sequences/SplitandJoin
  :assignment_name: Prep 04
  :deadline: 2016-09-30 04:00
  :pct_required: 80
  :points: 50


* **Before Wednesday's class 9/21:**

  * :ref:`Lecture 5 Waiver<lecture_5_waiver>`

  * Read :ref:`Iteration<iteration_chap>`, and try the exercises in that chapter. 

.. usageassignment:: 
  :subchapters: Iteration/intro-Iteration, Iteration/TheforLoop, Iteration/FlowofExecutionoftheforLoop, Iteration/Stringsandforloops, Iteration/TraversalandtheforLoopByIndex, Iteration/Listsandforloops, Iteration/TheAccumulatorPattern, Iteration/TheAccumulatorPatternwithLists, Iteration/TheAccumulatorPatternwithStrings
  :assignment_name: Prep 05
  :deadline: 2016-09-30 04:00
  :pct_required: 80
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

.. activecode:: ps_2_1
    :language: python
    :autograde: unittest
    :hidecode:
  
    **1.** Assign the variable ``fl`` the value of the first element of the string value in ``original_str``. Use string indexing to assign the variable ``last_l`` the value of the last element of the string value in ``original_str``. Write code so that will work no matter how long ``original_str``'s value is.
    ~~~~
    original_str = "The quick brown rhino jumped over the extremely lazy fox."
     
    # assign variables as specified below this line!
     
    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
           self.assertEqual(fl, original_str[0], "Testing that fl has been set to first char in original_str")
           self.assertEqual(last_l, original_str[-1], "Testing that last_l has been set to last char in original_str")
           self.assertIn('-1', self.getEditorText(), "Testing that you indexed correctly. (Don't worry about Actual and Expected Values.)")

    myTests().main()


.. activecode:: ps_2_2
    :language: python
    :autograde: unittest
    :hidecode:

    **2.** How long (how many characters) is the string in the variable ``sent``? Write code to assign the length of that string to a variable called ``len_of_sent``.

    How long is the string in the variable ``short_sent``? Write code to assign the value of that string's length to a variable ``short_len``.

    Write code to print out the value of ``short_len`` (and the value of len_of_sent, if you want!) so you can see it.

    Consider (ungraded but important): Why is the length of ``short_sent`` longer than 15 characters?

    Finally, write code to assign the index of the first ``'v'`` in the value of the variable ``sent`` TO a variable called ``index_of_v``. (Hint: we saw a method of the string class that can help with this)
    ~~~~
    sent = """
    He took his vorpal sword in hand:
    Long time the manxome foe he sought
    So rested he by the Tumtum tree,
    And stood awhile in thought.
    - Jabberwocky, Lewis Carroll (1832-1898)"""

    short_sent = """
    So much depends
    on
    """

    # Write your code here.


     =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
           self.assertEqual(len_of_sent, len(sent), "Testing that len_of_sent has been set to the length of the variable sent.")
        def testTwo(self):
           self.assertEqual(short_len,len(short_sent), "Testing that short_len has been set to the length of the variable short_sent")
        def testThree(self):
           self.assertEqual(index_of_v, sent.find('v'), "Testing that index_of_v has been set to the index of v in the variable sent.")
        def testFour(self):
           self.assertIn('20', self.getOutput(), "Testing that you printed the length of short_sent. (Don't worry about Actual and Expected Values.)")

    myTests().main()


.. activecode:: ps_2_3
    :language: python
    :autograde: unittest
    :hidecode:

    **3.** Assign the value of the third element of ``num_lst`` to a variable called ``third_elem``.

    Assign the value of the sixth element of ``num_lst`` to a variable called ``elem_sixth``.

    Assign the length of ``num_lst`` to a variable called ``num_lst_len``.

    *Consider:* what is the difference between ``mixed_bag[-1]`` and ``mixed_bag[-2]`` (you may want to print out those values or print out information about those values, so you can make sure you know what they are!)?

    Write code to print out the type of the third element of ``mixed_bag``.

    Write code to assign the **type of the fifth element of** ``mixed_bag`` to a variable called ``fifth_type``.

    Write code to assign the **type of the first element of** ``mixed_bag`` to a variable called ``another_type``.

    **Keep in mind:** All ordinal numbers in *instructions*, like "third" or "fifth" refer to the way HUMANS count. How do you write code to find the right things?
    ~~~~
    num_lst = [4,16,25,9,100,12,13]
    mixed_bag = ["hi", 4,6,8, 92.4, "see ya", "23", 23]

    # Write your code here:


    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
           self.assertEqual(third_elem, num_lst[2], "Testing that third_elem has been set to the third element of num_lst")
        def testTwo(self):
           self.assertEqual(elem_sixth, num_lst[5], "Testing that elem_sixth has been set to the sixth element of num_lst")
        def testThree(self):
           self.assertEqual(num_lst_len,len(num_lst), "Testing that num_len has been set to the length of num_lst")
        def testFour(self):
           self.assertEqual(fifth_type, type(mixed_bag[4]), "Testing that fifth_type has been set to the type of the fifth element in mixed_bag")
        def testFive(self):
           self.assertEqual(another_type, type(mixed_bag[0]), "Testing that another_type has been set to the type of the first element of mixed_bag")
        def testSix(self):
           self.assertIn('print', self.getEditorText(), "Testing that 'print' is in your code. (Don't worry about Actual and Expected Values.)")
        def testSeven(self):
           self.assertIn('int', self.getOutput(), "Testing that you printed the correct element of mixed_bag. (Don't worry about Actual and Expected Values.)")


    myTests().main()

.. activecode:: ps_2_4
    :include: addl_functions_2
    :language: python
    :hidecode:

    **4.** There is a function we are giving you for this problem set that takes two strings as inputs, and returns the length of both of those strings added together, called ``add_lengths``. We are also including the functions from Problem Set 1 called ``random_digit`` and ``square`` in this problem set. 

    Now, take a look at the following code and related questions, in this code window.
    ~~~~
    new_str = "'Twas brillig"
     
    y = add_lengths("receipt","receive")
     
    x = random_digit()
     
    z = new_str.find('b')
     
    l = new_str.find("'")
     
    # notice that this line of code is made up of a lot of different expressions
    fin_value = square(len(new_str)) + (z - l) + (x * random_digit())
     
    # DO NOT CHANGE ANY CODE ABOVE THIS LINE
    # But below here, putting print statements and running the code may help you!
     
    # The following questions are based on that code. All refer to the types of the 
    #variables and/or expressions after the above code is run.
     
    #####################   
     
    # Write a comment explaining each of the following, after each question.
    # Don't forget to press **run** to save!
     
    # What is square? 
     
    # What type of object does the expression square(len(new_str)) evaluate to?
     
    # What type is z?
     
    # What type is l?
     
    # What type is the expression z-l?
     
    # What type is x?
     
    # What is random_digit? How many inputs does it take?
     
    # What type does the expression x * random_digit() evaluate to?
     
    # Given all this information, what type will fin_value hold once all this code is run?

    ====

    print "\n\nThere are no tests for this problem"


.. activecode:: ps_2_5
    :language: python
    :autograde: unittest
    :hidecode:

    **5.** Write code to assign the number of characters in the string ``rv`` to a variable ``num_chars``. Then write code to assign the number of words in the string ``rv`` to the variable ``num_words``. (Hint: remember how to split strings?)
    ~~~~
    rv = """Once upon a midnight dreary, while I pondered, weak and weary,
        Over many a quaint and curious volume of forgotten lore,
        While I nodded, nearly napping, suddenly there came a tapping,
        As of some one gently rapping, rapping at my chamber door.
        'Tis some visitor, I muttered, tapping at my chamber door;
        Only this and nothing more."""

    # Write your code here!

    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
           self.assertEqual(num_chars, len(rv), "Testing that num_chars has been set to the length of rv")
           self.assertEqual(num_words, len(rv.split()), "Testing that num_words has been set to the number of words in rv")

    myTests().main()


.. external:: ps2_dyu

  Submit your `Demonstrate Your Understanding <https://umich.instructure.com/courses/105657/assignments/131285>`_ assignment for this week.

The code below is NOT a problem in your problem set. You do not need to edit it or look at it (in fact, you should NOT change it). These are function definitions that we are providing for you to use. You will learn more about this in a couple of weeks!

.. activecode:: addl_functions_2
    :nopre:
    :hidecode:

    def square(num):
        return num**2

    def greeting(st):
        #st = str(st) # just in case
        return "Hello, " + st

    def random_digit():
        import random
        return random.choice([0,1,2,3,4,5,6,7,8,9])
      
    def add_lengths(str1, str2):
        return len(str1) + len(str2)
